from datetime import datetime
import sqlite3
from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)
DB_NAME = "phones.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/google257792cf7979e332.html")
def google_verify():
    return app.send_static_file("google257792cf7979e332.html")

@app.route("/")
def home():
    search = request.args.get("search", "").strip()
    brand = request.args.get("brand", "").strip()
    budget = request.args.get("budget", "").strip()
    sort = request.args.get("sort", "").strip()

    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if search:
        query += " AND name LIKE ?"
        params.append(f"%{search}%")

    if brand:
        query += " AND brand = ?"
        params.append(brand)

    if budget:
        try:
            query += " AND price <= ?"
            params.append(int(budget))
        except ValueError:
            pass

    # Dynamic sorting
    if sort == "price_low":
        query += " ORDER BY price ASC"
    elif sort == "price_high":
        query += " ORDER BY price DESC"
    else:
        query += " ORDER BY id DESC"

    with get_db() as conn:
        phones = conn.execute(query, params).fetchall()

    return render_template(
        "index.html",
        phones=phones,
        search=search,
        brand=brand,
        budget=budget,
        sort=sort
    )

@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    recommended_phone = None

    if request.method == "POST":
        try:
            budget = int(request.form.get("budget", 0))
            battery_weight = int(request.form.get("battery", 0))
            camera_weight = int(request.form.get("camera", 0))
            gaming_weight = int(request.form.get("gaming", 0))
        except ValueError:
            return render_template("recommend.html", recommended_phone=None)

        with get_db() as conn:
            phones = conn.execute("SELECT * FROM phones WHERE price <= ?", (budget,)).fetchall()

        best_score = -1

        for phone in phones:
            try:
                battery_str = "".join(filter(str.isdigit, str(phone["battery"] or "")))
                camera_str = "".join(filter(str.isdigit, str(phone["camera"] or "")))
                
                battery = int(battery_str) if battery_str else 0
                camera = int(camera_str) if camera_str else 0
            except (ValueError, TypeError):
                continue

            gaming = phone["gaming_score"] if phone["gaming_score"] else 0
            rating = phone["rating"] if phone["rating"] else 0.0

            # Scoring Algorithm
            score = 0
            score += (battery / 1000) * battery_weight
            score += (camera / 10) * camera_weight
            score += gaming * gaming_weight
            score += rating * 20

            if score > best_score:
                best_score = score
                recommended_phone = phone

    return render_template("recommend.html", recommended_phone=recommended_phone)

@app.route("/phone/<int:id>")
def phone(id):
    with get_db() as conn:
        phone_data = conn.execute(
            "SELECT * FROM phones WHERE id=?",
            (id,)
        ).fetchone()

        if not phone_data:
            abort(404)

        related = conn.execute(
            """
            SELECT *
            FROM phones
            WHERE brand=?
            AND id != ?
            LIMIT 4
            """,
            (phone_data["brand"], id)
        ).fetchall()

    return render_template(
        "phone.html",
        phone=phone_data,
        related=related
    )

@app.route("/compare", methods=["GET", "POST"])
def compare():
    with get_db() as conn:
        phones = conn.execute("SELECT * FROM phones ORDER BY name").fetchall()
        phone1, phone2 = None, None

        if request.method == "POST":
            id1 = request.form.get("phone1")
            id2 = request.form.get("phone2")

            if id1 and id1.isdigit():
                phone1 = conn.execute("SELECT * FROM phones WHERE id=?", (int(id1),)).fetchone()

            if id2 and id2.isdigit():
                phone2 = conn.execute("SELECT * FROM phones WHERE id=?", (int(id2),)).fetchone()

    return render_template("compare.html", phones=phones, phone1=phone1, phone2=phone2)

@app.route("/compare/<int:id1>/<int:id2>")
def compare_two(id1, id2):
    with get_db() as conn:
        phone1 = conn.execute("SELECT * FROM phones WHERE id=?", (id1,)).fetchone()
        phone2 = conn.execute("SELECT * FROM phones WHERE id=?", (id2,)).fetchone()

    if not phone1 or not phone2:
        abort(404)

    return render_template("compare_two.html", phone1=phone1, phone2=phone2)

# --- CLEANED DYNAMIC CATEGORY FILTERING ---
CATEGORIES = {
    "best-under-15000": ("Best Phones Under ₹15,000", "SELECT * FROM phones WHERE price <= 15000 ORDER BY rating DESC"),
    "best-under-25000": ("Best Phones Under ₹25,000", "SELECT * FROM phones WHERE price <= 25000 ORDER BY rating DESC"),
    "best-under-50000": ("Best Phones Under ₹50,000", "SELECT * FROM phones WHERE price <= 50000 ORDER BY rating DESC"),
    "best-samsung-phones": ("Best Samsung Phones", "SELECT * FROM phones WHERE brand='Samsung' ORDER BY rating DESC"),
    "best-oneplus-phones": ("Best OnePlus Phones", "SELECT * FROM phones WHERE brand='OnePlus' ORDER BY rating DESC"),
    "best-gaming-phones": ("Best Gaming Phones", "SELECT * FROM phones ORDER BY gaming_score DESC"),
    "best-camera-phones": ("Best Camera Phones", "SELECT * FROM phones ORDER BY CAST(REPLACE(REPLACE(camera, 'MP', ''), ' ', '') AS INTEGER) DESC"),
    "best-battery-phones": ("Best Battery Phones", "SELECT * FROM phones ORDER BY CAST(REPLACE(REPLACE(battery, 'mAh', ''), ' ', '') AS INTEGER) DESC"),
    "best-camera-under-25000": ("Best Camera Phones Under ₹25,000", "SELECT * FROM phones WHERE price <= 25000 ORDER BY CAST(REPLACE(REPLACE(camera, 'MP', ''), ' ', '') AS INTEGER) DESC"),
    "best-under-10000": ("Best Phones Under ₹10,000", "SELECT * FROM phones WHERE price <= 10000 ORDER BY rating DESC"),
    "best-under-20000": ("Best Phones Under ₹20,000", "SELECT * FROM phones WHERE price <= 20000 ORDER BY rating DESC"),
    "best-under-30000": ("Best Phones Under ₹30,000", "SELECT * FROM phones WHERE price <= 30000 ORDER BY rating DESC"),
    "best-under-40000": ("Best Phones Under ₹40,000", "SELECT * FROM phones WHERE price <= 40000 ORDER BY rating DESC"),
    "best-under-60000": ("Best Phones Under ₹60,000", "SELECT * FROM phones WHERE price <= 60000 ORDER BY rating DESC"),
    "best-vivo-phones": ("Best Vivo Phones", "SELECT * FROM phones WHERE brand='Vivo' ORDER BY rating DESC"),
    "best-realme-phones": ("Best Realme Phones", "SELECT * FROM phones WHERE brand='Realme' ORDER BY rating DESC"),
    "best-apple-phones": ("Best Apple iPhones", "SELECT * FROM phones WHERE brand='Apple' ORDER BY rating DESC"),
    "best-iqoo-phones": ("Best iQOO Phones", "SELECT * FROM phones WHERE brand='iQOO' ORDER BY rating DESC"),
    "best-poco-phones": ("Best POCO Phones", "SELECT * FROM phones WHERE brand='POCO' ORDER BY rating DESC")
}

@app.route("/category/<string:cat_slug>")
def dynamic_category(cat_slug):
    if cat_slug not in CATEGORIES:
        abort(404)
        
    title, query = CATEGORIES[cat_slug]
    with get_db() as conn:
        phones = conn.execute(query).fetchall()
        
    return render_template("category.html", title=title, phones=phones)

@app.route("/<path:slug>")
def seo_page(slug):
    if slug in CATEGORIES:
        return dynamic_category(slug)
    abort(404)

@app.route("/sitemap.xml")
def sitemap():
    pages = []
    today = datetime.now().date().isoformat()

    static_urls = [
        "/",
        "/compare",
        "/recommend",
        "/about",
        "/contact",
        "/privacy-policy",
        "/terms"
    ]

    for slug in CATEGORIES.keys():
        static_urls.append(f"/{slug}")

    for url in static_urls:
        pages.append(f"""
        <url>
            <loc>https://gadgetadvisor.onrender.com{url}</loc>
            <lastmod>{today}</lastmod>
        </url>
        """)

    with get_db() as conn:
        phones = conn.execute("SELECT id FROM phones").fetchall()

    for phone in phones:
        pages.append(f"""
        <url>
            <loc>https://gadgetadvisor.onrender.com/phone/{phone['id']}</loc>
            <lastmod>{today}</lastmod>
        </url>
        """)

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(pages)}
</urlset>"""

    return Response(xml, mimetype="application/xml")

# --- STATIC CONTENT ROUTES ---
@app.route("/about")
def about(): return render_template("about.html")

@app.route("/contact")
def contact(): return render_template("contact.html")

@app.route("/privacy-policy")
def privacy_policy(): return render_template("privacy.html")

@app.route("/terms")
def terms(): return render_template("terms.html")

if __name__ == "__main__":
    app.run()
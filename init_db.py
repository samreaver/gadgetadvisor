import sqlite3

conn = sqlite3.connect("phones.db")
cursor = conn.cursor()

# Drop the old table layout so SQLite can recreate it with the new columns
cursor.execute("DROP TABLE IF EXISTS phones")

# Create the fresh table structure
cursor.execute("""
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    price INTEGER,
    ram TEXT,
    storage TEXT,
    battery TEXT,
    camera TEXT,
    image TEXT,
    rating REAL,
    gaming_score INTEGER,
    processor TEXT
)
""")

phones = [
    # --- SAMSUNG ---
    ('Samsung Galaxy A17', 'Samsung', 14999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/samsung-a17.jpg', 4.2, 65, 'Exynos 1330'),
    ('Samsung Galaxy M56 5G', 'Samsung', 23999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/galaxy-m56.jpg', 4.5, 82, 'Exynos 1480'),
    ('Samsung Galaxy S24 FE', 'Samsung', 44999, '8GB', '128GB', '4700mAh', '50MP', '/static/images/s24-fe.jpg', 4.7, 90, 'Exynos 2400e'),
    ('Samsung Galaxy S25', 'Samsung', 74999, '12GB', '256GB', '4000mAh', '50MP', '/static/images/samsung-s25.jpg', 4.8, 95, 'Snapdragon 8 Elite'),
    ('Samsung Galaxy S25 Ultra', 'Samsung', 124999, '12GB', '256GB', '5000mAh', '200MP', '/static/images/s25-ultra.jpg', 4.9, 98, 'Snapdragon 8 Elite'),
    ('Samsung Galaxy A35', 'Samsung', 27999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/samsung-a35.jpg', 4.3, 70, 'Exynos 1380'),
    ('Samsung Galaxy A55', 'Samsung', 39999, '12GB', '256GB', '5000mAh', '50MP', '/static/images/samsung-a55.jpg', 4.5, 78, 'Exynos 1480'),
    ('Samsung Galaxy F15 5G', 'Samsung', 12999, '6GB', '128GB', '6000mAh', '50MP', '/static/images/samsung-f15.jpg', 4.1, 58, 'Dimensity 6100+'),
    ('Samsung Galaxy M35', 'Samsung', 19999, '8GB', '128GB', '6000mAh', '50MP', '/static/images/samsung-m35.jpg', 4.3, 68, 'Exynos 1280'),
    ('Samsung Galaxy Z Fold 6', 'Samsung', 164999, '12GB', '256GB', '4400mAh', '50MP', '/static/images/z-fold6.jpg', 4.7, 94, 'Snapdragon 8 Gen 3'),
    ('Samsung Galaxy Z Flip 6', 'Samsung', 109999, '12GB', '256GB', '4000mAh', '50MP', '/static/images/z-flip6.jpg', 4.6, 92, 'Snapdragon 8 Gen 3'),
    ('Samsung Galaxy A06', 'Samsung', 9999, '4GB', '64GB', '5000mAh', '50MP', '/static/images/samsung-a06.jpg', 3.9, 45, 'Helio G85'),

    # --- ONEPLUS ---
    ('OnePlus Nord CE6 Lite', 'OnePlus', 16999, '8GB', '128GB', '5500mAh', '108MP', '/static/images/nord-ce6-lite.jpg', 4.4, 75, 'Snapdragon 695'),
    ('OnePlus 13R', 'OnePlus', 42999, '12GB', '256GB', '6000mAh', '50MP', '/static/images/oneplus-13r.jpg', 4.8, 95, 'Snapdragon 8 Gen 3'),
    ('OnePlus Nord CE5', 'OnePlus', 24999, '8GB', '128GB', '7100mAh', '50MP', '/static/images/nord-ce5.jpg', 4.5, 84, 'Snapdragon 7 Gen 3'),
    ('OnePlus 13', 'OnePlus', 69999, '16GB', '512GB', '6000mAh', '50MP', '/static/images/oneplus-13.jpg', 4.9, 99, 'Snapdragon 8 Elite'),
    ('OnePlus Nord 4', 'OnePlus', 29999, '8GB', '256GB', '5500mAh', '50MP', '/static/images/nord-4.jpg', 4.6, 88, 'Snapdragon 7+ Gen 3'),
    ('OnePlus Nord CE4', 'OnePlus', 24999, '8GB', '128GB', '5500mAh', '50MP', '/static/images/nord-ce4.jpg', 4.5, 83, 'Snapdragon 7 Gen 3'),
    ('OnePlus 12', 'OnePlus', 64999, '12GB', '256GB', '5400mAh', '50MP', '/static/images/oneplus-12.jpg', 4.8, 93, 'Snapdragon 8 Gen 3'),
    ('OnePlus Open 2', 'OnePlus', 139999, '16GB', '512GB', '5050mAh', '48MP', '/static/images/oneplus-open2.jpg', 4.8, 96, 'Snapdragon 8 Elite'),

    # --- XIAOMI / REDMI ---
    ('Redmi Note 14', 'Xiaomi', 14999, '6GB', '128GB', '5110mAh', '50MP', '/static/images/redmi-note14.jpg', 4.3, 72, 'Dimensity 7025'),
    ('Redmi Note 14 Pro', 'Xiaomi', 21999, '8GB', '256GB', '5500mAh', '50MP', '/static/images/redmi-note14-pro.jpg', 4.5, 81, 'Dimensity 7300 Ultra'),
    ('Redmi Note 14 Pro Plus', 'Xiaomi', 28999, '12GB', '256GB', '6200mAh', '50MP', '/static/images/redmi-note14-pro-plus.jpg', 4.6, 85, 'Snapdragon 7s Gen 3'),
    ('Xiaomi 15', 'Xiaomi', 54999, '12GB', '256GB', '5400mAh', '50MP', '/static/images/xiaomi-15.jpg', 4.8, 96, 'Snapdragon 8 Elite'),
    ('Xiaomi 15 Pro', 'Xiaomi', 68999, '16GB', '512GB', '6100mAh', '50MP', '/static/images/xiaomi-15-pro.jpg', 4.9, 97, 'Snapdragon 8 Elite'),
    ('Redmi 14C', 'Xiaomi', 8999, '4GB', '128GB', '5160mAh', '50MP', '/static/images/redmi-14c.jpg', 4.0, 48, 'Helio G81 Ultra'),
    ('Redmi 13 5G', 'Xiaomi', 12999, '6GB', '128GB', '5030mAh', '108MP', '/static/images/redmi-13-5g.jpg', 4.2, 60, 'Snapdragon 4 Gen 2'),
    ('Xiaomi 14T Pro', 'Xiaomi', 49999, '12GB', '512GB', '5000mAh', '50MP', '/static/images/xiaomi-14t-pro.jpg', 4.7, 94, 'Dimensity 9300+'),

    # --- POCO ---
    ('POCO X7 Pro', 'POCO', 21999, '8GB', '256GB', '6500mAh', '50MP', '/static/images/poco-x7.jpg', 4.7, 93, 'Dimensity 8400'),
    ('POCO M8', 'POCO', 12999, '8GB', '128GB', '6000mAh', '50MP', '/static/images/poco-m8.jpg', 4.2, 70, 'Snapdragon 6 Gen 1'),
    ('POCO F7 Pro', 'POCO', 34999, '12GB', '256GB', '5500mAh', '50MP', '/static/images/poco-f7-pro.jpg', 4.8, 96, 'Snapdragon 8 Gen 3'),
    ('POCO X6 Neo', 'POCO', 14999, '8GB', '128GB', '5000mAh', '108MP', '/static/images/poco-x6-neo.jpg', 4.2, 66, 'Dimensity 6080'),
    ('POCO M6 Plus', 'POCO', 11999, '6GB', '128GB', '5030mAh', '108MP', '/static/images/poco-m6-plus.jpg', 4.1, 59, 'Snapdragon 4 Gen 2 AE'),
    ('POCO F6', 'POCO', 27999, '8GB', '256GB', '5000mAh', '50MP', '/static/images/poco-f6.jpg', 4.6, 91, 'Snapdragon 8s Gen 3'),

    # --- REALME ---
    ('Realme P4 Pro', 'Realme', 24999, '8GB', '256GB', '7000mAh', '50MP', '/static/images/realme-p4-pro.jpg', 4.6, 88, 'Snapdragon 7s Gen 3'),
    ('Realme P3 Ultra', 'Realme', 22999, '8GB', '128GB', '6000mAh', '50MP', '/static/images/realme-p3-ultra.jpg', 4.5, 86, 'Dimensity 8350'),
    ('Realme GT 7 Pro', 'Realme', 59999, '16GB', '512GB', '6500mAh', '50MP', '/static/images/realme-gt7-pro.jpg', 4.9, 98, 'Snapdragon 8 Elite'),
    ('Realme 14 Pro Plus', 'Realme', 29999, '8GB', '256GB', '5200mAh', '50MP', '/static/images/realme-14-pro-plus.jpg', 4.6, 84, 'Dimensity 7300'),
    ('Realme 14x 5G', 'Realme', 13999, '6GB', '128GB', '5000mAh', '50MP', '/static/images/realme-14x.jpg', 4.1, 64, 'Dimensity 6300'),
    ('Realme C65 5G', 'Realme', 10499, '4GB', '64GB', '5000mAh', '50MP', '/static/images/realme-c65.jpg', 4.0, 55, 'Dimensity 6300'),
    ('Realme Narzo 70 Turbo', 'Realme', 16999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/narzo-70-turbo.jpg', 4.4, 80, 'Dimensity 7300 Energy'),
    ('Realme GT Neo 6', 'Realme', 25999, '12GB', '256GB', '5500mAh', '50MP', '/static/images/gt-neo-6.jpg', 4.6, 90, 'Snapdragon 7+ Gen 3'),

    # --- VIVO ---
    ('Vivo T4', 'Vivo', 24999, '8GB', '128GB', '7300mAh', '50MP', '/static/images/vivo-t4.jpg', 4.6, 85, 'Snapdragon 7s Gen 3'),
    ('Vivo X200', 'Vivo', 65999, '12GB', '256GB', '5800mAh', '50MP', '/static/images/vivo-x200.jpg', 4.8, 94, 'Dimensity 9400'),
    ('Vivo X200 Pro', 'Vivo', 84999, '16GB', '512GB', '6000mAh', '200MP', '/static/images/vivo-x200-pro.jpg', 4.9, 96, 'Dimensity 9400'),
    ('Vivo V40 Pro', 'Vivo', 49999, '12GB', '512GB', '5500mAh', '50MP', '/static/images/vivo-v40-pro.jpg', 4.7, 89, 'Dimensity 9200+'),
    ('Vivo V40e', 'Vivo', 28999, '8GB', '128GB', '5500mAh', '50MP', '/static/images/vivo-v40e.jpg', 4.4, 76, 'Dimensity 7300'),
    ('Vivo T3x 5G', 'Vivo', 13499, '6GB', '128GB', '6000mAh', '50MP', '/static/images/vivo-t3x.jpg', 4.3, 71, 'Snapdragon 6 Gen 1'),
    ('Vivo Y200 AI', 'Vivo', 18999, '8GB', '128GB', '6000mAh', '50MP', '/static/images/vivo-y200-ai.jpg', 4.2, 66, 'Snapdragon 4 Gen 2'),

    # --- IQOO ---
    ('iQOO Neo 10R', 'iQOO', 27999, '8GB', '128GB', '6400mAh', '50MP', '/static/images/neo10r.jpg', 4.7, 96, 'Snapdragon 8s Gen 4'),
    ('iQOO Z11x', 'iQOO', 22999, '8GB', '128GB', '6500mAh', '50MP', '/static/images/z11x.jpg', 4.4, 83, 'Snapdragon 7 Gen 3'),
    ('iQOO 13', 'iQOO', 54999, '12GB', '256GB', '6150mAh', '50MP', '/static/images/iqoo-13.jpg', 4.9, 99, 'Snapdragon 8 Elite'),
    ('iQOO Neo 10 Pro', 'iQOO', 38999, '12GB', '256GB', '6100mAh', '50MP', '/static/images/iqoo-neo10-pro.jpg', 4.8, 97, 'Dimensity 9400'),
    ('iQOO Z9s Pro', 'iQOO', 24999, '8GB', '128GB', '5500mAh', '50MP', '/static/images/iqoo-z9s-pro.jpg', 4.5, 84, 'Snapdragon 7 Gen 3'),
    ('iQOO Z9 Lite', 'iQOO', 10499, '4GB', '128GB', '5000mAh', '50MP', '/static/images/iqoo-z9-lite.jpg', 4.1, 56, 'Dimensity 6300'),

    # --- NOTHING / CMF ---
    ('Nothing Phone 3a', 'Nothing', 24999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/nothing-3a.jpg', 4.5, 82, 'Snapdragon 7s Gen 3'),
    ('Nothing Phone 3a Pro', 'Nothing', 29999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/phone3a-pro.jpg', 4.6, 86, 'Snapdragon 7s Gen 3'),
    ('Nothing Phone 3', 'Nothing', 44999, '12GB', '256GB', '5000mAh', '50MP', '/static/images/nothing-phone-3.jpg', 4.7, 92, 'Snapdragon 8s Gen 3'),
    ('CMF Phone 2', 'Nothing', 17999, '8GB', '128GB', '5200mAh', '50MP', '/static/images/cmf-phone-2.jpg', 4.4, 78, 'Dimensity 7300'),

    # --- MOTOROLA ---
    ('Motorola Edge 60 Fusion', 'Motorola', 21999, '8GB', '128GB', '5500mAh', '50MP', '/static/images/edge60fusion.jpg', 4.5, 84, 'Dimensity 7400'),
    ('Motorola Edge 50 Ultra', 'Motorola', 54999, '16GB', '1TB', '4500mAh', '50MP', '/static/images/edge50-ultra.jpg', 4.7, 91, 'Snapdragon 8s Gen 3'),
    ('Motorola Edge 50 Pro', 'Motorola', 31999, '12GB', '256GB', '4500mAh', '50MP', '/static/images/edge50-pro.jpg', 4.5, 82, 'Snapdragon 7 Gen 3'),
    ('Motorola Edge 50 Neo', 'Motorola', 23999, '8GB', '256GB', '4310mAh', '50MP', '/static/images/edge50-neo.jpg', 4.4, 75, 'Dimensity 7300'),
    ('Moto G85 5G', 'Motorola', 17999, '8GB', '128GB', '5000mAh', '50MP', '/static/images/moto-g85.jpg', 4.3, 70, 'Snapdragon 6s Gen 3'),
    ('Moto G64 5G', 'Motorola', 14999, '8GB', '128GB', '6000mAh', '50MP', '/static/images/moto-g64.jpg', 4.2, 73, 'Dimensity 7025'),
    ('Moto G45 5G', 'Motorola', 10999, '4GB', '64GB', '5000mAh', '50MP', '/static/images/moto-g45.jpg', 4.0, 62, 'Snapdragon 6s Gen 3'),
    ('Motorola Razr 50 Ultra', 'Motorola', 89999, '12GB', '512GB', '4000mAh', '50MP', '/static/images/razr-50-ultra.jpg', 4.6, 90, 'Snapdragon 8s Gen 3'),

    # --- OPPO ---
    ('OPPO K13', 'OPPO', 22999, '8GB', '128GB', '7000mAh', '50MP', '/static/images/oppo-k13.jpg', 4.5, 83, 'Snapdragon 7 Gen 3'),
    ('OPPO Find X8 Pro', 'OPPO', 99999, '16GB', '512GB', '5910mAh', '50MP', '/static/images/oppo-find-x8-pro.jpg', 4.9, 96, 'Dimensity 9400'),
    ('OPPO Find X8', 'OPPO', 69999, '12GB', '256GB', '5630mAh', '50MP', '/static/images/oppo-find-x8.jpg', 4.8, 95, 'Dimensity 9400'),
    ('OPPO Reno 13 Pro', 'OPPO', 42999, '12GB', '512GB', '5600mAh', '50MP', '/static/images/oppo-reno13-pro.jpg', 4.6, 86, 'Dimensity 8350'),
    ('OPPO Reno 13', 'OPPO', 32999, '8GB', '256GB', '5600mAh', '50MP', '/static/images/oppo-reno13.jpg', 4.4, 80, 'Dimensity 8300'),
    ('OPPO F27 Pro Plus', 'OPPO', 27999, '8GB', '256GB', '5000mAh', '64MP', '/static/images/oppo-f27-pro.jpg', 4.3, 72, 'Dimensity 7050'),
    ('OPPO K12x 5G', 'OPPO', 12999, '6GB', '128GB', '5100mAh', '32MP', '/static/images/oppo-k12x.jpg', 4.1, 57, 'Dimensity 6300'),

    # --- APPLE ---
    ('Apple iPhone 16', 'Apple', 79999, '8GB', '128GB', '3561mAh', '48MP', '/static/images/iphone-16.jpg', 4.9, 92, 'Apple A18'),
    ('Apple iPhone 16 Plus', 'Apple', 89999, '8GB', '128GB', '4674mAh', '48MP', '/static/images/iphone16-plus.jpg', 4.8, 93, 'Apple A18'),
    ('Apple iPhone 16 Pro', 'Apple', 119999, '8GB', '128GB', '3582mAh', '48MP', '/static/images/iphone16-pro.jpg', 4.9, 97, 'Apple A18 Pro'),
    ('Apple iPhone 16 Pro Max', 'Apple', 144999, '8GB', '256GB', '4685mAh', '48MP', '/static/images/iphone16-promax.jpg', 4.9, 99, 'Apple A18 Pro'),
    ('Apple iPhone 15', 'Apple', 65999, '6GB', '128GB', '3349mAh', '48MP', '/static/images/iphone15.jpg', 4.7, 86, 'Apple A16 Bionic'),
    ('Apple iPhone SE 4', 'Apple', 49999, '8GB', '128GB', '3279mAh', '48MP', '/static/images/iphone-se4.jpg', 4.5, 89, 'Apple A18'),

    # --- GOOGLE ---
    ('Google Pixel 9', 'Google', 79999, '12GB', '128GB', '4700mAh', '50MP', '/static/images/pixel-9.jpg', 4.6, 80, 'Tensor G4'),
    ('Google Pixel 9 Pro', 'Google', 109999, '16GB', '256GB', '4700mAh', '50MP', '/static/images/pixel-9-pro.jpg', 4.8, 83, 'Tensor G4'),
    ('Google Pixel 9 Pro Max', 'Google', 119999, '16GB', '256GB', '5060mAh', '50MP', '/static/images/pixel-9-promax.jpg', 4.8, 84, 'Tensor G4'),
    ('Google Pixel 9a', 'Google', 43999, '8GB', '128GB', '5000mAh', '64MP', '/static/images/pixel-9a.jpg', 4.5, 78, 'Tensor G4'),
    ('Google Pixel 8a', 'Google', 39999, '8GB', '128GB', '4492mAh', '64MP', '/static/images/pixel-8a.jpg', 4.4, 75, 'Tensor G3'),

    # --- INFINIX ---
    ('Infinix GT 20 Pro', 'Infinix', 24999, '8GB', '256GB', '5000mAh', '108MP', '/static/images/infinix-gt20-pro.jpg', 4.5, 89, 'Dimensity 8200 Ultimate'),
    ('Infinix Zero 40 5G', 'Infinix', 27999, '12GB', '256GB', '5000mAh', '108MP', '/static/images/infinix-zero40.jpg', 4.4, 82, 'Dimensity 8200 Ultimate'),
    ('Infinix Note 40 Pro', 'Infinix', 21999, '8GB', '256GB', '5000mAh', '108MP', '/static/images/infinix-note40-pro.jpg', 4.3, 71, 'Dimensity 7020'),
    ('Infinix Hot 50 5G', 'Infinix', 9999, '4GB', '128GB', '5000mAh', '48MP', '/static/images/infinix-hot50.jpg', 4.0, 58, 'Dimensity 6300'),

    # --- TECNO ---
    ('Tecno Pova 6 Pro', 'Tecno', 19999, '8GB', '256GB', '6000mAh', '108MP', '/static/images/tecno-pova6-pro.jpg', 4.4, 76, 'Dimensity 6080'),
    ('Tecno Camon 30 Premier', 'Tecno', 39999, '12GB', '512GB', '5000mAh', '50MP', '/static/images/tecno-camon30-premier.jpg', 4.5, 87, 'Dimensity 8200 Ultimate'),
    ('Tecno Phantom V Fold 2', 'Tecno', 79999, '12GB', '512GB', '5750mAh', '50MP', '/static/images/phantom-v-fold2.jpg', 4.4, 88, 'Dimensity 9000+'),
    ('Tecno Spark 30 5G', 'Tecno', 11499, '6GB', '128GB', '5000mAh', '48MP', '/static/images/tecno-spark30.jpg', 4.1, 56, 'Dimensity 6300'),

    # --- HONOR ---
    ('Honor 200 Pro', 'Honor', 44999, '12GB', '512GB', '5200mAh', '50MP', '/static/images/honor-200-pro.jpg', 4.6, 90, 'Snapdragon 8s Gen 3'),
    ('Honor 200', 'Honor', 31999, '8GB', '256GB', '5200mAh', '50MP', '/static/images/honor-200.jpg', 4.4, 81, 'Snapdragon 7 Gen 3'),
    ('Honor X9b', 'Honor', 21999, '8GB', '256GB', '5800mAh', '108MP', '/static/images/honor-x9b.jpg', 4.3, 68, 'Snapdragon 6 Gen 1'),
    ('Honor Magic 6 Pro', 'Honor', 89999, '12GB', '512GB', '5600mAh', '50MP', '/static/images/honor-magic6-pro.jpg', 4.8, 94, 'Snapdragon 8 Gen 3'),

    # --- HMD / NOKIA ---
    ('HMD Skyline', 'HMD', 35999, '12GB', '256GB', '4600mAh', '108MP', '/static/images/hmd-skyline.jpg', 4.3, 79, 'Snapdragon 7s Gen 2'),
    ('HMD Crest Max', 'HMD', 14999, '8GB', '256GB', '5000mAh', '64MP', '/static/images/hmd-crest-max.jpg', 4.0, 55, 'Unisoc T760'),
    ('Nokia G42 5G', 'Nokia', 11999, '6GB', '128GB', '5000mAh', '50MP', '/static/images/nokia-g42.jpg', 4.1, 52, 'Snapdragon 480+'),

    # --- ASUS ---
    ('Asus ROG Phone 9', 'Asus', 79999, '16GB', '512GB', '5800mAh', '50MP', '/static/images/rog-phone-9.jpg', 4.9, 100, 'Snapdragon 8 Elite'),
    ('Asus ROG Phone 9 Pro', 'Asus', 99999, '24GB', '1TB', '5800mAh', '50MP', '/static/images/rog-phone-9pro.jpg', 5.0, 100, 'Snapdragon 8 Elite'),
    ('Asus Zenfone 11 Ultra', 'Asus', 69999, '12GB', '256GB', '5500mAh', '50MP', '/static/images/zenfone-11-ultra.jpg', 4.6, 93, 'Snapdragon 8 Gen 3')
]

cursor.executemany("""
INSERT INTO phones
(
    name,
    brand,
    price,
    ram,
    storage,
    battery,
    camera,
    image,
    rating,
    gaming_score,
    processor
)
VALUES (?,?,?,?,?,?,?,?,?,?,?)
""", phones)

conn.commit()

# Verify the count
cursor.execute("SELECT COUNT(*) FROM phones")
count = cursor.fetchone()[0]

conn.close()

print(f"Database recreated successfully with {count} phones.")
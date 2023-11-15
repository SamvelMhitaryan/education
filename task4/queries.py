CREATING_TABLE = '''CREATE TABLE IF NOT EXISTS weather (
        user_id SERIAL PRIMARY KEY,
        lon VARCHAR(50),
        lat VARCHAR(50),
        base VARCHAR(50), 
        temp INTEGER,
        feels_like INTEGER,
        sea_level INTEGER,
        visibility INTEGER,                    
        wind_speed FLOAT, 
        clouds_all INTEGER, 
        name VARCHAR(50), 
        created_at TIMESTAMP DEFAULT current_timestamp);'''

INSERTING_TABLE = '''INSERT INTO weather (lon, lat, base, temp, 
        feels_like, sea_level, visibility, wind_speed, clouds_all, name) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''


import json
from schemas import Response
from get_weather import get_weather_from_api
import psycopg2
from queries import CREATING_TABLE, INSERTING_TABLE
from settings import API_KEY, CITY_NAME

def record_file(json_data, file_name):
    with open(file_name, 'w') as text_file:
        x = json.dump(json_data, text_file, indent=4)

def validate_response(resp):
    answer = Response.model_validate(resp)
    return answer

def val_data():
    validated_data = validate_response(get_weather_from_api(CITY_NAME, API_KEY))
    return validated_data

def conn():
    try:
        conn = psycopg2.connect(dbname='mydatabase', user='user', password='password', host='localhost')
    except Exception as e:
        print(e, ' \n Can`t establish connection to database')
        return None
    return conn

def create_weather_table(conn):
    with conn.cursor() as curs:
        curs.execute(CREATING_TABLE)
        conn.commit() 
        
def inserting_table(conn, val_data):
    with conn.cursor() as curs:
        new_val_data = (
            val_data.coord.lon,
            val_data.coord.lat,
            val_data.base, 
            val_data.main.temp, 
            val_data.main.feels_like, 
            val_data.main.sea_level,
            val_data.visibility, 
            val_data.wind.speed, 
            val_data.clouds.all, 
            val_data.name
        )
        standart = INSERTING_TABLE

        curs.execute(standart, new_val_data)
        conn.commit()
    

def selecting_table(conn):
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM weather')
        result = curs.fetchall()
        return result 

import psycopg2
from utils import validate_response, create_weather_table, inserting_table, selecting_table
from get_weather import get_weather_from_api
from settings import API_KEY, CITY_NAME

def main():
    validated_data = validate_response(get_weather_from_api(CITY_NAME, API_KEY))

    try:
        conn = psycopg2.connect(dbname='mydatabase', user='user', password='password', host='localhost')
    except Exception as e:
        print(e, ' \n Can`t establish connection to database')
        return None
    
    create_weather_table(conn)
    inserting_table(conn, validated_data)
    a = selecting_table(conn)
    print(a) 
    
if __name__ == '__main__':
    main()


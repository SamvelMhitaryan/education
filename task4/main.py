import requests
import time
import os

from dotenv import load_dotenv
from typing import Any

load_dotenv()

max_retries = int(os.environ.get('max_retries'))
city_name = os.environ.get('city', 'Кисловодск')
API_KEY = os.environ.get('API_KEY')


def retry(max_retries):
    def wrapper(func):
        def inner(*args, **kwargs):
            counter = 0
            while counter <= max_retries:
                result = func(*args, **kwargs)
                print(counter, result)
                if result.get('cod') in {200, 201}:
                    return result
                counter += 1
                time.sleep(2)
                if counter > max_retries:
                    print(
                        'Превышено максимальное количество попыток. Запрос не удался.')
                    break
            return result
        return inner
    return wrapper


@retry(max_retries)
def get_weather_from_api(city: str, appid: str = 'API_KEY') -> dict[str, Any]:

    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    url = f'{BASE_URL}?appid={appid}&q={city}&lang=ru'
    response = requests.get(url).json()
    return response


weather_data = get_weather_from_api(city_name, API_KEY)
print(weather_data)

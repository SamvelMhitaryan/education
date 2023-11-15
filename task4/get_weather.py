import requests
import time
from settings import MAX_RETRIES
from typing import Any


def retry(max_retries):
    def wrapper(func):
        def inner(*args, **kwargs):
            counter = 0
            while counter <= max_retries:
                result = func(*args, **kwargs)
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


@retry(int(MAX_RETRIES))
def get_weather_from_api(city: str, appid: str = 'API_KEY', lang: str = 'ru') -> dict[str, Any]:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    url = f'{BASE_URL}?appid={appid}&q={city}&lang={lang}'
    response = requests.get(url).json()
    return response
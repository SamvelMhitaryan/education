import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = os.environ.get('MAX_RETRIES')
CITY_NAME = os.environ.get('CITY', 'Кисловодск')
API_KEY = os.environ.get('API_KEY')
LANGUAGE = os.environ.get('LANGUAGE')
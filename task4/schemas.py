'''pydantic models'''
from pydantic import BaseModel
from pydantic_settings import BaseSettings

class Coord(BaseModel):
    lon: float
    lat: float


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Base(BaseModel):
    base: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Visibility(BaseModel):
    visibility: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Clouds(BaseModel):
    all: int


class Dt(BaseModel):
    dt: int


class Sys(BaseModel):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int


class Response(BaseModel):
    coord: Coord 
    weather: list[Weather]
    base: str  # Base
    main: Main
    visibility: int  # Visibility
    wind: Wind
    clouds: Clouds
    dt: int  # Dt
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int


class PostgresSettings(BaseSettings):
    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

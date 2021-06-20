from pydantic import BaseSettings


class Config(BaseSettings):
    service_name: str = 'weather_app'
    secret_key: str = 'thisisasecretkey'


config = Config()

from fastapi import FastAPI

from api.endpoints import health_check, weather


def create_api():
    api = FastAPI()
    api.include_router(health_check.router, prefix='/api')
    api.include_router(weather.router, prefix='/api')
    return api

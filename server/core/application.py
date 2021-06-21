from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import health_check, weather

# load routers
def create_api():
    origins = ["*"]
    api = FastAPI()
    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # healthCheck router
    api.include_router(health_check.router, prefix='/api')
    # weather routers
    api.include_router(weather.router, prefix='/api')
    return api

from fastapi import APIRouter, Response, status, Depends
from typing import Optional
import requests
from sqlalchemy.orm import Session
from middleware import crud
from models import user
from core.database import SessionLocal, engine

user.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/weather')
def read_root(res: Response, db: Session = Depends(get_db), name: Optional[str] = None, city: Optional[str] = None):
    try:
        if name:
            # Check user in DB
            db_user = crud.get_user(db, name=name)
            if db_user:
                if city:
                    # update user city
                    crud.update_user(db, name, city)
                else:
                    # get city from DB if there is no city on query
                    city = db_user.city
            else:
                # new user add to DB
                if city:
                    crud.create_user(db, name, city)
                else:
                    # new user has not city on query
                    res.status_code = status.HTTP_400_BAD_REQUEST
                    return {'msg': 'Where is city?'}
            if city:
                weather = requests.get(
                    "https://api.weatherapi.com/v1/forecast.json?key=e9c23a3c8b4040488e7112737212006&q=" + city + "&days=7&aqi=no&alerts=no").json()
                return {
                    'location': weather['location']['country'] + ' - ' + weather['location']['region'] + ' - ' +
                                weather['location']['name'],
                    'today': {
                        'temp': weather['forecast']['forecastday'][0]['day']['avgtemp_c'],
                        'text': weather['forecast']['forecastday'][0]['day']['condition']['text'],
                        'icon': weather['forecast']['forecastday'][0]['day']['condition']['icon']
                    },
                    'tomorrow': {
                        'temp': weather['forecast']['forecastday'][1]['day']['avgtemp_c'],
                        'text': weather['forecast']['forecastday'][1]['day']['condition']['text'],
                        'icon': weather['forecast']['forecastday'][1]['day']['condition']['icon']
                    },
                    'the day after tomorrow': {
                        'temp': weather['forecast']['forecastday'][2]['day']['avgtemp_c'],
                        'text': weather['forecast']['forecastday'][2]['day']['condition']['text'],
                        'icon': weather['forecast']['forecastday'][2]['day']['condition']['icon']
                    }
                }
            else:
                return {'msg': 'Where is city'}
        else:
            res.status_code = status.HTTP_400_BAD_REQUEST
            return {'msg': 'Name can not be null'}
    except:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {'msg': 'A problem was occured to find city'}

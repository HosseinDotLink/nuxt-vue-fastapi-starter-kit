from sqlalchemy.orm import Session

from models.user import User


def get_user(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def create_user(db: Session, name: str, city: str):
    db_user = User(name = name, city= city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, name: str, city: str):
    db_user = db.query(User).filter(User.name == name).first()
    db_user.city = city
    db.commit()
    db.refresh(db_user)
    return db_user
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate, hashed_password: str):
    """
    Create a new user in the database.
    """

    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    """
    Find a user by email.
    """

    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    """
    Find a user by ID.
    """

    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session):
    """
    Return all users.
    """

    return db.query(User).all()


def delete_user(db: Session, user_id: int):
    """
    Delete a user.
    """

    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()

    return user
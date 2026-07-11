from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate

from app.repositories.user_repository import (
    create_user as create_user_repo,
    get_user_by_email,
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def create_user(
    db: Session,
    user: UserCreate,
):
    """
    Register a new user.
    """

    existing_user = get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    hashed_password = hash_password(
        user.password,
    )

    new_user = create_user_repo(
        db=db,
        user=user,
        hashed_password=hashed_password,
    )

    return new_user


def login_user(
    db: Session,
    email: str,
    password: str,
):
    """
    Login user and return JWT token.
    """

    db_user = get_user_by_email(
        db,
        email,
    )

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        password,
        db_user.password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        data={
            "sub": str(db_user.id),
            "email": db_user.email,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
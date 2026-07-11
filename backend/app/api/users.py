from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.oauth2 import get_current_user
from app.db.session import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
)

from app.schemas.token_schema import Token

from app.services.user_service import (
    create_user,
    login_user,
)

router = APIRouter()


# ----------------------------
# Register User
# ----------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user)


# ----------------------------
# Login User (OAuth2)
# ----------------------------
@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return login_user(
        db=db,
        email=form_data.username,
        password=form_data.password,
    )


# ----------------------------
# Current User
# ----------------------------
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user=Depends(get_current_user),
):
    return current_user
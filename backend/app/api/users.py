from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
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
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


# ----------------------------
# Login User
# ----------------------------
@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user)
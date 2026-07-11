from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.oauth2 import get_current_user

from app.schemas.business_schema import (
    BusinessCreate,
    BusinessUpdate,
    BusinessResponse,
)

from app.services.business_service import (
    create_new_business,
    get_my_businesses,
    get_my_business,
    update_my_business,
    delete_my_business,
)

router = APIRouter()


# -----------------------------
# Create Business
# -----------------------------
@router.post(
    "/",
    response_model=BusinessResponse,
    status_code=201,
)
def create_business(
    business: BusinessCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_new_business(
        db=db,
        business=business,
        current_user=current_user,
    )


# -----------------------------
# Get All My Businesses
# -----------------------------
@router.get(
    "/",
    response_model=list[BusinessResponse],
)
def get_businesses(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_my_businesses(
        db=db,
        current_user=current_user,
    )


# -----------------------------
# Get Business By ID
# -----------------------------
@router.get(
    "/{business_id}",
    response_model=BusinessResponse,
)
def get_business(
    business_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_my_business(
        db=db,
        business_id=business_id,
        current_user=current_user,
    )


# -----------------------------
# Update Business
# -----------------------------
@router.put(
    "/{business_id}",
    response_model=BusinessResponse,
)
def update_business(
    business_id: int,
    business: BusinessUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return update_my_business(
        db=db,
        business_id=business_id,
        business_update=business,
        current_user=current_user,
    )


# -----------------------------
# Delete Business
# -----------------------------
@router.delete(
    "/{business_id}",
)
def delete_business(
    business_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return delete_my_business(
        db=db,
        business_id=business_id,
        current_user=current_user,
    )
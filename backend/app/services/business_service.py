from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.business_schema import (
    BusinessCreate,
    BusinessUpdate,
)

from app.repositories.business_repository import (
    create_business,
    get_business_by_id,
    get_businesses_by_owner,
    update_business,
    delete_business,
)


def create_new_business(
    db: Session,
    business: BusinessCreate,
    current_user,
):
    return create_business(
        db=db,
        business=business,
        owner_id=current_user.id,
    )


def get_my_businesses(
    db: Session,
    current_user,
):
    return get_businesses_by_owner(
        db=db,
        owner_id=current_user.id,
    )


def get_my_business(
    db: Session,
    business_id: int,
    current_user,
):
    business = get_business_by_id(
        db=db,
        business_id=business_id,
    )

    if business is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this business",
        )

    return business


def update_my_business(
    db: Session,
    business_id: int,
    business_update: BusinessUpdate,
    current_user,
):
    business = get_business_by_id(
        db=db,
        business_id=business_id,
    )

    if business is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this business",
        )

    return update_business(
        db=db,
        business=business,
        business_update=business_update,
    )


def delete_my_business(
    db: Session,
    business_id: int,
    current_user,
):
    business = get_business_by_id(
        db=db,
        business_id=business_id,
    )

    if business is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this business",
        )

    delete_business(
        db=db,
        business=business,
    )

    return {
        "message": "Business deleted successfully"
    }
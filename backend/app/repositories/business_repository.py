from typing import Optional

from sqlalchemy.orm import Session

from app.models.business_model import Business
from app.schemas.business_schema import (
    BusinessCreate,
    BusinessUpdate,
)


def create_business(
    db: Session,
    business: BusinessCreate,
    owner_id: int,
) -> Business:
    new_business = Business(
        name=business.name,
        description=business.description,
        industry=business.industry,
        phone=business.phone,
        email=business.email,
        website=str(business.website) if business.website else None,
        address=business.address,
        logo_url=str(business.logo_url) if business.logo_url else None,
        owner_id=owner_id,
    )

    db.add(new_business)
    db.commit()
    db.refresh(new_business)

    return new_business


def get_business_by_id(
    db: Session,
    business_id: int,
) -> Optional[Business]:

    return (
        db.query(Business)
        .filter(Business.id == business_id)
        .first()
    )


def get_businesses_by_owner(
    db: Session,
    owner_id: int,
) -> list[Business]:

    return (
        db.query(Business)
        .filter(Business.owner_id == owner_id)
        .all()
    )


def update_business(
    db: Session,
    business: Business,
    business_update: BusinessUpdate,
) -> Business:

    update_data = business_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(business, key, value)

    db.commit()
    db.refresh(business)

    return business


def delete_business(
    db: Session,
    business: Business,
) -> None:

    db.delete(business)
    db.commit()
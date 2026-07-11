from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.core.oauth2 import get_current_user

from app.models.user_model import User

from app.schemas.document_schema import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
)

from app.services.document_service import (
    create_new_document,
    get_document,
    get_my_documents,
    update_my_document,
    delete_my_document,
)

router = APIRouter()


@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_new_document(
        db=db,
        document=document,
        current_user=current_user,
    )


@router.get(
    "/business/{business_id}",
    response_model=List[DocumentResponse],
)
def get_documents(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_my_documents(
        db=db,
        business_id=business_id,
        current_user=current_user,
    )


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document_by_id(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_document(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )


@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
)
def update_document(
    document_id: int,
    document_update: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_my_document(
        db=db,
        document_id=document_id,
        document_update=document_update,
        current_user=current_user,
    )


@router.delete(
    "/{document_id}",
)
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_my_document(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )
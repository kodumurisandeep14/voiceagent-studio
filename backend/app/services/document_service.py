from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.document_schema import (
    DocumentCreate,
    DocumentUpdate,
)

from app.repositories.business_repository import (
    get_business_by_id,
)

from app.repositories.document_repository import (
    create_document,
    get_document_by_id,
    get_documents_by_business,
    update_document,
    delete_document,
)


def create_new_document(
    db: Session,
    document: DocumentCreate,
    current_user: User,
):
    business = get_business_by_id(
        db=db,
        business_id=document.business_id,
    )

    if business is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found",
        )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to upload documents to this business.",
        )

    return create_document(
        db=db,
        document=document,
    )


def get_document(
    db: Session,
    document_id: int,
    current_user: User,
):
    document = get_document_by_id(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    business = get_business_by_id(
        db=db,
        business_id=document.business_id,
    )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to view this document.",
        )

    return document


def get_my_documents(
    db: Session,
    business_id: int,
    current_user: User,
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
            detail="You do not have permission to access these documents.",
        )

    return get_documents_by_business(
        db=db,
        business_id=business_id,
    )


def update_my_document(
    db: Session,
    document_id: int,
    document_update: DocumentUpdate,
    current_user: User,
):
    document = get_document_by_id(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    business = get_business_by_id(
        db=db,
        business_id=document.business_id,
    )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this document.",
        )

    return update_document(
        db=db,
        document=document,
        document_update=document_update,
    )


def delete_my_document(
    db: Session,
    document_id: int,
    current_user: User,
):
    document = get_document_by_id(
        db=db,
        document_id=document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    business = get_business_by_id(
        db=db,
        business_id=document.business_id,
    )

    if business.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this document.",
        )

    delete_document(
        db=db,
        document=document,
    )

    return {
        "message": "Document deleted successfully"
    }
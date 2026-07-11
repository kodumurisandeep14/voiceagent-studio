from typing import Optional

from sqlalchemy.orm import Session

from app.models.document_model import Document
from app.schemas.document_schema import (
    DocumentCreate,
    DocumentUpdate,
)


def create_document(
    db: Session,
    document: DocumentCreate,
) -> Document:

    new_document = Document(
        filename=document.filename,
        original_filename=document.original_filename,
        file_type=document.file_type,
        file_size=document.file_size,
        file_path=document.file_path,
        business_id=document.business_id,
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document


def get_document_by_id(
    db: Session,
    document_id: int,
) -> Optional[Document]:

    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )


def get_documents_by_business(
    db: Session,
    business_id: int,
) -> list[Document]:

    return (
        db.query(Document)
        .filter(Document.business_id == business_id)
        .all()
    )


def update_document(
    db: Session,
    document: Document,
    document_update: DocumentUpdate,
) -> Document:

    update_data = document_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(document, key, value)

    db.commit()
    db.refresh(document)

    return document


def delete_document(
    db: Session,
    document: Document,
) -> None:

    db.delete(document)
    db.commit()
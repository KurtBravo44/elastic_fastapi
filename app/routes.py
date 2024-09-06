from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Document as DocumentModel
from .elastic import search_documents, es

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search")
async def search(query: str):
    """Ищет документы по тексту в индексе Elasticsearch."""
    results = await search_documents(query)
    return results

@router.delete("/documents/{id}")
async def delete_document(id: int, db: Session = Depends(get_db)):
    """Удаляет документ из БД и индекса по ID."""
    document = db.query(DocumentModel).filter(DocumentModel.id == id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")


    await es.delete(index="documents", id=str(id))

    # Удаление из БД
    db.delete(document)
    db.commit()
    return {"detail": "Document deleted"}

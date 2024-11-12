from ..database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/db-test/')
async def test_db_conn(db: Session=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {'msg':'Database Connection Successful'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

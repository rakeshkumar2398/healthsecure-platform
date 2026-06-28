from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.claim_schema import ClaimCreate, ClaimResponse
from app.services.claim_service import create_claim, get_claims

router = APIRouter(prefix="/claims", tags=["Claims"])


@router.post("/", response_model=ClaimResponse)
def submit_claim(claim_data: ClaimCreate, db: Session = Depends(get_db)):
    return create_claim(db, claim_data)


@router.get("/", response_model=List[ClaimResponse])
def list_claims(db: Session = Depends(get_db)):
    return get_claims(db)

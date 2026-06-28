from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.claim_schema import ClaimCreate, ClaimUpdate, ClaimResponse
from app.services.claim_service import (
    create_claim,
    get_claims,
    get_claim_by_id,
    update_claim,
    delete_claim
)

router = APIRouter(prefix="/claims", tags=["Claims"])


@router.post("/", response_model=ClaimResponse)
def submit_claim(claim_data: ClaimCreate, db: Session = Depends(get_db)):
    return create_claim(db, claim_data)


@router.get("/", response_model=List[ClaimResponse])
def list_claims(db: Session = Depends(get_db)):
    return get_claims(db)


@router.get("/{claim_id}", response_model=ClaimResponse)
def get_claim(claim_id: str, db: Session = Depends(get_db)):
    claim = get_claim_by_id(db, claim_id)

    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")

    return claim


@router.put("/{claim_id}", response_model=ClaimResponse)
def modify_claim(claim_id: str, claim_data: ClaimUpdate, db: Session = Depends(get_db)):
    claim = update_claim(db, claim_id, claim_data)

    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")

    return claim


@router.delete("/{claim_id}")
def remove_claim(claim_id: str, db: Session = Depends(get_db)):
    claim = delete_claim(db, claim_id)

    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")

    return {"message": "Claim deleted successfully", "claim_id": claim_id}

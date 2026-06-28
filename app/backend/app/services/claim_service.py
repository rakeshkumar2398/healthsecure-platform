from sqlalchemy.orm import Session
from app.models.claim import Claim
from app.schemas.claim_schema import ClaimCreate, ClaimUpdate


def create_claim(db: Session, claim_data: ClaimCreate):
    claim = Claim(
        patient_name=claim_data.patient_name,
        insurance_provider=claim_data.insurance_provider,
        policy_number=claim_data.policy_number,
        diagnosis=claim_data.diagnosis,
        claim_amount=claim_data.claim_amount,
        status="SUBMITTED",
        fraud_score=0.0
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim


def get_claims(db: Session):
    return db.query(Claim).all()


def get_claim_by_id(db: Session, claim_id: str):
    return db.query(Claim).filter(Claim.id == claim_id).first()


def update_claim(db: Session, claim_id: str, claim_data: ClaimUpdate):
    claim = get_claim_by_id(db, claim_id)

    if not claim:
        return None

    update_data = claim_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(claim, field, value)

    db.commit()
    db.refresh(claim)

    return claim


def delete_claim(db: Session, claim_id: str):
    claim = get_claim_by_id(db, claim_id)

    if not claim:
        return None

    db.delete(claim)
    db.commit()

    return claim

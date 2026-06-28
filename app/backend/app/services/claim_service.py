from sqlalchemy.orm import Session
from app.models.claim import Claim
from app.schemas.claim_schema import ClaimCreate


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

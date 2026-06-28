import uuid
from datetime import datetime

from sqlalchemy import Column, String, Text, Numeric, Float, DateTime
from app.db.database import Base


class Claim(Base):
    __tablename__ = "claims"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    patient_name = Column(String(100), nullable=False)
    insurance_provider = Column(String(100), nullable=False)
    policy_number = Column(String(50), nullable=False)
    diagnosis = Column(Text, nullable=False)
    claim_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), nullable=False, default="SUBMITTED")
    fraud_score = Column(Float, nullable=True, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field


class ClaimCreate(BaseModel):
    patient_name: str = Field(..., min_length=2, max_length=100)
    insurance_provider: str = Field(..., min_length=2, max_length=100)
    policy_number: str = Field(..., min_length=3, max_length=50)
    diagnosis: str = Field(..., min_length=3)
    claim_amount: Decimal = Field(..., gt=0)


class ClaimUpdate(BaseModel):
    patient_name: Optional[str] = Field(None, min_length=2, max_length=100)
    insurance_provider: Optional[str] = Field(None, min_length=2, max_length=100)
    policy_number: Optional[str] = Field(None, min_length=3, max_length=50)
    diagnosis: Optional[str] = Field(None, min_length=3)
    claim_amount: Optional[Decimal] = Field(None, gt=0)
    status: Optional[str] = None


class ClaimResponse(BaseModel):
    id: str
    patient_name: str
    insurance_provider: str
    policy_number: str
    diagnosis: str
    claim_amount: Decimal
    status: str
    fraud_score: Optional[float]

    class Config:
        from_attributes = True

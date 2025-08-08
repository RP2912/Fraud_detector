from pydantic import BaseModel, Field, validator
from typing import List

class TransactionData(BaseModel):
    features: List[float]=Field(..., description="List of features for fraud prediction")

    @validator('features')
    def validate_length(cls, v):
        if len(v) != 4:
            raise ValueError('Features list must contain exactly 4 elements.')
        return v

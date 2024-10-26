from pydantic import BaseModel
from fastapi import FastAPI

class CountryOperator(BaseModel):
    country: str
    operator: str
    high_priority: bool

class SMSMetrics(BaseModel):
    attempts: int
    sent: int
    received: int
    confirmed: int
    success_rate: float
    SMS_success_rate: float
    confirm_rate: Optional[float] = None
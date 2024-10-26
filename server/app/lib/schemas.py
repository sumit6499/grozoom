from pydantic import BaseModel
from fastapi import FastAPI

class CountryOperator(BaseModel):
    country: str
    operator: str
    high_priority: bool

class SMSMetrics(BaseModel):
    country :str
    operator :str
    attempts : int
    sent : int
    received :int 
    confirmed :int
    success_rate :int
    sms_success_rate :int
    confirm_rate :int
from pydantic import BaseModel
from typing import Optional

class CountryOperatorBase(BaseModel):
    country: str
    operator: str
    is_high_priority: bool

class CountryOperatorCreate(CountryOperatorBase):
    pass

class CountryOperatorUpdate(CountryOperatorBase):
    pass

class CountryOperator(CountryOperatorBase):
    id: str

class SMSMetricsBase(BaseModel):
    country: str
    operator: str
    attempts: int
    sent: int
    received: int
    confirmed: int
    success_rate: float
    sms_success_rate: float
    confirm_rate: Optional[float]

class SMSMetricsCreate(SMSMetricsBase):
    pass

class SMSMetricsUpdate(SMSMetricsBase):
    pass

class SMSMetrics(SMSMetricsBase):
    id: int
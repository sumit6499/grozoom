from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SMSMetrics(Base):
    __tablename__ = "sms_metrics"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    operator = Column(String)
    attempts = Column(Integer)
    sent = Column(Integer)
    received = Column(Integer)
    confirmed = Column(Integer)
    success_rate = Column(Float)
    sms_success_rate = Column(Float)
    confirm_rate = Column(Float, nullable=True)
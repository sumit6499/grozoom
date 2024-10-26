from sqlalchemy import  Column, Integer, Float, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
import db

Base = declarative_base()

class SMSMetrics(Base):
    __tablename__ = "sms_metrics"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    operator = Column(String,index=True)
    attempts = Column(Integer)
    sent = Column(Integer)
    received = Column(Integer)
    confirmed = Column(Integer)
    success_rate = Column(Float)
    sms_success_rate = Column(Float)
    confirm_rate = Column(Float, nullable=True)

Base.metadata.create_all(bind=db.engine)

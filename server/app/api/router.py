from fastapi import APIRouter
from app.api.sms import router as sms_router
from app.api.country_operator import router as country_operator_router
from app.api.alerts import router as alerts_router

api_router = APIRouter()
api_router.include_router(sms_router, prefix="/sms", tags=["SMS"])
api_router.include_router(country_operator_router, prefix="/country-operators", tags=["Country-Operators"])
api_router.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
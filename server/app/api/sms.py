from fastapi import APIRouter, Depends, HTTPException
from app.services.sms import get_sms_metrics, create_sms_metrics, update_sms_metrics, delete_sms_metrics
from app.models.schemas import SMSMetricsCreate, SMSMetricsUpdate,SMSMetrics
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=list[SMSMetrics])
async def get_sms_metrics_endpoint(user = Depends(get_current_user)):
    try:
        return await get_sms_metrics()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=SMSMetrics)
async def create_sms_metrics_endpoint(
    data: SMSMetricsCreate, user = Depends(get_current_user)
):
    try:
        return await create_sms_metrics(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}", response_model=SMSMetrics)
async def update_sms_metrics_endpoint(
    id: int, data: SMSMetricsUpdate, user = Depends(get_current_user)
):
    try:
        metrics = await update_sms_metrics(id, data)
        if not metrics:
            raise HTTPException(status_code=404, detail="SMS metrics not found")
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}", response_model=SMSMetrics)
async def delete_sms_metrics_endpoint(
    id: int, user = Depends(get_current_user)
):
    try:
        metrics = await delete_sms_metrics(id)
        if not metrics:
            raise HTTPException(status_code=404, detail="SMS metrics not found")
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

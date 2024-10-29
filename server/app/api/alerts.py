from fastapi import APIRouter, Depends, HTTPException
from app.services.alerts import send_telegram_alert
from app.core.security import get_current_user

router = APIRouter()

@router.post("/send")
async def send_alert(
    alert_type: str, message: str, user = Depends(get_current_user)
):
    try:
        await send_telegram_alert(alert_type, message)
        return {"message": "Alert sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

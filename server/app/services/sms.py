from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.database.sql_config import get_mysql_session
from app.models.models import SMSMetrics
from app.models.schemas import SMSMetricsCreate, SMSMetricsUpdate

async def get_sms_metrics():
    session = get_mysql_session()
    result = await session.execute(select(SMSMetrics))
    return result.scalars().all()

async def create_sms_metrics(data: SMSMetricsCreate):
    session = get_mysql_session()
    metrics = SMSMetrics(**data.dict())
    session.add(metrics)
    await session.commit()
    await session.refresh(metrics)
    return metrics

async def update_sms_metrics(id: int, data: SMSMetricsUpdate):
    session = get_mysql_session()
    metrics = await session.get(SMSMetrics, id)
    if metrics:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(metrics, key, value)
        await session.commit()
        await session.refresh(metrics)
        return metrics
    return None

async def delete_sms_metrics(id: int):
    session = get_mysql_session()
    metrics = await session.get(SMSMetrics, id)
    if metrics:
        await session.delete(metrics)
        await session.commit()
        return metrics
    return None
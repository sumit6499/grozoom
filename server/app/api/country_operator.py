from fastapi import APIRouter, Depends, HTTPException
from app.services.country_operator import (
    get_country_operators,
    create_country_operator,
    update_country_operator,
    delete_country_operator
)
from app.models.schemas import CountryOperatorCreate, CountryOperatorUpdate,CountryOperator
from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=list[CountryOperator])
async def get_country_operators_endpoint(user = Depends(get_current_user)):
    try:
        return await get_country_operators()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=CountryOperator)
async def create_country_operator_endpoint(
    data: CountryOperatorCreate, user = Depends(get_current_user)
):
    try:
        return await create_country_operator(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}", response_model=CountryOperator)
async def update_country_operator_endpoint(
    id: str, data: CountryOperatorUpdate, user = Depends(get_current_user)
):
    try:
        country_operator = await update_country_operator(id, data)
        if not country_operator:
            raise HTTPException(status_code=404, detail="Country-operator not found")
        return country_operator
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}", response_model=CountryOperator)
async def delete_country_operator_endpoint(
    id: str, user = Depends(get_current_user)
):
    try:
        country_operator = await delete_country_operator(id)
        if not country_operator:
            raise HTTPException(status_code=404, detail="Country-operator not found")
        return country_operator
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from app.database.mongo_config import get_country_operators_collection
from app.models.schemas import CountryOperatorCreate, CountryOperatorUpdate, CountryOperator

async def get_country_operators():
    collection = get_country_operators_collection()
    country_operators = [CountryOperator(**doc) for doc in collection.find({})]
    return country_operators

async def create_country_operator(data: CountryOperatorCreate):
    collection = get_country_operators_collection()
    result = collection.insert_one(data.dict())
    return CountryOperator(id=str(result.inserted_id), **data.dict())

async def update_country_operator(id: str, data: CountryOperatorUpdate):
    collection = get_country_operators_collection()
    result = collection.update_one({"_id": id}, {"$set": data.dict()})
    if result.modified_count > 0:
        return CountryOperator(id=id, **data.dict())
    return None

async def delete_country_operator(id: str):
    collection = get_country_operators_collection()
    result = collection.delete_one({"_id": id})
    if result.deleted_count > 0:
        return CountryOperator(id=id)
    return None
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router
from app.database.mongo_config import connect_to_mongodb, close_mongodb_connection
from app.database.sql_config import connect_to_mysql, close_mysql_connection
from app.services.alerts import initialize_telegram_bot

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    connect_to_mongodb()
    connect_to_mysql()
    # initialize_telegram_bot()

@app.on_event("shutdown")
async def shutdown_event():
    close_mongodb_connection()
    close_mysql_connection()

@app.get('/')
async def get_root()->dict:
    return {"message":"Hello from SMS metrics backend"}

@app.get("/health-check")
def check_health()->dict:
    return {"success":True,"message":"Health check complete"}

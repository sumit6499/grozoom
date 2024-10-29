from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str =""
    MONGODB_DB: str =""
    MYSQL_HOST: str  = ""
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_DB: str = ""
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_CHAT_ID: str = ""
    JWT_SECRET_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
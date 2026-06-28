from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "healthsecure"
    database_user: str = "postgres"
    database_password: str = "postgres"

    redis_host: str = "localhost"
    redis_port: int = 6379

settings = Settings()

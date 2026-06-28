from fastapi import FastAPI
from app.core.config import settings
import psycopg2
import redis

app = FastAPI(title="HealthSecure Claims API")

@app.get("/health")
def health_check():
    health = {
        "api": "UP",
        "database": "DOWN",
        "redis": "DOWN"
    }

    try:
        conn = psycopg2.connect(
            host=settings.database_host,
            port=settings.database_port,
            dbname=settings.database_name,
            user=settings.database_user,
            password=settings.database_password
        )
        conn.close()
        health["database"] = "UP"
    except Exception as e:
        health["database_error"] = str(e)

    try:
        r = redis.Redis(host=settings.redis_host, port=settings.redis_port)
        r.ping()
        health["redis"] = "UP"
    except Exception as e:
        health["redis_error"] = str(e)

    return health

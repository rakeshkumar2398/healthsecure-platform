from fastapi import FastAPI

app = FastAPI(title="HealthSecure Claims API")

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "healthsecure-claims-api"
    }

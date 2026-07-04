from fastapi import FastAPI

from backend.app.api.collector import router as collector_router
from backend.app.logging.logger import logger
from backend.app.database.init_db import init_db
from backend.app.api.jobs import router as jobs_router

app = FastAPI(
    title="CareerOS API",
    version="1.0.0"
)

app.include_router(jobs_router)
app.include_router(collector_router)


@app.on_event("startup")
def startup():

    logger.info("CareerOS Backend Started")

    init_db()

    logger.info("Database Initialized Successfully")


@app.get("/")
def home():

    logger.info("Home endpoint called")

    return {
        "message": "Welcome to CareerOS API 🚀"
    }


@app.get("/health")
def health():

    logger.info("Health endpoint checked")

    return {
        "status": "healthy"
    }
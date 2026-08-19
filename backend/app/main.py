from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import roadmap, topics, phases, weeks
from . import models
from .database import database_engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"],

)
models.db_base.metadata.create_all(bind = database_engine)
app.include_router(roadmap.router)
app.include_router(phases.router)
app.include_router(weeks.router)
app.include_router(topics.router)

@app.get("/health")
def health_check():
    return {"status" : "ok"}
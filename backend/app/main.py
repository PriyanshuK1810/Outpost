from fastapi import FastAPI
from .routers import roadmap, topics, phases, weeks
from . import models
from .database import database_engine

app = FastAPI()
models.db_base.metadata.create_all(bind = database_engine)
app.include_router(roadmap.router)
app.include_router(phases.router)
app.include_router(weeks.router)
app.include_router(topics.router)

@app.get("/health")
def health_check():
    return {"status" : "ok"}
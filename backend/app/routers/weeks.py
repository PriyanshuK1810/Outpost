from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix = "/weeks", tags = ["Weeks"])
@router.post("/{week_id}/topics", response_model = schemas.TopicRead)
def create_topics(week_id : int, payload : schemas.TopicCreate, db : Session = Depends(get_db)):
    topic = models.Topic(week_id = week_id, **payload.model_dump())
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic
@router.delete("/{week_id}", status_code = 204)
def delete_week(week_id : int, db : Session = Depends(get_db)):
    week = db.query(models.Week).filter(models.Week.id == week_id).first()
    if week is None:
        raise HTTPException(status_code = 404, detail = "Week Not Found")
    db.delete(week)
    db.commit()
    
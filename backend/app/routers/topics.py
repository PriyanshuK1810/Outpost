from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix = "/topics", tags = ["Topics"])
@router.patch("/{topic_id}", response_model = schemas.TopicRead)
def update_topic(topic_id : int, payload : schemas.TopicUpdate, db : Session = Depends(get_db)):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code = 404, detail = "Topic Not Found")
    updates = payload.model_dump(exclude_unset = True)
    for field, value in updates.items():
        setattr(topic, field, value)
    db.commit()
    db.refresh(topic)
    return topic
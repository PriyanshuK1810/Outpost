from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix = "/phases", tags = ["Phases"])
@router.post("/{phase_id}/weeks", response_model = schemas.WeekRead)
def create_weeks(phase_id : int, payload : schemas.WeekCreate, db : Session = Depends(get_db)):
    week = models.Week(phase_id = phase_id, **payload.model_dump())
    db.add(week)
    db.commit()
    db.refresh(week)
    return week
@router.delete("/{phase_id}", status_code = 204)
def delete_phase(phase_id : int, db : Session = Depends(get_db)):
    phase = db.query(models.Phase).filter(models.Phase.id == phase_id).first()
    if phase is None:
        raise HTTPException(status_code = 404, detail = "Phase Not Found")
    db.delete(phase)
    db.commit()

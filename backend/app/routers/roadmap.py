from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
router = APIRouter(prefix = "/roadmaps", tags = ["Roadmaps"])
@router.post("", response_model = schemas.RoadmapRead)
def create_roadmap(payload : schemas.RoadmapCreate, db : Session = Depends(get_db)):
    roadmap = models.Roadmap(title = payload.title)
    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)
    return roadmap
@router.get("/{roadmap_id}", response_model = schemas.RoadmapRead)
def get_roadmap(roadmap_id : int, db : Session = Depends(get_db)):
    roadmap = db.query(models.Roadmap).filter(models.Roadmap.id == roadmap_id).first()
    if roadmap is None:
        raise HTTPException(status_code = 404, detail = "Roadmap Not Found")
    return roadmap
@router.post("/{roadmap_id}/phases", response_model = schemas.PhaseRead)
def create_phase(roadmap_id : int, payload : schemas.PhaseCreate, db : Session = Depends(get_db)):
    phase = models.Phase(roadmap_id = roadmap_id, **payload.model_dump())
    db.add(phase)
    db.commit()
    db.refresh(phase)
    return phase
@router.delete("/{roadmap_id}", status_code = 204)
def delete_roadmap(roadmap_id : int, db : Session = Depends(get_db)):
    roadmap = db.query(models.Roadmap).filter(models.Roadmap.id == roadmap_id).first()
    if roadmap is None:
        raise HTTPException(status_code = 404, detail = "Roadmap Not Found")
    db.delete(roadmap)
    db.commit()
    



from pydantic import BaseModel, ConfigDict
from .models import topic_status

# Topic Schemas

class TopicBase(BaseModel):
    title : str
    order_index : int
    description : str | None = None
    status : topic_status = topic_status.not_started

class TopicCreate(TopicBase):
    pass

class TopicUpdate(BaseModel):
    title : str | None = None
    order_index : int | None = None
    description : str | None = None
    status : topic_status | None = None

class TopicRead(TopicBase):
    id : int
    week_id : int
    model_config = ConfigDict(from_attributes = True)
# Week Schemas

class WeekBase(BaseModel):
    title : str
    order_index : int

class WeekCreate(WeekBase):
    pass

class WeekUpdate(BaseModel):
    title : str | None = None
    order_index : int | None = None

class WeekRead(WeekBase):
    id : int
    topics : list[TopicRead] = []
    model_config = ConfigDict(from_attributes = True)

# Phase Schemas

class PhaseBase(BaseModel):
    title : str
    order_index : int
    checkpoint_text : str | None = None

class PhaseCreate(PhaseBase):
    pass

class PhaseUpdate(BaseModel):
    title : str | None = None
    order_index : int | None = None
    checkpoint_text : str | None = None

class PhaseRead(PhaseBase):
    id : int
    weeks : list[WeekRead] = [] 
    model_config = ConfigDict(from_attributes = True)

# RoadMap Schemas

class RoadmapBase(BaseModel):
    title : str

class RoadmapCreate(RoadmapBase):
    pass

class RoadmapUpdate(BaseModel):
    title : str | None = None

class RoadmapRead(RoadmapBase):
    id : int
    phases : list[PhaseRead] = []
    model_config = ConfigDict(from_attributes = True)


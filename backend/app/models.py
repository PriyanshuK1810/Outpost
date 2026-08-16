from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from .database import db_base

class topic_status(str, enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed = "completed"

class Roadmap(db_base):
    __tablename__ = "roadmap"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    user_id = Column(String, default = "1")
    phases = relationship("Phase", back_populates = "roadmap")

class Phase(db_base):
    __tablename__ = "phases"
    id = Column(Integer, primary_key = True, index = True)
    roadmap_id = Column(Integer, ForeignKey("roadmap.id"))
    title = Column(String, nullable = False)
    order_index = Column(Integer)
    checkpoint_text = Column(String, nullable = True)
    weeks = relationship("Week", back_populates = "phase")
    roadmap = relationship("Roadmap", back_populates = "phases")

class Week(db_base):
    __tablename__ = "weeks"
    id = Column(Integer, primary_key = True, index = True)
    phase_id = Column(Integer, ForeignKey("phases.id"))
    title = Column(String, nullable = False)
    order_index = Column(Integer)
    topics = relationship("Topic", back_populates = "week")
    phase = relationship("Phase", back_populates = "weeks")

class Topic(db_base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key = True, index = True)
    week_id = Column(Integer, ForeignKey("weeks.id"))
    title = Column(String, nullable = False)
    description = Column(String, nullable = True)
    status = Column(Enum(topic_status), nullable = False, default = topic_status.not_started)
    order_index = Column(Integer)
    week = relationship("Week", back_populates = "topics") 



from datetime import datetime
import email
import enum
from click import echo
from sqlalchemy import ForeignKey, select
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship, aliased
from sqlalchemy_utils import URLType
from sqlalchemy.orm import declarative_mixin
from traitlets import default

from database_setup import Base

@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Role(enum.Enum):
    developer =1
    researcher =2

class User(Timestamp, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    fullname = Column(String(100))
    nickname = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    role = Column(Enum(Role))
    
    usersimulation = relationship("Simulation", back_populates='simulationuser')

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

class Model(Timestamp, Base):
    __tablename__= "models"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    memorycost = Column(Integer)
    performancecost = Column(Float)

    modelsimulation = relationship("Simulation", back_populates='simulationmodel')

class Simulation(Timestamp, Base):
    __tablename__= "simulations"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    userid = Column(Integer, ForeignKey("users.id"), nullable=False)
    modelid = Column(Integer, ForeignKey("models.id"), nullable=False)
    starttime = DateTime()
    endtime = DateTime()
    url = Column(URLType, nullable=True)

    simulationuser = relationship("User", back_populates='usersimulation')
    simulationmodel = relationship("Model", back_populates='modelsimulation')
from sqlalchemy import Bo, Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class EventLog(Base):

    __tablename__ = "eventlog"
    timestamp = Column(String, primary_key=True)
    monitorName = Column(String)
    healthStatus = Column(Integer)

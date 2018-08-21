"""This file define all the model we will need in CI"""

import logging
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
    Boolean,
    UniqueConstraint,
)

from sqlalchemy_utils import EmailType

from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from config import engine


LOG = logging.getLogger(__name__)
Metadata = MetaData(bind=engine)
MetaBase = declarative_base(metadata=Metadata)


class Writers(MetaBase):
    __tablename__ = 'writers'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    email = Column(EmailType, nullable=False)
    workedProjects = Column(Integer, nullable=True)

    def __init__(self, name, email, workedProjects=0):
        self.name = name
        self.email = email
        self.workedProjects = workedProjects


class Projects(MetaBase):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    # the project shoudn't been upload to nowhere
    uploadPath = Column(String(256), nullable=False)
    keyWords = Column(Text, nullable=True)
    writer = Column(String(32), nullable=True)
    updatedTime = Column(DateTime, nullable=True)
    description = Column(Text, nullable=True)
    taken = Column(Boolean, nullable=True)

    def __init__(self, name, uploadPath, keyWords=None, description=None, writer=None, updatedTime=None, taken=None):
        self.name = name
        self.keyWords = keyWords
        self.writer = writer
        self.updatedTime = updatedTime
        self.uploadPath = uploadPath
        self.description = description
        self.taken = taken

if __name__ == "__main__":
    # create all table and column, so we must call this before
    # all things begin.
    Metadata.create_all(bind=engine, checkfirst=True)

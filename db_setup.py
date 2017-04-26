import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Band(Base):
	__tablename__ = 'bands'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class Album(Base):
	__tablename__ = 'albums'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	band_id = Column(Integer, ForeignKey('bands.id'))
	band = relationship(Band)

class Song(Base):
	__tablename__ = 'songs'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	length = Column(String(8), nullable=False)
	isHit = Column(Boolean, default=False)
	band_id = Column(Integer, ForeignKey('bands.id'))
	band = relationship(Band)
	album_id = Column(Integer, ForeignKey('albums.id'))
	album = relationship(Album)

engine = create_engine('sqlite:///catalogs.db')

Base.metadata.create_all(engine)
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Band(Base):
	__tabelname__ = 'bands'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

class Album(Base):
	__tabelname__ = 'ablums'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	band_id = Column(Integer, ForeignKey('band.id'))
	band = relationship(Band)

class Song(Base):
	__tabelname__ = 'songs'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	length = Column(String(8), nullable=False)
	isHit = Column(Boolean, default=False)
	band_id = Column(Integer, ForeignKey('band.id'))
	band = relationship(Band)
	album_id = Column(Integer, ForeignKey('album.id'))

engine = create_engine('sqlite:///catalogs.db')

Base.metadata.create_all(engine)
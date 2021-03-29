#! python

import sqlite3
from sqlalchemy import create_engine, select, insert, Table, Column, Integer, String, Float, Numeric, Boolean
from sqlalchemy.orm import declarative_base

import sys

engine = create_engine('sqlite+pysqlite:///data.sqlite')
conn = engine.connect()

Base = declarative_base()

class AccessToken(Base):
    __tablename__ = 'access_tokens'

    id = Column(Integer, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)
    expiry = Column(Integer)

    def __repr__(self):
        return(f"AccessToken(access_token={self.access_token}, refresh_token={self.refresh_token}, expiry={self.expiry}")

class Type(Base):
    __tablename__ = 'invTypes'

    type_id = Column('typeID', Integer, nullable=False, primary_key=True)
    group_id = Column('groupID', Integer)
    type_name = Column('typeName', String)
    description = Column('description', String)
    mass = Column('mass', Float)
    volume = Column('volume', Float)
    capacity = Column('capacity', Float)
    portion_size = Column('portionSize', Integer)
    race_id = Column('raceID', Integer)
    base_price = Column('basePrice', Numeric(19, 4))
    published = Column('published', Boolean)
    market_group_id = Column('marketGroupID', Integer)
    icon_id = Column('iconID', Integer)
    sound_id = Column('soundID', Integer)
    graphic_id = Column('graphicID', Integer)

    def __repr__(self):
        return(f"Type(type_id={self.type_id}, type_name={self.type_name}")


def create_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    if sys.argv[1] == 'create':
        create_database()

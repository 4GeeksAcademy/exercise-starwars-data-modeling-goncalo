import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Association table for the many-to-many relationship between User and Planet
user_planet_association = Table('user_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('planet_id', Integer, ForeignKey('planet.id'))
)

# Association table for the many-to-many relationship between User and Character
user_character_association = Table('user_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

class User(Base):
    __tablename__ = 'user'
    # Here define colums for the table users
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorite_planets = relationship("Planet", secondary=user_planet_association, back_populates="users")
    favorite_characters = relationship("Character", secondary=user_character_association, back_populates="users")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    # Define relationship with User through the association table
    users = relationship("User", secondary=user_planet_association, back_populates="favorite_planets")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    # Define relationship with User through the association table
    users = relationship("User", secondary=user_character_association, back_populates="favorite_characters")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

from __future__ import annotations

import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base, Mapped
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


user_planet_favorite = Table(
    "UserPlanetFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
)


user_starship_favorite = Table(
    "UserStarshipFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("starship_id", ForeignKey("Starship.id"), primary_key=True),
)

user_character_favorite = Table(
    "UserCharacterFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("character_id", ForeignKey("Character.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    favorites: Mapped[List[Planet]] = relationship("Planet", secondary=user_planet_favorite)
    starship_favorites: Mapped[List[Starship]] = relationship("Starship", secondary=user_starship_favorite)
    character_favorites: Mapped[List[Character]] = relationship("Character", secondary=user_character_favorite)

class Planet(Base):
    __tablename__ = "Planet"

    id = Column(Integer, primary_key=True)
    population = Column(Integer,nullable=False)
    climate = Column(String, nullable=False)
    surface_water_percentage = Column(String, nullable=False)
    radius = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    favorites: Mapped[List[User]] = relationship("User", secondary=user_planet_favorite)

class Starship(Base):
    __tablename__ = "Starship"

    id = Column(Integer, primary_key=True)
    Class = Column(String ,nullable=False)
    Crew_Members= Column(String ,nullable=False)
    Passengers=Column(String ,nullable=False)
    Length=Column(Integer ,nullable=False)
    starship_favorites: Mapped[List[User]] = relationship("User", secondary=user_starship_favorite)

class Character(Base):
    __tablename__ = "Character"

    id = Column(Integer, primary_key=True)
    Height = Column(Integer ,nullable=False)
    Mass= Column(Integer ,nullable=False)
    Hair_Color=Column(String ,nullable=False)
    Skin_Color=Column(String ,nullable=False)
    character_favorites: Mapped[List[User]] = relationship("User", secondary=user_character_favorite)
    



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

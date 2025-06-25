# Object–relational mapping (ORM, O/RM, and O/R mapping tool)
# obsługujemy obiekty kals jako modele odwzorowujące Tabele w bazie danych - encje
# sqlalchemy

import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

DATABSE_URL = "sqlite:///moja_baza.db"

engine = create_engine(DATABSE_URL, echo=True)  # właczamy logowanie komend sql

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    # relacja jeden do wielu
    posts = relationship('Post', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates='posts')


Base.metadata.create_all(engine)

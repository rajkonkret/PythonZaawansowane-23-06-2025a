# Object–relational mapping (ORM, O/RM, and O/R mapping tool)
# obsługujemy obiekty kals jako modele odwzorowujące Tabele w bazie danych - encje
# sqlalchemy

import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from krok1_modele import User, Post

DATABSE_URL = "sqlite:///moja_baza.db"

engine = create_engine(DATABSE_URL, echo=True)  # właczamy logowanie komend sql
Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = User(name="Jan Kowalski", email="jan.kowalski@example.com")
    session.add(new_user)

    new_post = Post(title="Pierwszy post", content="To jest treśc pierwszego posta", user=new_user)
    session.add(new_post)

    session.commit()
except Exception as e:
    print(f"Bład: {e}")
    session.rollback()  # wycofanie zmian w przypadku błedu

finally:
    session.close()

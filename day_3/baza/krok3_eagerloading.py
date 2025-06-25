import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

from krok1_modele import User, Post

DATABSE_URL = "sqlite:///moja_baza.db"

engine = create_engine(DATABSE_URL, echo=True)  # właczamy logowanie komend sql
Session = sessionmaker(bind=engine)
session = Session()

# problem n+1
# joinedload - ominiecie problemu n +1
# user_with_posts = session.query(User).all()
user_with_posts = session.query(User).options(joinedload(User.posts)).all()

for user in user_with_posts:
    print(f"Użytkownik: {user.name}")
    for post in user.posts:
        print(f" Post: {post.title}")

session.close()
# Użytkownik: Jan Kowalski
#  Post: Pierwszy post

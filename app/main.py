from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body, Depends
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy import schema
from starlette.status import HTTP_404_NOT_FOUND
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from . import utils
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='odoo14', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("connecting to database fail")
#         time.sleep(3000)


# my_posts = [
#     {
#         "title": "title of post 1",
#         "content": "content of post 1",
#         "id": 1
#     },
#     {
#         "title": "title of post 2",
#         "content": "content of post 2",
#         "id": 2
#     },
#     {
#         "title": "title of post 3",
#         "content": "content of post 3",
#         "id": 3
#     }
# ]


# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post


# def find_post_index(id):
#     for index, post in enumerate(my_posts):
#         if post['id'] == id:
#             return index

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to python api development with FastAPI"}

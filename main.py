from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

from starlette.status import HTTP_404_NOT_FOUND


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "title of post 2",
        "content": "content of post 2",
        "id": 2
    },
    {
        "title": "title of post 3",
        "content": "content of post 3",
        "id": 3
    }
]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post


@app.get("/")
def root():
    return {"message": "Welcome to python api development with FastAPI"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000)
    my_posts.append(post_dict)
    return {"post": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} was not found')
    return {"post_detail": post}

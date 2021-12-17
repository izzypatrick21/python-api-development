from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World, welcome to python api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post('/createposts')
def createposts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"'title': {payload['title']}  'content':{payload['content']} "}

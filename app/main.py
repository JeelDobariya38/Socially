from pydantic import BaseModel
from fastapi import FastAPI

class Post(BaseModel):
    title: str
    content: str

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "my first post",
        "content": "placeholder content....",
    },
    {
        "id": 2,
        "title": "my second post",
        "content": "placeholder demo content....",
    }
]

@app.get("/")
def root():
    return {"name": "simple api", "msg": "hello", "version": "v0.1.0-alpha"}

@app.get("/posts")
def get_posts():
    return {"posts": posts}

@app.get("/posts/{post_id}")
def get_post_with_id(post_id: int):
    for item in posts:
        if item["id"] == post_id:
            return item
    return {"data": f"Post With Id {post_id} Not Found!!"}

@app.post("/posts/")
def create_item(post: Post):
    item = {
        "id": 3,
        "title": post.title,
        "content": post.content,
    }
    posts.append(item)
    return item

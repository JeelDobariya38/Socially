from fastapi import FastAPI

import models

app = FastAPI()

@app.get("/")
def root():
    return {"name": "Socially", "message": "hello, welcome to socially api!!", "version": "v0.1.0"}

@app.get("/posts")
def get_posts():
    post = getposts()
    return {"posts": posts}

@app.get("/posts/{post_id}")
def get_post_with_id(post_id: int):
    for item in posts:
        if item["id"] == post_id:
            return item
    return {"data": f"Post With Id {post_id} Not Found!!"}

@app.post("/posts/")
def create_item(post: models.Post):
    item = {
        "id": 3,
        "title": post.title,
        "content": post.content,
    }
    posts.append(item)
    return item

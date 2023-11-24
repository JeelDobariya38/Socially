from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get("/")
def root():
    return {"name": "simple api", "msg": "hello", "version": "v0.1.0-alpha"}

@app.get("/posts")
def get_posts():
    return {"posts": posts}

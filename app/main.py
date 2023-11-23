from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"name": "simple api", "msg": "hello", "version": "v0.1.0-alpha"}

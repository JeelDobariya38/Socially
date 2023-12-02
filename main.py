import uvicorn

import Database


def run_fastapi():
    uvicorn.run("main:app", app_dir="Api")


if __name__ == "__main__":
    Database.init()
    run_fastapi()

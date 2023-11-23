import subprocess
import os

def run_fastapi():
    # Specify the command to run FastAPI using Uvicorn
    command = "uvicorn main:app"

    # Run the command using subprocess
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Run the FastAPI app in the 'app' directory
    os.chdir('app')
    run_fastapi()

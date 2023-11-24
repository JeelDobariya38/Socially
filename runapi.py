import subprocess

def run_fastapi():
    # Specify the command to run FastAPI using Uvicorn
    command = "uvicorn app.main:app"

    # Run the command using subprocess
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_fastapi()

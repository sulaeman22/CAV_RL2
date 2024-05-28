import os
import subprocess

def run_gradle_task(task_name):
    subprocess.run(['./gradlew', task_name], check=True)

if __name__ == "__main__":
    task_name = "build"
    run_gradle_task(task_name)

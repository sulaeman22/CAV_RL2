import os
import subprocess

def setup_environment():
    os.environ['SUMO_HOME'] = '/path/to/sumo'
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)

if __name__ == "__main__":
    setup_environment()

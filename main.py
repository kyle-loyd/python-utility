from dotenv import load_dotenv
from project_init import ProjectInitializer
from uuid_gen import UuidGenerator
import os

uuid = UuidGenerator()
project_init = ProjectInitializer()

def fetch_env_vars():
    if not load_dotenv():
        print("No environment variables set within \".env\" file")
        exit(1)

if __name__ == "__main__":    
    fetch_env_vars()
    project_init.initialize()
    print(f"Project Initialized Successfully: {project_init.project_dir}")
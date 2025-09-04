import os
from uuid_gen import UuidGenerator

uuid = UuidGenerator()

class ProjectInitializer:
    def __init__(self):
        return

    def initialize(self):
        configured_dev_dir = os.environ.get("DEV_DIR")
        print("Development Directory Configured: ", configured_dev_dir)

        os.chdir(configured_dev_dir)
        dev_dir = os.getcwd()
        print("Changed directory to: ", dev_dir)
        
        dir_uuid = str(uuid.generate())
        self.project_dir = f"python-{dir_uuid}"
        os.system(f"mkdir {self.project_dir}")
        print(f"Created directory: {self.project_dir}")

        os.chdir(self.project_dir)
        print(f"Changed directory to: {self.project_dir}")

        os.system(f"python3 -m venv env")
        print("Created virtual environment: env")
        
        os.system("touch .env")
        print("Created file: .env")

        os.system("git init")
        os.system(f"touch .gitignore")
        print("Created file: .gitignore")

        with open(".gitignore", "a") as gitignore:
            gitignore.write("env/\n")
            gitignore.write(".env\n")
            gitignore.write("__pycache__/\n")
        print("Added \"env\" and \".env\" to .gitignore")
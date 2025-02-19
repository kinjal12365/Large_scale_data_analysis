#!/usr/bin/env python3
import os
from pathlib import Path

def create_empty_file(file_path: Path):
    """
    Creates an empty file at file_path if it doesn't exist.
    """
    if not file_path.exists():
        file_path.touch()
        print(f"Created: {file_path}")
    else:
        print(f"File already exists: {file_path}")

def main():
    # Set the project root as the current working directory
    project_root = Path.cwd()

    # Define the files to be created in the project root
    files = ["README.md", "requirements.txt", ".gitignore", "main_analytics.ipynb"]
    
    for file_name in files:
        create_empty_file(project_root / file_name)

    # Create the experimentation directory
    experimentation_dir = project_root / "experimentation"
    experimentation_dir.mkdir(exist_ok=True)
    print(f"Ensured directory exists: {experimentation_dir}")

    # Create the notebook file in the experimentation directory
    create_empty_file(experimentation_dir / "data_analytics_exp.ipynb")

if __name__ == "__main__":
    main()

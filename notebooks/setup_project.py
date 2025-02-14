import os
import sys
from pathlib import Path
import shutil

def create_project_structure(base_path: str = "tender-ai"):
    """
    Creates the project directory structure and initial files.
    
    Args:
        base_path (str): The base path where the project will be created
    """
    # Create base directory
    base_dir = Path(base_path)
    
    # Define the directory structure
    directories = [
        "src",
        "src/config",
        "src/agents",
        "src/tools",
        "src/rag",
        "src/database",
        "src/utils",
        "data",
        "data/raw",
        "data/processed",
        "data/embeddings",
        "tests",
        "tests/test_agents",
        "tests/test_rag",
        "tests/test_tools"
    ]
    
    # Create directories
    for dir_path in directories:
        (base_dir / dir_path).mkdir(parents=True, exist_ok=True)
        # Add __init__.py to Python packages
        if dir_path.startswith(("src", "tests")):
            (base_dir / dir_path / "__init__.py").touch()

    # Create .env file with template
    env_content = """# OpenAI API Key
OPENAI_API_KEY=your_api_key_here

# ChromaDB Settings
CHROMA_DB_PATH=data/embeddings/chroma

# Project Settings
MODEL_NAME=gpt-4-turbo-preview
EMBEDDING_MODEL=text-embedding-3-small
"""
    
    with open(base_dir / ".env", "w", encoding="utf-8") as f:
        f.write(env_content)

    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# Environment Variables
.env

# IDE
.idea/
.vscode/
*.swp
*.swo

# Project Specific
data/raw/*
data/processed/*
data/embeddings/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/embeddings/.gitkeep

# OS
.DS_Store
Thumbs.db
"""
    
    with open(base_dir / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)

    # Create README.md
    readme_content = """# Tender AI Assistant

An AI-powered system for automating and optimizing the tender/bidding process for architectural firms.

## Project Structure

- `src/`: Source code
  - `agents/`: CrewAI agents for different tasks
  - `rag/`: Retrieval-Augmented Generation system
  - `tools/`: Custom tools for agents
  - `database/`: Database interactions
  - `utils/`: Utility functions
- `data/`: Data storage
  - `raw/`: Original tender documents
  - `processed/`: Processed documents
  - `embeddings/`: Vector embeddings

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your API keys

## Usage

[Usage instructions will be added as the project develops]
"""
    
    with open(base_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Create requirements.txt
    requirements_content = """# Core dependencies
crewai>=0.76
langchain>=0.3.7
chromadb>=0.4.24
openai>=1.54.0
python-dotenv>=1.0.0

# Document processing
pypdf>=5.0.0
python-docx>=0.8.11
beautifulsoup4>=4.12.0

# Data manipulation
pandas>=2.0.0
numpy>=1.24.0

# Testing
pytest>=8.0.0
"""
    
    with open(base_dir / "requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements_content)

    # Create initial config file
    config_content = """from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"

# Model settings
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4-turbo-preview")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ChromaDB settings
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", str(EMBEDDINGS_DIR / "chroma"))

# Create directories if they don't exist
for dir_path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, EMBEDDINGS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)
"""
    
    with open(base_dir / "src" / "config" / "settings.py", "w", encoding="utf-8") as f:
        f.write(config_content)

    # Create .gitkeep files in empty directories
    for dir_path in ["data/raw", "data/processed", "data/embeddings"]:
        (base_dir / dir_path / ".gitkeep").touch()

    print(f"Project structure created successfully in {base_path}")
    print("\nNext steps:")
    print("1. Create and activate a virtual environment")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Update the .env file with your API keys")

if __name__ == "__main__":
    create_project_structure()
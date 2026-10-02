from pathlib import Path


PROJECT_ROOT = Path.cwd().resolve()

#  calling paths inside notebooks dir, go one level up
if PROJECT_ROOT.name == 'notebooks':
    PROJECT_ROOT = PROJECT_ROOT.parent

# data paths
RAW_DATA_PATH = PROJECT_ROOT / "data/raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data/processed"
ANALYTICAL_DATA_PATH = PROJECT_ROOT / "data/analytical"

print(PROJECT_ROOT, RAW_DATA_PATH,PROCESSED_DATA_PATH )
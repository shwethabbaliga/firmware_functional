import pytest 
import logging
from pathlib import Path 
import os

ROOT_FOLDER = Path(__file__).parent
NEW_FW = ROOT_FOLDER / "new_firmware"
LOGS = ROOT_FOLDER / "logs"

@pytest.fixture(scope="session",autouse=True)
def project_setting():  
    for folder in ["NEW_FW","LOGS"]:
        folder.mkdir(parent=True,exist_ok=True)

os.listdir()

release = os.environ.get("TPP_RELEASE")








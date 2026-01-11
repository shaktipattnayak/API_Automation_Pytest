import pytest
import requests
import yaml
import sys
from pathlib import Path

# Ensure top-level 'utils' package (api_tests/utils) is importable during tests
ROOT_DIR = Path(__file__).resolve().parents[1]  # points to api_tests
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def api_session(config):
    session = requests.session()
    session.headers.update({"Content-Type": "application/json"})
    session.base_url = config['base_url']
    return session


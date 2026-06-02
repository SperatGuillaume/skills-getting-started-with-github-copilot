import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app

# Snapshot of the original activities data taken once at import time
_ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dict to its original state before each test."""
    app_module.activities = copy.deepcopy(_ORIGINAL_ACTIVITIES)
    yield
    app_module.activities = copy.deepcopy(_ORIGINAL_ACTIVITIES)


@pytest.fixture
def client():
    return TestClient(app)

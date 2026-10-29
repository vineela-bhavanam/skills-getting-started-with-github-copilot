from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a fresh TestClient and reset the in-memory activities store between tests."""
    original_activities = deepcopy(activities)
    test_client = TestClient(app)

    try:
        yield test_client
    finally:
        activities.clear()
        activities.update(original_activities)

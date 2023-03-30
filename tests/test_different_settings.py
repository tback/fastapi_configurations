from fastapi.testclient import TestClient
import pytest
from configurations.config import Settings
from configurations.deps import get_settings
from configurations.main import app


def generate_parameter_dependant_on_scenario(scenarios):
    for scenario in scenarios:
        client = TestClient(app)
        app.dependency_overrides[get_settings] = lambda: settings
        settings = Settings(a=scenario)
        for position, letter in enumerate(scenario, 1):
            yield position, letter.upper(), client


@pytest.mark.parametrize(
    "position, expected_letter,client",
    generate_parameter_dependant_on_scenario(["default", "special"]),
)
def test_different_settings(position, expected_letter, client):
    response = client.get("/")
    assert 200 == response.status_code
    assert response.content.decode()[position] == expected_letter

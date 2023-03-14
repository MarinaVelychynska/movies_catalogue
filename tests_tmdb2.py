from main import app
from unittest.mock import Mock
import pytest


@pytest.mark.parametrize("list_type, expected_response", [
    ("popular", {'results': []}),
    ("top_rated", {'results': []}),
    ("upcoming", {'results': []}),
])

def test_list_types(monkeypatch, list_type, expected_response):
    api_mock = Mock(return_value=expected_response)
    monkeypatch.setattr("tmdb_client.get_popular_movies", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)
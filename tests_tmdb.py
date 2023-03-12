from unittest.mock import Mock

import tmdb_client


class TestTMDBClient:

    def test_get_single_movie(self, monkeypatch):
        movie_id = "12345"
        mock_single_movie = {"id": movie_id}
        requests_mock = Mock()
        requests_mock.return_value.json.return_value = mock_single_movie
        monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
        movie = tmdb_client.get_single_movie(movie_id)
        assert movie == mock_single_movie

    
    def test_get_single_movie_cast(self, monkeypatch):
        movie_id = "12345"
        mock_single_movie_cast = [{"id": 1, "name": "Actor 1"}, {"id": 2, "name": "Actor 2"}]
        requests_mock = Mock()
        requests_mock.return_value.json.return_value = {"cast": mock_single_movie_cast}
        monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
        movie = tmdb_client.get_single_movie_cast(movie_id)
        assert movie == mock_single_movie_cast


    def test_get_movie_images(self, monkeypatch):
        movie_id = "12345"
        mock_movie_images = {"id": movie_id, "backdrops": [], "posters": []}
        requests_mock = Mock()
        requests_mock.return_value.json.return_value = mock_movie_images
        monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
        movie = tmdb_client.get_single_movie_images(movie_id)
        assert movie == mock_movie_images


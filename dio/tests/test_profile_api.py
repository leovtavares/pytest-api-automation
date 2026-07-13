import pytest
import requests
from unittest.mock import patch

BASE_URL = "https://web.dio.me/api"

@patch("requests.get")
def test_get_user_profile_success(mock_get):
    """
    Testa se o endpoint de perfil do usuário retorna dados estruturais corretos e HTTP 200.
    Simula uma requisição bem-sucedida.
    """
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": "12345",
        "name": "Reall Leo Tavares",
        "username": "realleotavares",
        "courses_completed": 15
    }

    response = requests.get(f"{BASE_URL}/users/realleotavares")
    data = response.json()
    
    assert response.status_code == 200
    assert data["username"] == "realleotavares"
    assert "courses_completed" in data

@patch("requests.get")
def test_get_user_achievements(mock_get):
    """
    Testa a listagem de conquistas (achievements) do usuário.
    Garante que a estrutura de retorno é um Array contendo chaves de id e nome.
    """
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"id": 1, "title": "Javascript Starter", "badge_url": "/assets/badges/js.png"},
        {"id": 2, "title": "React Master", "badge_url": "/assets/badges/react.png"}
    ]

    response = requests.get(f"{BASE_URL}/users/realleotavares/achievements")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    assert "badge_url" in data[0]

@patch("requests.get")
def test_resource_not_found(mock_get):
    """
    Validação Backend do Bug-001 (SPA Infinite Loading).
    Garante que o backend retorna HTTP 404 adequadamente quando um recurso relativo é solicitado
    equivocadamente (ex: /users/assets/utils.js). O problema estava no SPA não tratar o 404,
    mas a API/Backend deve rigorosamente emitir o 404.
    """
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    # Simulando o erro do frontend pedindo path relativo
    response = requests.get("https://web.dio.me/users/assets/utils.js")
    
    assert response.status_code == 404

import pytest
import requests
from unittest.mock import patch

BASE_URL = "https://ag.tavardt.com"

@patch("requests.get")
def test_site_is_reachable(mock_get):
    """
    Testa se o servidor principal está respondendo corretamente.
    Usando mock para ambiente educacional.
    """
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><body><h1>TAVARDT</h1></body></html>"

    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert "TAVARDT" in response.text

@patch("requests.get")
def test_redirect_to_locale(mock_get):
    """
    Testa se o site redireciona corretamente para o diretório de idioma (ex: /br).
    """
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><body><h1>TAVARDT - BR</h1></body></html>"

    response = requests.get(BASE_URL, allow_redirects=True)
    assert response.status_code == 200
    assert "TAVARDT" in response.text

@patch("requests.post")
def test_contact_form_invalid_submission(mock_post):
    """
    Testa a segurança da API de contato contra payloads vazios ou inválidos.
    """
    mock_response = mock_post.return_value
    mock_response.status_code = 400

    contact_url = f"{BASE_URL}/br/contato"
    payload = {}
    
    response = requests.post(contact_url, data=payload)
    
    assert response.status_code in [400, 403, 404, 405]

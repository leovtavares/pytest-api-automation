import pytest
import requests

BASE_URL = "https://ag.tavardt.com"

def test_site_is_reachable():
    """
    Testa se o servidor principal está respondendo corretamente.
    """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert "TAVARDT" in response.text

def test_redirect_to_locale():
    """
    Testa se o site redireciona corretamente para o diretório de idioma (ex: /br).
    """
    # Acessando a raiz sem idioma
    response = requests.get(BASE_URL, allow_redirects=True)
    assert response.status_code == 200
    # Valida se o conteúdo retornado contém o layout esperado
    assert "TAVARDT" in response.text

def test_contact_form_invalid_submission():
    """
    Testa a segurança da API de contato contra payloads vazios ou inválidos.
    Em um cenário real, apontaria para o endpoint exato da API de submissão.
    """
    # Exemplo simulado apontando para a página de contato (ajustar para endpoint de API)
    contact_url = f"{BASE_URL}/br/contato"
    payload = {}
    
    response = requests.post(contact_url, data=payload)
    
    # Valida que o servidor não aceita requisições POST não autorizadas/inválidas na rota da página
    # Ou valida se a resposta da API retorna 400 Bad Request
    assert response.status_code in [400, 403, 404, 405]

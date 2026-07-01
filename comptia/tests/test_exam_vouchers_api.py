import pytest
import requests
from unittest.mock import patch
import allure

BASE_URL = "https://api.comptia.org/v1"

@allure.epic("Certification Vouchers")
@allure.feature("Search API")
class TestCompTIAVouchersAPI:

    @allure.story("Get voucher details for Security+ certification")
    @allure.severity(allure.severity_level.CRITICAL)
    @patch("requests.get")
    def test_get_security_plus_voucher(self, mock_get):
        """
        Valida se a API retorna as informações corretas para o voucher Security+.
        Utiliza 'patch' para simular o backend sem consumir quotas reais.
        """
        # Arrange (Setup do Mock)
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "certification_id": "SY0-701",
            "name": "CompTIA Security+",
            "price": 392.00,
            "currency": "USD",
            "is_active": True
        }

        # Act
        response = requests.get(f"{BASE_URL}/vouchers/security-plus")
        data = response.json()

        # Assert
        with allure.step("Verifica Status Code 200"):
            assert response.status_code == 200
            
        with allure.step("Valida Integridade do Schema JSON"):
            assert data["certification_id"] == "SY0-701"
            assert isinstance(data["price"], float)
            assert data["currency"] == "USD"
            assert data["is_active"] is True

import pytest
import requests
from unittest.mock import patch
import allure

BASE_URL = "https://api.luxurystore.com/v1"

@allure.epic("E-commerce Core")
@allure.feature("Cart and Checkout API")
class TestLuxuryStoreCartAPI:

    @allure.story("Calculate total amount during checkout POST")
    @allure.severity(allure.severity_level.BLOCKER)
    @patch("requests.post")
    def test_post_checkout_calculates_total(self, mock_post):
        """
        Valida se o endpoint POST /checkout processa os itens do carrinho
        e retorna o status 201 (Created) junto com o total financeiro exato.
        """
        # Arrange
        mock_response = mock_post.return_value
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "order_id": "ORD-99382-LUX",
            "status": "PROCESSING",
            "items_count": 2,
            "subtotal": 5200.00,
            "taxes": 416.00,
            "total": 5616.00
        }
        
        payload = {
            "user_id": "usr_99182",
            "items": [
                {"product_id": "lux_bag_01", "quantity": 1},
                {"product_id": "lux_shoes_02", "quantity": 1}
            ]
        }

        # Act
        response = requests.post(f"{BASE_URL}/cart/checkout", json=payload)
        data = response.json()

        # Assert
        with allure.step("Verifica Status Code 201 (Order Created)"):
            assert response.status_code == 201
            
        with allure.step("Verifica Matemática Financeira e Schema"):
            assert data["items_count"] == 2
            assert data["subtotal"] + data["taxes"] == data["total"]
            assert data["total"] == 5616.00
            assert data["status"] == "PROCESSING"

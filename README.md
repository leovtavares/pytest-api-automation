[English](#english) | [Português](#português)

<a id="english"></a>
# Pytest API Automation Portfolio

This repository is dedicated to backend quality assurance and API test automation using **Python** and **Pytest**. It demonstrates my ability to validate data integrity, handle HTTP requests, and implement test assertions directly in code, without relying on graphical interfaces.

## Multi-Client Architecture
The test scripts are organized by client/project folders, demonstrating an enterprise-ready structure for scaling test suites across different environments.

```text
pytest-api-automation/
├── .github/workflows/        # CI Pipeline (GitHub Actions)
├── tavardt/                  # [Client 1]
│   └── tests/
│       └── test_tavardt_api.py # Python/Pytest API Tests
├── client2/                  # [Client 2]
│   └── tests/
```

## Tech Stack
- **Python** (Core Language)
- **Pytest** (Test Framework)
- **Requests** (HTTP Library)

## Running the Tests
```bash
pip install -r requirements.txt
pytest */tests/ -v
```

<br><br>

<a id="português"></a>
# Portfólio de Automação de API com Pytest

Este repositório é dedicado à garantia de qualidade de backend e automação de testes de API utilizando **Python** e **Pytest**. Ele demonstra minha capacidade de validar integridade de dados, manipular requisições HTTP e implementar asserções de teste diretamente via código, sem depender de interfaces gráficas.

## Arquitetura Multi-Cliente
Os scripts de teste são organizados por pastas de clientes/projetos, demonstrando uma estrutura corporativa pronta para escalar suítes de testes em diferentes ambientes.

```text
pytest-api-automation/
├── .github/workflows/        # Pipeline de CI (GitHub Actions)
├── tavardt/                  # [Cliente 1]
│   └── tests/
│       └── test_tavardt_api.py # Testes de API (Python/Pytest)
├── client2/                  # [Cliente 2]
│   └── tests/
```

## Stack Técnica
- **Python** (Linguagem Base)
- **Pytest** (Framework de Testes)
- **Requests** (Biblioteca HTTP)

## Executando os Testes
```bash
pip install -r requirements.txt
pytest */tests/ -v
```

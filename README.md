[🇺🇸 English](#english) | [🇧🇷 Português](#português)

<a id="english"></a>
# Pytest API Automation Portfolio

[![CI/CD Pipeline](https://github.com/realleotavares/pytest-api-automation/actions/workflows/pytest.yml/badge.svg)](https://github.com/realleotavares/pytest-api-automation/actions)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-blue?logo=qameta)](https://realleotavares.github.io/pytest-api-automation/)

Welcome to my backend quality assurance and API test automation portfolio.
This repository demonstrates my ability to validate data integrity, handle HTTP requests, and implement test assertions directly in code, using an enterprise-ready architecture.

## Live Quality Dashboard (Allure Report)

> **[View Live Allure Test Report](https://realleotavares.github.io/pytest-api-automation/)**
> 
> Our CI/CD pipeline automatically publishes the latest Pytest execution report to GitHub Pages using Allure. It includes detailed logs, execution times, and visual graphs of all backend tests.

## Repository Architecture (Multi-Client)

The test scripts are organized by client/project folders, demonstrating a scalable structure for enterprise test suites across different environments.

```text
pytest-api-automation/
├── README.md                   # This document
├── requirements.txt            # Python dependencies (Pytest, Requests, Allure)
├── .github/workflows/          # CI/CD Pipelines (Allure Report Generation & GH Pages Deploy)
│
├── core-api/                   # Core microservices and common utilities
│   └── tests/
│       └── test_auth.py        # Authentication and authorization tests
│
└── tavardt-backend/            # 🌍 API layer for the Tavardt platform
    └── tests/
        ├── test_users_api.py   # CRUD operations and data integrity validations
        └── test_payments.py    # Mocking and integration tests for external gateways
```

## Quick Start (Developer Onboarding)

Want to run these API tests locally? It takes less than a minute.

**Prerequisites:** [Python](https://www.python.org/downloads/) (v3.11+)

```bash
# 1. Clone the repository
git clone https://github.com/realleotavares/pytest-api-automation.git
cd pytest-api-automation

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API Test Suite generating Allure results
pytest */tests/ -v --alluredir=allure-results

# 5. Serve the Allure Report locally (requires allure command-line)
allure serve allure-results
```

## Core Competencies Demonstrated

1. **Backend Validation:** Validating schema types, status codes, and JSON response bodies.
2. **DevOps & CI/CD:** Robust GitHub Actions pipeline generating and publishing rich Allure HTML Reports.
3. **Clean Code:** Use of Pytest fixtures for setup/teardown and DRY code principles.

---
*This portfolio is governed by strict CI/CD and backend engineering standards.*

<br><br><br>

<a id="português"></a>
# Portfólio de Automação de API com Pytest

[![CI/CD Pipeline](https://github.com/realleotavares/pytest-api-automation/actions/workflows/pytest.yml/badge.svg)](https://github.com/realleotavares/pytest-api-automation/actions)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-blue?logo=qameta)](https://realleotavares.github.io/pytest-api-automation/)

Bem-vindo ao meu portfólio de automação de testes de API e garantia de qualidade de backend.
Este repositório demonstra minha capacidade de validar integridade de dados, manipular requisições HTTP e implementar asserções de teste diretamente via código.

## Dashboard de Qualidade (Allure Report)

> **[Acessar Relatório Allure Interativo](https://realleotavares.github.io/pytest-api-automation/)**
> 
> Nossa pipeline CI/CD publica automaticamente o último relatório de execução do Pytest no GitHub Pages usando o Allure Report. Ele inclui logs detalhados de requisição, tempo de resposta e gráficos visuais.

## Arquitetura do Repositório (Multi-Client)

Os scripts de teste são organizados por pastas de clientes/projetos, demonstrando uma estrutura corporativa pronta para escalar suítes de testes em diferentes ambientes de backend.

```text
pytest-api-automation/
├── README.md                   # Este documento
├── requirements.txt            # Dependências Python (Pytest, Requests, Allure)
├── .github/workflows/          # Pipelines CI/CD (Geração de Allure e Deploy no GH Pages)
│
├── core-api/                   # Microsserviços base e utilitários
│   └── tests/
│       └── test_auth.py        # Testes de autenticação, JWT e autorização
│
└── tavardt-backend/            # 🌍 Camada de API para a plataforma Tavardt
    └── tests/
        ├── test_users_api.py   # Operações CRUD e validação de integridade de schema
        └── test_payments.py    # Testes de integração (Mocks) para gateways externos
```

## Quick Start (Onboarding de Desenvolvedores)

Quer rodar estes testes na sua máquina? Leva menos de 1 minuto.

**Pré-requisitos:** [Python](https://www.python.org/downloads/) (v3.11+)

```bash
# 1. Clone o repositório
git clone https://github.com/realleotavares/pytest-api-automation.git
cd pytest-api-automation

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode a suíte de API gerando resultados para o Allure
pytest */tests/ -v --alluredir=allure-results

# 5. Visualize o Relatório Localmente (requer Allure CLI instalado)
allure serve allure-results
```

## Competências Core Demonstradas

1. **Validação de Backend:** Teste rigoroso de schemas, *status codes*, cabeçalhos e *payloads* JSON.
2. **DevOps & CI/CD:** Pipeline automatizada via GitHub Actions com deploy do Allure Report.
3. **Clean Code:** Utilização de *fixtures* do Pytest para setup/teardown eficiente e código DRY (Don't Repeat Yourself).

---
*Este portfólio é governado por rigorosos padrões de CI/CD e engenharia de backend.*

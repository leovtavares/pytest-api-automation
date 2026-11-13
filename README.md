[English](#english) | [Português](#português)

<a id="english"></a>
# Pytest API Automation Portfolio

[![CI/CD Pipeline](https://github.com/leovtavares/pytest-api-automation/actions/workflows/pytest.yml/badge.svg)](https://github.com/leovtavares/pytest-api-automation/actions)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-blue?logo=qameta)](https://leovtavares.github.io/pytest-api-automation/)

Welcome to my backend quality assurance and API test automation portfolio.
This repository demonstrates my ability to validate data integrity, handle HTTP requests, and implement test assertions directly in code, using an enterprise-ready architecture.

## Repository Architecture (Multi-Client)

The test scripts are organized by client/project folders, demonstrating a scalable structure for enterprise test suites across different environments.

```text
📁 pytest-api-automation/
├── 📄 README.md                   # This document
├── 📄 requirements.txt            # Python dependencies (Pytest, Requests, Allure)
├── 📁 .github/workflows/          # CI/CD Pipelines (Allure Report Generation & GH Pages Deploy)
│
├── 📁 luxury-store/               # E-commerce API validations
│   └── 📁 tests/
│       └── 📄 test_cart_api.py    # Math validations and backend logic
│
├── 📁 comptia/                    # Vouchers and pricing validations
│   └── 📁 tests/
│       └── 📄 test_exam_vouchers_api.py # JSON schema and data type checks
│
├── 📁 dio/                        # Educational Platform Backend
│   └── 📁 tests/
│       └── 📄 test_profile_api.py # API schema validation and 404 injection
│
└── 📁 tavardt/                    # API layer for the Tavardt platform
    └── 📁 tests/
        └── 📄 test_tavardt_api.py # Core API tests
```

## Live Quality Dashboard (Allure Report)

> **[View Live Allure Test Report](https://leovtavares.github.io/pytest-api-automation/)**
> 
> Our CI/CD pipeline automatically publishes the latest Pytest execution report to GitHub Pages using Allure. It includes detailed logs, execution times, and visual graphs of all backend tests.

## Quick Start (Developer Onboarding)

Want to run these API tests locally? It takes less than a minute.

**Prerequisites:** [Python](https://www.python.org/downloads/) (v3.11+)

```bash
# 1. Clone the repository
git clone https://github.com/leovtavares/pytest-api-automation.git
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

## The QA Engineering Ecosystem

This repository is part of a larger Quality Engineering ecosystem, demonstrating my ability to test applications across the entire testing pyramid. Check out the other layers:

- **[Playwright E2E Architecture](https://github.com/leovtavares/playwright-e2e-automation)** (Main E2E Framework)
- **[Pytest API Automation](https://github.com/leovtavares/pytest-api-automation)** (Backend JSON & Schema validation)
- **[QA Robot Framework & Python](https://github.com/leovtavares/qa-robot-framework-python)** (BDD & Keyword-Driven UI Testing)
- **[K6 Performance Testing](https://github.com/leovtavares/k6-performance-testing)** (Load, Stress & Spike Testing SLAs)

---
*This portfolio is governed by strict CI/CD and backend engineering standards.*

<br><br><br>

<a id="português"></a>
# Portfólio de Automação de API com Pytest

[![CI/CD Pipeline](https://github.com/leovtavares/pytest-api-automation/actions/workflows/pytest.yml/badge.svg)](https://github.com/leovtavares/pytest-api-automation/actions)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-Live_Dashboard-blue?logo=qameta)](https://leovtavares.github.io/pytest-api-automation/)

Bem-vindo ao meu portfólio de automação de testes de API e garantia de qualidade de backend.
Este repositório demonstra minha capacidade de validar integridade de dados, manipular requisições HTTP e implementar asserções de teste diretamente via código.

## Arquitetura do Repositório (Multi-Client)

Os scripts de teste são organizados por pastas de clientes/projetos, demonstrando uma estrutura corporativa pronta para escalar suítes de testes em diferentes ambientes de backend.

```text
📁 pytest-api-automation/
├── 📄 README.md                   # Este documento
├── 📄 requirements.txt            # Dependências Python (Pytest, Requests, Allure)
├── 📁 .github/workflows/          # Pipelines CI/CD (Geração de Allure e Deploy no GH Pages)
│
├── 📁 luxury-store/               # Validações de E-commerce
│   └── 📁 tests/
│       └── 📄 test_cart_api.py    # Validação de regras matemáticas e backend
│
├── 📁 comptia/                    # Validações de preços e vouchers
│   └── 📁 tests/
│       └── 📄 test_exam_vouchers_api.py # Checagem de tipos e JSON schema
│
├── 📁 dio/                        # Backend da Plataforma Educacional
│   └── 📁 tests/
│       └── 📄 test_profile_api.py # Validação de schema da API e injeção de 404
│
└── 📁 tavardt/                    # Camada de API para a plataforma Tavardt
    └── 📁 tests/
        └── 📄 test_tavardt_api.py # Testes da API principal
```

## Dashboard de Qualidade (Allure Report)

> **[Acessar Relatório Allure Interativo](https://leovtavares.github.io/pytest-api-automation/)**
> 
> Nossa pipeline CI/CD publica automaticamente o último relatório de execução do Pytest no GitHub Pages usando o Allure Report. Ele inclui logs detalhados de requisição, tempo de resposta e gráficos visuais.

## Quick Start (Onboarding de Desenvolvedores)

Quer rodar estes testes na sua máquina? Leva menos de 1 minuto.

**Pré-requisitos:** [Python](https://www.python.org/downloads/) (v3.11+)

```bash
# 1. Clone o repositório
git clone https://github.com/leovtavares/pytest-api-automation.git
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

## O Ecossistema de Engenharia de Qualidade

Este repositório faz parte de um ecossistema maior de Quality Engineering, demonstrando minha habilidade de testar aplicações em todas as camadas da Pirâmide de Testes. Conheça as outras camadas:

- **[Playwright E2E Architecture](https://github.com/leovtavares/playwright-e2e-automation)** (Framework Principal de E2E)
- **[Pytest API Automation](https://github.com/leovtavares/pytest-api-automation)** (Validação de Backend JSON & Schema)
- **[QA Robot Framework & Python](https://github.com/leovtavares/qa-robot-framework-python)** (Testes de UI BDD & Keyword-Driven)
- **[K6 Performance Testing](https://github.com/leovtavares/k6-performance-testing)** (SLAs de Load, Stress & Spike Testing)

---
*Este portfólio é governado por rigorosos padrões de CI/CD e engenharia de backend.*


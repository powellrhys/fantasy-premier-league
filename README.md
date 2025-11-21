# fantasy-premier-league

### Project Codebase

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=postgresql&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-BF0000?style=for-the-badge&logo=flyway&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Gherkin BDD](https://img.shields.io/badge/Gherkin%20BDD-darkgreen?style=for-the-badge&logo=cucumber&logoColor=white)


### Project GitHub Action Pipelines

![Build & Deploy](https://github.com/powellrhys/fantasy-premier-league/actions/workflows/build-and-deploy.yml/badge.svg)
![Flyway Migration](https://github.com/powellrhys/fantasy-premier-league/actions/workflows/flyway.yml/badge.svg)
![Update Fantasy Premier League Data](https://github.com/powellrhys/fantasy-premier-league/actions/workflows/update-fpl-data.yml/badge.svg)

### Codebase Coverage

![Codecov](https://codecov.io/gh/powellrhys/fantasy-premier-league/branch/main/graph/badge.svg)
![GitHub issues](https://img.shields.io/github/issues/powellrhys/fantasy-premier-league.svg)

### Codebase Structure

```
├── .github
│ └── workflows
├── backend
│ └── functions
├── flyway
│ ├── functions
│ └── models
├── frontend
│ ├── pages
│ └── functions
├── infra
├── shared
│ └── functions
└── tests
├── features
└── unit_tests
```

## Overview

**fantasy-premier-league** is a full-stack analytics application built to help Fantasy Premier League managers explore and understand performance trends across the Premier League. The system automatically collects live player, fixture, and match data from official Premier League API endpoints, processes it into structured datasets, and exposes interactive insights through a Streamlit-based interface.

- Collects and processes real-time Fantasy Premier League data from official endpoints.  
- Automates data ingestion using scheduled **GitHub Actions** workflows.  
- Stores structured datasets in a SQL environment, version-controlled using **Flyway**.  
- Provides interactive dashboards and visualisations via a **Streamlit** frontend.  
- Fully reproducible and scalable through **Terraform**-managed infrastructure.  
- Packaged and deployed using **Docker** for consistent runtime behaviour.

## Backend

- Built using **Python**, responsible for data ingestion, cleaning, and transformation.  
- Integrates with official Premier League APIs to retrieve player, team, and fixture data.  
- Processed datasets are persisted to a SQL database, with schema migrations handled through **Flyway**.  
- Backend logic is organised into modular functions for maintainability and scalability.

## Frontend

- Developed using **Streamlit**, enabling fast and interactive data exploration.  
- Dashboards visualise player statistics, team performance, fixtures, and trend analyses.  
- Designed to present clean, intuitive visualisations powered by Python and modern plotting libraries.  
- Authentication can be enabled to protect manager-specific or sensitive insights.

## Infrastructure

- Infrastructure-as-Code managed with **Terraform**, ensuring reproducible and auditable deployments.  
- Supports provisioning of database resources, hosting environments, and supporting services.  
- Containerised using **Docker** for streamlined local development and cloud deployment.  
- Can be deployed across cloud platforms or on-premise environments depending on configuration.

## Testing

- **Gherkin BDD** is used for high-level behavioural testing to ensure key workflows operate reliably.  
- **Pytest** supports unit and integration tests across backend and data-processing components.  
- Automated test execution is integrated into the CI pipeline for consistent validation.

## Deployment

The frontend application has been deployed to an azure app service. The application can be navigated to via the following url:

- [Azure App Service Deployment](https://fantasy-premier-league-frontend.azurewebsites.net/)

Due to the sensitive nature of the data, both applications are secured behind authentication, powered by oauth0. Renders of the application are illustrated below.

## Frontend Application

### Home Page
![Screenshot of Home Page](docs/assets/home_page.png?raw=true "Home Page")

### Player Analysis Page
![Screenshot of Player Analysis Page](docs/assets/player_analysis_page.png?raw=true "Player Analysis Page")

### Goalkeeper Analysis Page
![Screenshot of Goalkeeper Analysis Page](docs/assets/goalkeeper_analysis_page.png?raw=true "Goalkeeper Analysis Page")

### Outfield Player Analysis Page
![Screenshot of Outfield Player Analysis Page](docs/assets/outfield_player_analysis_page.png?raw=true "Outfield Player Analysis Page")

### Chip Analysis Page
![Screenshot of Chip Analysis Page](docs/assets/chip_analysis_page.png?raw=true "Chip Analysis Page")
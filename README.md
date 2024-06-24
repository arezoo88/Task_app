Task App Project

A Django-based task management application with cache system using redis and real-time notifications using Django Channels and Celery for background tasks.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Running Tests](#running-tests)
- [API Documentation](#api-documentation)
- [License](#license)

## Features

- Create, update, delete, and list tasks and projects
- Add comments to tasks
- Real-time notifications using Django Channels
- Background tasks with Celery and RabbitMQ
- Cache with redis
- API documentation with Swagger

## Requirements

- Docker
- Docker Compose

## Installation

1. **Clone the repository:**

    ```sh
    git clone git@github.com:arezoo88/Task_app.git
    cd source
    ```

2. **Create a `.env` file:**

    ```sh
    touch .env in source folder
    ```

    Add the content of .env-sample into your `.env` file in source folder:

3. **Build and start the Docker containers:**

    ```sh
    docker-compose up --build
    ```

4. **Create superuser:**

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

## Running the Project

1. **Start the Docker containers:**

    ```sh
    docker-compose up
    ```

2. **Access the application:**

    - API: `http://127.0.0.1:8000/api/v1/`
    - Swagger UI: `http://127.0.0.1:8000/swagger/`
    - Admin: `http://127.0.0.1:8000/admin/`

## Running Tests

1. **Run tests:**

    ```sh
    docker-compose exec web python manage.py test
    ```

## API Documentation

Access the Swagger UI at `http://127.0.0.1:8000/swagger/` for interactive API documentation.

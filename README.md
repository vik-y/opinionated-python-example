# Opinionated Python Project Example

Welcome to this straightforward example project where I've put together a combination of various Python libraries that I find useful. The project structure is quite simple, and the primary goal here is to demonstrate the basic usage of these libraries rather than to show off any advanced features or optimizations.


This project demonstrates a simple web scraping and processing application. It uses the scraper.py to define web scraping functions that can extract data from web pages, and tasks.py to handle these operations asynchronously using Celery, a distributed task queue. When you run the project using Docker Compose, it sets up the necessary environment for the web scraping application to function. Specifically, it uses Redis as a message broker for Celery, allowing tasks to be queued and processed by worker instances.

## Goal

The main goal of this project is to demonstrate usage of a few python libraries which when mixed together can drastically improve the quality of your code and also make development a lot easier.

## Project Structure

```
.
├── Dockerfile
├── Pipfile
├── docker-compose.yaml
├── main.py
├── scraper.py
├── tasks.py
├── tests
│   ├── __init__.py
│   └── test_scraper.py
└── utils.py
```

The project includes a handful of Python scripts, a Dockerfile, a Pipfile for managing dependencies, and a docker-compose file for setting up the project's environment.

## How to Run

1. Make sure you have Docker and Docker Compose installed on your machine.
2. Clone this repository and navigate to the project's directory.
3. Run the following command to build and start the Docker containers:

    ```sh
    docker-compose up
    ```

4. The application will start, and you should see the output in your terminal.

## Overview of Files

- `main.py`: This is the entry point of the application. It utilizes the Fire library for command-line interfaces, and dotenv for environment variable management.
- `scraper.py`: A script that would typically contain functions for web scraping.
- `tasks.py`: This script presumably contains Celery tasks for asynchronous job processing.
- `utils.py`: A utility script for miscellaneous helper functions.
- `tests/test_scraper.py`: A basic test file for the scraper.

## Libraries Used

- `fire`: For creating a simple command-line interface.
- `dotenv`: To load environment variables from a .env file.
- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML and extracting the information you need.
- `celery`: For asynchronous task queue/job queue.
- `pydantic`: For data validation and settings management using Python type annotations.
- `tenacity`: For retrying operations that might fail.
- `pytest`: For running tests.

## Docker and Docker Compose

This project is containerized using Docker, and the setup includes three main services:

1. `web`: The main application.
2. `worker`: The Celery worker.
3. `redis`: The message broker for Celery.

The services are defined in the `docker-compose.yaml` file.

## Final Words

This example project is kept simple and to the point. It demonstrates basic usage and integration of the mentioned libraries, and it provides a straightforward environment setup using Docker. Feel free to clone the repository, play around with the code, and adapt it to your own needs.

---

Feel free to raise an issue or submit a pull request if you have any improvements or suggestions. Happy coding!

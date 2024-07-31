# powerplant-coding-challenge


## Introduction 

This repository contains the implementation of a REST API developed for calculating the energy production needs of various powerplants. The goal of this project is to compute how much energy each power plant needs to produce based on the given load, while considering the cost of underlying energy sources (such as gas and kerosene) and the minimum (Pmin) and maximum (Pmax) production limits of each power plant. The API is built using FastAPI with Python 3.12.
## Requirements 

-Python: Version 3.12

-FastAPI: For building the API.

-Uvicorn: ASGI server for running the FastAPI app.

## Getting Started

### Prerequisites
Clone the repository:
  ```
  git clone https://github.com/ElenaDominguezNavarro/powerplant-coding-challenge.git
  cd powerplant-coding-challenge
  ```

### Create a Virtual Environment
Create a virtual environment using Pipenv with Python 3.12:
```
pipenv --python 3.12
```

### Install dependencies
Install the required packages listed in Pipfile:
```
pipenv install
```

### Activate the Virtual Environment
Activate the virtual environment with:
```
pipenv shell
```

## Running the Application

### Running the Application without Docker Compose
If you choose not to use Docker Compose, you need to set up a MySQL container manually and initialize the database.

Steps:
1. Create a MySQL container:

    Run the following command to start a MySQL container:
    ```
    docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -v /path/to/your/local/volume:/var/lib/mysql -d mysql:latest
    ```

    - --name some-mysql: Names the container.
    - -p 3306:3306: Maps the MySQL port.
    - -e MYSQL_ROOT_PASSWORD=my-secret-pw: Sets the MySQL root password.
    - -v /path/to/your/local/volume:/var/lib/mysql: Mounts a local directory to persist MySQL data.
    - -d mysql:latest: Uses the latest MySQL image.

2. Create the database and table:

    After the MySQL container is up and running, create the database error_logs and the table tb_error_logs using the SQL commands from the init.sql file.

3. Run the FastAPI application:
    ```
    python main.py
    ```

4. Access the API:

    Once the FastAPI application is running, you can access the API documentation and interact with the endpoints at http://127.0.0.1:8888/powerplant/v1/docs

### Running the Application using Docker Compose
The preferred method is to use Docker Compose, which simplifies the setup by managing both the application and the MySQL database together.

Steps:

1. Start the services:

    Run the following command to build and start the services defined in the docker-compose.yml file:
    ```
    docker-compose up --build
    ```
    This command will:

    - Build the Docker image for the application.
    - Start the MySQL container and initialize it with the init.sql file.
    - Start the application container.

2. Access the API:
  
    Once the containers are up, you can access the API documentation at http://localhost:8888/powerplant/v1/docs
    
## Running Tests
The project uses pytest for running the tests. To execute all tests, run:
```
pytest
```


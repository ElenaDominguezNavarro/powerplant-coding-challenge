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

### Running the Application
To run the FastAPI application, use the following command:
```
python main.py
```
This command will start the FastAPI application on http://127.0.0.1:8888


### Accessing the API Documentation
FastAPI automatically generates interactive API documentation. You can view it at:

- Swagger UI: http://127.0.0.1:8888/powerplant/v1/docs


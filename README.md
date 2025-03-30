# Restful API for system notification
Implementing DDD architecture in a Python application.


## Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/)


## Description

The Notification System handles Notifications and redirects them to the correct channel depending on the Topic.

Each Notification contains:
- Topic: a string
- Description: a string with a description of the problem that needs assistance from


``` 
Topic    | Channel   
----------------------
sales    | Slack
pricing  | Email
support  | Notion
```


## Project Setup

### Prerequisites
- Docker Desktop:  
  Install Docker Desktop from Docker's official website. https://www.docker.com/products/docker-desktop/
- Python 3.12:  
  The minimum version to run this project is Python 3.12
- Poetry:  
  Install Poetry. https://python-poetry.org/docs/  
  Make sure to add Poetry to your system's PATH and verify the installation.
  ```
  poetry --version
  ```


### Configuration
1. Clone the repository and navigate to the root folder.

2. Install project dependencies:
```
poetry install
```

3. Ensure Docker Desktop is running.


### Running the Project
1. Build and start the services:
```
docker-compose up --build
```

2. The API will be available at:
```
http://localhost:8000
```

3. Access FastAPI Documentation:
```
http://localhost:8000/docs#/
```


### Additional Information
- Poetry:  
  Manage dependencies and virtual environments with Poetry. To add new packages:
  ```
  poetry add package-name
  ```
- Docker:  
  - Ensure Docker Desktop is running before starting the project
  - The project uses Python 3.12 base image
  - FastAPI runs on port 8000

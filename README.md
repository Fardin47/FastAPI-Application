# FastAPI Application

# Description
This is a simple FastAPI application that allows users to manage a list of items. It includes 
endpoints to create, read, and retrieve specific items. This application is containerized using Docker.

## Setup

### How to set up the project locally and run Docker:

1. Go to a folder and open command prompt. 
2. Now paste "git clone https://github.com/Fardin47/FastAPI-Application.git"
3. Go to the project directory: "cd FastAPI-Application"
4. Run the application using: "docker-compose up --build -d"
5. See the List of Docker containers: "docker-compose ps"
6. Open "http://localhost:8000/docs"
7. To stop and Remove container: "docker-compose down"

### How to interact with the API endpoints:

GET /items:
 -> Returns a list of items.

POST /items
 -> Accepts an item in JSON format and adds it to the list.

GET /items/{item_id}
 -> Returns the details of a specific item by item_id.

### Link to Github Repository:
https://github.com/Fardin47/FastAPI-Application.git
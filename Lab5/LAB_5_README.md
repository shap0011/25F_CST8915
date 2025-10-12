# Lab 5 - CST8915 Full-stack Cloud-native Development: Containerizing the Algonquin Pet Store with Docker

### Student: Olga Durham

### St#: 040687883

#### In this lab:
 I'm learning how to containerize microservices using Docker and manage them with Docker Compose.

 #### Goal:

 - containerize the Algonquin Pet Store application, 
 - run it using Docker (either on the local machine or on a VM), 
 - prepare it for cloud-based environments.

 #### Lab Objectives:

- Understand the fundamentals of Docker containers.
- Dockerize the `order-service`, `product-service`, and `store-front` microservices of the **Algonquin Pet Store**.
- Use Docker Compose to manage multi-container applications.
- Push Docker images to a container registry Docker Hub.

#### Prerequisites:
- **Docker:** Install Docker Desktop - *DONE*

---

## Lab Steps:

---

## Step 1: Fork and Clone the Repositories

### 1.1. Forked repositories into my own account:

- [Order Service](https://github.com/shap0011/order-service-L4.git)
- [Product Service (Python)](https://github.com/shap0011/product-service-python-L4.git)
- [Product Service (Rust)](https://github.com/shap0011/product-service-rust-L4.git)
- [Store Front](https://github.com/shap0011/store-front-L4.git)

### 1.2. Cloned repositories to local machine:

<img src="./screenshots/1 clone ropos to locat machine.png" alt="Cloned repositories to local machine" title="Cloned repositories to local machine" width="300">

---

## Step 2: Containerizing the Algonquin Pet Store Microservices

### Step 2.1. Dockerize the order-service

In the `order-service` directory, created a `Dockerfile`

Build the Docker image

<img src="./screenshots/3 build docker image.png" alt="Build the Docker image" title="Build the Docker image" width="600">

Run a Docker container from order-service:latest image and expose it on port 3000

<img src="./screenshots/4 run a docker container.png" alt="Run a Docker container" title="Run a Docker container" width="700">

Open port on localhost:3000

<img src="./screenshots/5 open port on local host cannot get.png" alt="Running order-service on local host cannot get" title="Running order-service on local host cannot get" width="150">

Running test order-service

<img src="./screenshots/6 running test order service.png" alt="Run test order-service" title="Run test order-service" width="500">

Stop container

<img src="./screenshots/7 stop container.png" alt="Stop container" title="Stop container" width="300">

### Step 2.2. Dockerize the product-service

<img src="" alt="" title="" width="300">

### Step 2.3. Dockerize the store-front

<img src="" alt="" title="" width="300">

## Step 3: Using Docker Compose for Local Development

<img src="" alt="" title="" width="300">

### Step 3.1. Create a docker-compose.yml file

<img src="" alt="" title="" width="300">



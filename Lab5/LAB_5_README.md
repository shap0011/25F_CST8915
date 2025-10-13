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

Run a Docker container from `order-service:latest` image and expose it on `port 3000`

<img src="./screenshots/4 run a docker container.png" alt="Run a Docker container" title="Run a Docker container" width="700">

Open port on `localhost:3000`

<img src="./screenshots/5 open port on local host cannot get.png" alt="Running order-service on local host cannot get" title="Running order-service on local host cannot get" width="150">

Running test `order-service`

<img src="./screenshots/6 running test order service.png" alt="Run test order-service" title="Run test order-service" width="500">

Stop container

<img src="./screenshots/7 stop container.png" alt="Stop container" title="Stop container" width="300">

Check out the Docker images

<img src="./screenshots/8 check out dockerimages.png" alt="Check out Docker images" title="Check out Docker images" width="400">

### Step 2.2. Dockerize the product-service

Build the Docker image for `product-service-python`

<img src="./screenshots/9 build image for product-service-python.png" alt="Build the Docker image for product-service-python" title="Build the Docker image for product-service-python" width="600">

Build the Docker image for `product-service-rust`

<img src="./screenshots/10 build image for product-service-rust.png" alt="Build the Docker image for product-service-rust" title="Build the Docker image for product-service-rust" width="600">

### Step 2.3. Dockerize the store-front

Built the Docker image for `store-front`

<img src="./screenshots/11 created store-front image.png" alt="All needed Docker images" title="All needed Docker images" width="600">

## Step 3: Using Docker Compose for Local Development

### Step 3.1. Create a docker-compose.yml file

Created a docker-compose.yml file

<img src="./screenshots/12 created docker compose file.png" alt="Created a docker-compose.yml file" title="Created a docker-compose.yml file" width="300">

### Step 3.2. Run the application using Docker Compose

Build and run all services together

<img src="./screenshots/13 build and run all services together.png" alt="Build and run all services together" title="Build and run all services together" width="600">

## Step 4: Pushing Docker Images to a Container Registry

Log in to Docker Hub account 

<img src="./screenshots/14 log in to docker hub account.png" alt="Log in to Docker Hub account" title="Log in to Docker Hub account" width="900">

Docker images

<img src="./screenshots/15 docker images.png" alt="Docker images" title="Docker images" width="250">

### Step 4.1 Tag the images

Tag the images

<img src="./screenshots/16 tag the images.png" alt="Tag the images" title="Tag the images" width="400">

### Step 4.2 Push the images

Push the images to Container Registry

<img src="./screenshots/17 push the images to Docker Hub.png" alt="Push the images to Docker Hub" title="Push the images to Docker Hub" width="250">

## Clean Up Docker Environment

Clean up Docker Environment

<img src="./screenshots/18 cleanup docker environment.png" alt="Clean up Docker Environment" title="Clean up Docker Environment" width="500">

## Use Docker Hub Images with Docker Compose


---

## Submission

### What to Submit

1. Demo Video (Max 5 minutes)

    - Record a short demo video for the lab

2. GitHub Repository (Submission Repo)

    - You must create one GitHub repository for your lab submission.
    - This submission repository must include:
        - A README.md file with:
            - The YouTube demo video link.
            - Your final docker-compose.yaml file which uses the images from your docker hub.
        - (Optional) Notes about setup challenges or lessons learned.

### Notes about Setup Challenges / Lessons Learned

While setting up Docker for this lab, I ran into an issue where **Docker Desktop** wouldn’t open after building and running containers. It turned out that the **Docker engine (WSL backend)** had stopped running in the background. To fix it, I had to **shut down WSL, end Docker processes,** and **restart Docker Desktop**. After that, everything worked fine. This helped me learn how Docker depends on WSL on Windows and how to check if the Docker engine is actually running using commands like docker `version` and `docker ps`.

```
1) Close any stuck Docker Desktop processes

Open PowerShell (not Git Bash) and run:

taskkill /IM "Docker Desktop.exe" /F
taskkill /IM "com.docker.backend.exe" /F

2) Restart WSL (the Docker backend)
wsl --status
wsl -l -v   # you should see "docker-desktop" and "docker-desktop-data"  
wsl --shutdown

3) Relaunch Docker Desktop

From Start menu: Docker Desktop, or

& "C:\Program Files\Docker\Docker\Docker Desktop.exe"

Give it ~30–60 seconds, then in any terminal:

docker version
docker ps
```

I also learned how to create and use a **Dockerfile** to containerize an application. Writing a Dockerfile helped me understand how each instruction (such as `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, and `CMD`) contributes to building the environment for a microservice. I realized how the order of these commands can affect the image size and build time, and how important it is to structure the file properly for clean, repeatable builds.

### How to Submit

    - Push your work to a public GitHub repository (the submission repository).
    - Submit the link to your submission repository as your final lab deliverable in Brightspace.




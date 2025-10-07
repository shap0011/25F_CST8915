# Lab 4 - CST8915 Full-stack Cloud-native Development: Introduction to Docker

### Student: Olga Durham
### St#: 040687883

## Prelab (Install and Run Docker locally):

### Step 1: Docker Desktop

Docker Desktop installed and running

![Docker Desktop installed and running](./screenshots/1-docker-desktop-installed-running.png)

docker run -d -p 8080:80 docker/welcome-to-docker

Running on local host
![Running on local host](./screenshots/2-run-first-container.png)

### Step 2: Develop with containers
Complete Develop with containers Guide (Video Included)

*[getting-started-todo-app](https://github.com/shap0011/getting-started-todo-app.git) (Click to open on GitHub)*

#### The application up and running

![The application up and running](./screenshots/3-getting-started-todo-app.png)

#### Make changes to the app

![Make changes to the app](./screenshots/4-modified-getGreeting,js-file.png)

#### Change the placeholder text

![Modified placeholder](./screenshots/5-modified-placeholder.png)

#### Change the background color

![Change the background color](./screenshots/6-changed-the-background-color.png)

### Step 3: Build and push your first image
Complete Build and push your first image (Video Included)

#### Image is on Docker Hub

![Image is on Docker Hub](./screenshots/7-image-on-docker-hub.png)

#### The app opened on localhost:3000

![The app opened on localhost:3000](./screenshots/8-the-app-opened-on-localhost.png)

## Part 1: Setting Up Your Docker Host on Azure

### Step 1.1: Create an Ubuntu VM (Standard_B2s) on Azure

#### Ubuntu VM created

![Ubuntu virtual machine created](./screenshots/10-ubuntu-vm-created.png)

![Resource group and VM created](./screenshots/11-vm-resource-group-created.png)

### Step 1.2: Connect to Your VM using VS Code

#### Azure VM connected successfully via VS Code Remote SSH

![VM connected successfully via VSC](./screenshots/12-vm-connected-successfully-through-vsc.png)

### Step 1.3: Install Docker Engine Using APT Repository

### Step 1.4: Verify Docker Installation

#### Docker installation verified

![Docker installation verified](./screenshots/13-docker-installation-verifyed.png)

#### User olga added to the docker group

Docker commands running without sudo

![Docker commands running without sudo](./screenshots/14-docker-commands-run-without-sudo%20.png)
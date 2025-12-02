# Lab 9 - CST8915 Full-stack Cloud-native Development: Automating the Algonquin Pet Store with GitHub Actions

**Student: Olga Durham**

**St#: 040687883**

---

Welcome to Lab 9! In this lab, you will automate the build, test, and deployment pipeline for the [Algonquin Pet Store (On Steroids)](https://github.com/ramymohamed10/algonquin-pet-store-on-steroids) microservices using GitHub Actions. This will enable continuous integration and continuous deployment (CI/CD) for your application, streamlining development and deployment processes.

> **Note:** This lab will incur an approximate cost of $3 to your Azure credit. Be sure to clean up your resources after completing the lab to avoid additional charges.

---

## Lab Objectives

1. Understand the basics of GitHub Actions and its workflow structure.
2. Set up a CI/CD pipeline to build, test, and deploy the Algonquin Pet Store microservices.

---

## Prerequisites

1. A GitHub account with access to the forked Algonquin Pet Store repositories from the last lab.
2. Docker Hub account credentials.
3. Access to an AKS cluster as configured in previous labs (You will need to create one for this lab as well).

---

## Introduction to GitHub Actions

**GitHub Actions** is a powerful workflow automation tool integrated directly into GitHub. It enables developers to automate tasks like testing, building, and deploying code using YAML-defined workflows. Workflows consist of jobs, steps, and triggers that execute tasks in response to events, such as a code push or pull request.

### Key Components of a Workflow

- **Workflow**: The pipeline definition written in YAML and stored in the `.github/workflows/` directory.
- **Event**: The trigger for the workflow (e.g., a push to the `main` branch).
- **Job**: A group of steps executed in sequence. Jobs can run independently or depend on other jobs.
- **Step**: A single task, such as running a command or action.
- **Runner**: The virtual machine where jobs run (e.g., `ubuntu-latest`).

---

## Step 1: Fork the Repository and Set Up Secrets

1. **Fork the Required Repositories**

   - Fork the following repositories into your GitHub account:
     - [`store-front`](https://github.com/ramymohamed10/store-front-L8)
     - [`store-admin`](https://github.com/ramymohamed10/store-admin-L8)
     - [`order-service`](https://github.com/ramymohamed10/order-service-L8)
     - [`product-service`](https://github.com/ramymohamed10/product-service-L8)
     - [`makeline-service`](https://github.com/ramymohamed10/makeline-service-L8)
     - [`ai-service`](https://github.com/ramymohamed10/ai-service-L8)

| Service            | Description                              | Github Repo                                                            |
| ------------------ | ---------------------------------------- | ---------------------------------------------------------------------- |
| `store-front`      | Web app for customers to place orders    | [store-front-L8](https://github.com/shap0011/store-front-L8)           |
| `store-admin`      | Web app for store employees              | [store-admin-L8](https://github.com/shap0011/store-admin-L8)           |
| `order-service`    | Handles order placement                  | [order-service-L8](https://github.com/shap0011/order-service-L8)       |
| `product-service`  | Handles CRUD operations on products      | [product-service-L8](https://github.com/shap0011/product-service-L8)   |
| `makeline-service` | Processes and completes orders           | [makeline-service-L8](https://github.com/shap0011/makeline-service-L8) |
| `ai-service`       | AI-based product descriptions and images | [ai-service-L8](https://github.com/shap0011/ai-service-L8)             |
| `virtual-customer` | Simulates customer order creation        | [virtual-customer-L8](https://github.com/shap0011/virtual-customer-L8) |
| `virtual-worker`   | Simulates order completion               | [virtual-worker-L8](https://github.com/shap0011/virtual-worker-L8)     |
| `rabbitmq`         | RabbitMQ for an order queue              | [rabbitmq]()                                                           |
| `mongodb`          | MongoDB instance for persisted data      | [mongodb]()                                                            |

2. **Set Up Secrets**

   - Go to **Settings > Secrets and variables > Actions** in each forked repository.
   - Add the following repository secrets:
     - `DOCKER_USERNAME`: Your Docker Hub username.
     - `DOCKER_PASSWORD`: Your Docker Hub password.
     - `KUBE_CONFIG_DATA`: Base64-encoded content of your Kubernetes configuration file (`kubeconfig`). This is used for authentication with your Kubernetes cluster.
       - Run the following commands to get `KUBE_CONFIG_DATA` after connecting to your AKS cluster:
     ```bash
     cat ~/.kube/config | base64 -w 0 > kube_config_base64.txt
     ```
     Use the content of this file as the value for the KUBE_CONFIG_DATA secret in GitHub.

3. **Set Up Environment Variables (Repository Variables)**
   - Go to **Settings > Secrets and variables > Actions** in each forked repository.
   - Add the following repository variables:
     - `DOCKER_IMAGE_NAME`: The name of the Docker image to be built, tagged, and pushed (For example: `store-front-l9`).
     - `DEPLOYMENT_NAME`: The name of the Kubernetes deployment to update (For example: `store-front`).
     - `CONTAINER_NAME`: The name of the container within the Kubernetes deployment to update (For example: `store-front`).

---

## Step 2: Create the Workflow File

1. **Create the Workflow Directory**:

   - In each forked repository, create a directory named `.github/workflows/`.

2. **Add the Workflow File**:
   - Copy the `ci_cd.yaml` file from the `Workflow Files` folder into the `.github/workflows/` directory of each forked repository.

---

## Step 3: Understand the Workflow Structure

- The `ci_cd .yaml` file defines a **GitHub Actions workflow** that automates the CI/CD pipeline for your application.

### Key Workflow Steps

1. **Trigger**:
   - The workflow is triggered whenever code is pushed to the `main` branch.
   ```yaml
   on:
     push:
       branches:
         - main
   ```
2. **Jobs**:

   - **Build**: Builds and pushes a Docker image for the service to Docker Hub.
   - **Test**: Runs unit and integration tests.
   - **Release**: Promotes the Docker image to the latest tag.
   - **Deploy**: Deploys the application to AKS.

3. **Secrets and Environment Variables**:
   - Environment Variables and secrets are **securely** injected into the workflow.

---

## Step 4: Run the Workflow

1. **Create AKS cluster**:

   - Create AKS cluster and deploy the Algonquin Pet Store using the provided deployment file in Deployment Filres folder.

2. **Push Code Changes**:
   - Push a change to the main branch of your repository to trigger the workflow.
3. **Monitor Workflow Execution**:
   - Go to the Actions tab in the repository and verify the progress of the workflow jobs (Build, Test, Release, Deploy).
4. **Validate Deployment**:
   - Use kubectl commands to check the deployment status:
     `kubectl get pods` and `kubectl get services`

---

## Submissions

Submit links to your forked repositories in brightspace submission.

> **Note:** GitHub Actions output will be used for marking.

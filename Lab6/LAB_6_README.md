# Lab 6 - CST8915 Full-stack Cloud-native Development: Deploy Algonquin Pet Store to Azure Kubernetes Service (AKS)

**Student: Olga Durham**

**St#: 040687883**

---

## In this lab:

I'm gaining hands-on experience deploying microservices to AKS, connecting to the cluster using kubectl, and exposing the application to the internet.

---

## Lab Tasks: Updating API Endpoints

1. Read `kubectl` documentation: https://kubernetes.io/docs/reference/kubectl/
2. Test the essential `kubectl` commands in the provided `Kubectl-Cheat-Sheet.md` file.
3. The application’s various services (such as `product-service`, `order-service`, and `RabbitMQ Management Console`) are all accessible via the same IP address, differentiated by paths (`/products`, `/orders`, `/rabbitmq`).

- Figure out how this setup is possible.
- Store-front was slightly modified to achieve that. Examine the updated store-front repo: https://github.com/ramymohamed10/store-front-L6.
- **Hint:** start by investigating `nginx.conf` file.

  ***

## Step 1: Install `kubectl`

**1. What is `kubectl`?**

- `kubectl` is a command-line tool that allows you to communicate with and manage Kubernetes clusters. You will use `kubectl` to deploy applications, configure clusters, and inspect resources.

**2. Installing `kubectl`:**

- Follow the official installation guide to install `kubectl` on your system. The guide provides detailed instructions for various operating systems.
- [kubectl Installation Guide](https://kubernetes.io/docs/tasks/tools/)

**3. Verify `kubectl` Installation:**

- After installing, confirm that `kubectl` is properly set up by running:

```
kubectl version --client
```

[kubectl installed](./screenshots/Step_1_Install_kubectl.png)

- You should see the client version information displayed, confirming a successful installation.

  ***

## Step 2: Create an Azure Kubernetes Cluster (AKS)

---

## Step 3: Deploy the Algonquin Pet Store Application

---

## Submission

### What to Submit

1. Demo Video (Max 5 minutes)
   - Record a short demo video for the lab showing the deployed app on your AKS cluster.

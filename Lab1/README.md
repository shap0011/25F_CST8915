
# Algonquin Pet Store – Lab 1 (CST8915)

## Demo Video
<!--[Lab 1 Video demo](https://youtu.be/Vq66230olQo?si=2ldy6osolDb9s9Xr)-->

[![Watch the video](https://img.youtube.com/vi/Vq66230olQo/0.jpg)](https://youtu.be/Vq66230olQo)



## Technical Explanation

### Order Service (Node.js / Express)
The Order Service is built with Node.js. It listens on port 3000 and handles incoming order requests from the store-front. When a user submits an order, the service accepts the product details and quantity in JSON and logs/returns confirmation. It exposes a REST API endpoint /orders for the front-end to consume. It demonstrates how backend logic for processing orders can be separated into a dedicated microservice.

### Product Service (Rust / Warp)
The Product Service is implemented in Rust. It runs on port 3030 and provides a REST API /products that returns a catalog of available products in JSON format. This service is stateless and only responsible for serving product data. The store-front fetches data directly from this API to display the catalog to users. CORS is enabled to allow the Vue front-end (running on a different port) to access it.

### Store-Front (Vue.js)
The store-front is a Vue.js single-page application that provides the user interface. It runs on port 8080 and communicates with the Product Service and Order Service through HTTP requests. It fetches the product list from the Product Service and displays it to the user. When a user places an order, it sends a POST request to the Order Service. The store-front demonstrates how a front-end client integrates with multiple backend services in a microservices architecture.

## Notes & Learnings
- Needed to configure services to listen on `0.0.0.0` so they were reachable via the VM’s public IP.  
- Adjusted fetch URLs in Vue from `localhost` to the VM IP (`http://4.206.12.144`).  
- Had to allow cross-origin requests in the Rust Product Service (CORS).

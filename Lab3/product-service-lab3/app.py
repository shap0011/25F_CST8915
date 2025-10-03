import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", "3030"))

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET"]}})

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/products")
def list_products():
    products = [
        {"id": 1, "name": "Dog Food",   "price": 19.99},
        {"id": 2, "name": "Cat Food",   "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

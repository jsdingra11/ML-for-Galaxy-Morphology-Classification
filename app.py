from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="frontend")  # Serve static files from "frontend" folder

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")  # Serve index.html directly

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import db  # import modułu db.py

app = Flask(__name__)
CORS(app)  # pozwala na requesty z innych portów/domains

@app.route("/")
def home():
    return "<h1>TODO App</h1><p>Użyj /tasks aby zobaczyć zadania</p>"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = db.get_tasks()  # pobiera listę z db.py
    return jsonify(tasks)    # jsonify robimy dopiero w Flask

@app.route("/tasks", methods=["POST"])
def add_tasks():
    data = request.get_json()
    print(data, "data") 
    name = data.get("name")
    db.add_task(name)
    return jsonify({"message": "success"}), 201


    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
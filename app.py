from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

student1 = {
            "name": "Qusai",
            "age": 15,
            "title": "DevOps Engineer"}

@app.route("/", methods=['POST', 'GET'])
def main():
    return jsonify(student1)


app.run(debug=True)
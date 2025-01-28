from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load marks data from marks.json
with open("abc.json", "r") as file:
    students = json.load(file)

student_marks = {student['name']: student['marks'] for student in students}


@app.route("/api", methods=["GET"])
def get_marks():
    # Get names from query params
    names = request.args.getlist("name")
    
    # Find marks for the provided names
    marks = [student_marks.get(name, None) for name in names]
    
    return jsonify({"marks": marks})

# For local testing
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=2121)
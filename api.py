from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load marks data from marks.json
# Make sure to use the correct relative path for Vercel
file_path = os.path.join(os.path.dirname(__file__), 'abc.json')

# Check if the file exists before loading
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        students = json.load(file)
    student_marks = {student['name']: student['marks'] for student in students}
else:
    student_marks = {}

@app.route("/api", methods=["GET"])
def get_marks():
    # Get names from query params
    names = request.args.getlist("name")
    
    # Find marks for the provided names
    marks = [student_marks.get(name, None) for name in names]
    
    return jsonify({"marks": marks})

# For local testing (this won't run in Vercel)
if __name__ == "__main__":
    app.run(debug=True)

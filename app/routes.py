from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():       
    return render_template('index.html')

@app.route("/message", methods=["POST"])
def message():
    return render_template('message.html')

@app.route('/response', methods=["POST"])
def response():
    query = request.form.get("query")
    print(query)
    return f"Response: '{query}'"
from flask import render_template, request
from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    css_class: str = request.form.get("css_class")
    text: str = request.form.get("text")

    return render_template("message.html", css_class=css_class, text=text)

@app.route("/response", methods=["POST"])
def response():
    query: str = request.form.get("query")
    print(query)
    return f"Response: '{query}'"
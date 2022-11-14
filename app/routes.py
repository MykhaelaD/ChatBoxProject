from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from app import app

class QueryForm(FlaskForm):
    query = StringField()
    submit = SubmitField("Send")

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        query = form.query.data
        queryElement: str = render_template("message.html", css_class="query", text=query)
        
        response: str = f"Response: '{query}'"
        responseElement: str = render_template("message.html", css_class="response", text=response)
        print(query)
        return queryElement + responseElement
    return render_template("index.html", form=form)
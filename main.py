from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Café Name", validators=[DataRequired()])
    location = StringField("Café Location on Google Maps (URL)", validators=[DataRequired(), URL(message="Must be an URL.")])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    closed = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    ratings = ["1/5", "2/5", "3/5", "4/5", "5/5"]
    coffee_rating = SelectField("Coffee Rating", choices=[(r, r) for r in ratings], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=[("✘", "✘"), *[(r, r) for r in ratings]], validators=[DataRequired()])
    power_availability = SelectField("Power Socket Availability", choices=[("✘", "✘"), *[(r, r) for r in ratings]], validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = [field.data for field in form if field.name != "submit" and field.name != "csrf_token"]
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as file:
            file.write(f"\n{",".join(new_row)}")
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = [row for row in csv_data]
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)

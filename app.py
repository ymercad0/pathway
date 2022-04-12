import re
from flask import Flask, url_for, render_template
import model


app = Flask(__name__) 
# app.config.from_object('config') 


@app.route("/")
@app.route("/index") 
def index():
    company1 = model.Company(
			name="Microsoft",
			category="software",
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)
    review_1 = model.Review(
            company1,
            "Placeholder Review",
            "Security Engineering",
            "Security Engineer Intern",
            4,
            "B.S.",
            "Had a good time overall. Tasking was tough and hours were long.",
            5
            )
    placeholder = [review_1 for _ in range(10)]
    return render_template("index.html", recent_reviews=placeholder)
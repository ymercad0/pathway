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
			category="Software",
			logo_img="https://bit.ly/3uWfYzK",
			banner_img="https://bit.ly/3xfolJs"
			)
    company2 = model.Company(
			name="Google",
			category="Software",
			logo_img="https://bit.ly/3Jvmy5t",
			banner_img="http://somelink.com"
			)
    review_1 = model.Review(
            company1,
            "Placeholder Review",
            "Security Engineering",
            "Security Engineer Intern",
            4,
            "B.S.",
            "Had a good time overall. Tasking was tough and hours were long.",
            5,
            offer=True
            )
    review_2 = model.Review(company2, "Title", 'Software Engineering',
		                 "Position", company_rating=4, education="M.S.", interview_desc="Interview",
						 interview_rat=4, offer=False, accepted=False, start_date="05-23-2022",
						 intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
						 pay=35.25, bonuses="Bonus")
    placeholder = [review_1 for _ in range(3)]
    placeholder.extend([review_2 for _ in range(3)])
    return render_template("index.html", recent_reviews=placeholder)
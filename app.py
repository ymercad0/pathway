from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo
import model


app = Flask(__name__) 
app.config.from_object('config')
mongo = PyMongo(app)
db = mongo.db
pathway = db.pathway

@app.route('/file/<path:filename>', methods=["GET"])
def file(filename):
    """Helper route for getting files from database. Functions as wrapper for 
    mongo.send_file function.

    Args:
        filename (str): file to return
    """
    return mongo.send_file(filename)

@app.route('/create_user', methods=['POST'])
def create_user():
    """Helper route for creating users.Takes in form information and
    pushes user to database. Should only be accessed from signup route. 

    Args:
        Form:
            username (str)
            password (str)
            email (str)
            profile_pic (file)
    """
    if 'profile_image' in request.files:
        pf = request.files['profile_image']
        filename = model.hash_profile_name(pf.filename)
        user = model.User(
            request.form['username'],
            pswd=request.form['password'],
            email=request.form['email'].strip(),
            profile_pic=filename
        )
        mongo.save_file(filename,pf)
        pathway.insert_one(user.to_json())

        return redirect(url_for('index'))

@app.route('/signup', methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/")
@app.route("/index") 
def index():
    """Route for index page. Renders 'index.html' file. Currently has 
    placeholder data for debugging/visualization of work.
    """
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
    review_1 = model.Review('user',company1,"Placeholder Review","Security Engineering",
        "Security Engineer Intern",company_rating=4,education="B.S.",
        interview_desc="Had a good time overall. Tasking was tough and hours were long.",
        interview_rat=5,offer=False, accepted=False, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")
    review_2 = model.Review('user',company2, "Title", 'Software Engineering',
        "Position", company_rating=4, education="M.S.", interview_desc="Interview",
        interview_rat=4, offer=False, accepted=False, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")
    placeholder = [review_1 for _ in range(3)]
    placeholder.extend([review_2 for _ in range(3)])
    return render_template("index.html", recent_reviews=placeholder)

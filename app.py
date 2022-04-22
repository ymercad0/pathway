from flask import Flask, flash, redirect, url_for, render_template, request, session
from bson.objectid import ObjectId
import model
import bcrypt

app = Flask(__name__)
app.config.from_object('config')
mongo = model.PyMongoFixed(app)
db = mongo.db

for collection in model.collections:
    if collection not in db.list_collection_names():
        db.create_collection(collection)
        if collection == "companies":
            # add backup companies in case we reset
            # a collection
            pass

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
    interview_rat=5,offer=True, accepted=True, start_date="05-23-2022",
    intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
    pay=35.25, bonuses="Bonus")

review_2 = model.Review('user',company2, "Title", 'Software Engineering',
    "Position", company_rating=4, education="M.S.", interview_desc="I did this x y z dsdsasddddddddddddddddddd",
    interview_rat=4, offer=False, accepted=False, start_date="05-23-2022",
    intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
    pay=35.25, bonuses="Bonus")
placeholder = [review_1 for _ in range(3)]
placeholder.extend([review_2 for _ in range(3)])



@app.route('/file/<path:filename>', methods=["GET"])
def file(filename):
    """Helper route for getting files from database. Functions as wrapper for
    mongo.send_file function.

    Args:
        filename (str): file to return
    """
    return mongo.send_file(filename)

@app.route('/login',methods=['GET','POST'])
def login():
    """Login form for users. Sends POST request to itself. If it
    validates the user, redirects to index page. Taken mostly from class
    slides.
    """
    if request.method == "POST":
        users = db.users
        login_user = users.find_one({'username':request.form['username']})
        if login_user:
            db_password = login_user['password']
            password = request.form['password'].encode('utf-8')
            if bcrypt.checkpw(password,db_password):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            else:
                flash('Invalid username/password combination.', 'danger')
        else:
            flash('User not found.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logging out endpoint. Clears all local
    session information and redirects to index.
    """
    session.clear()
    return redirect('/')

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
    users = db.users
    existing_user = users.find_one({'name':request.form['username']})
    if not existing_user:
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
        else:
            user = model.User(
                request.form['username'],
                pswd=request.form['password'],
                email=request.form['email'].strip()
            )
        users.insert_one(user.to_json())
        session['username'] = user.username
        return redirect(url_for('index'))

@app.route('/signup', methods=["GET"])
def signup():
    """Endpoint for 'signup.html'
    """
    return render_template('signup.html')


@app.route("/user")
@app.route("/user/<username>")
def user():
    """Route for user's profile page with information and account controls.
    If the user is not logged in, redirect to login page?
    """
    if 'username' not in session:
        return redirect(url_for("login"))
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
        interview_rat=5,offer=True, accepted=False, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")

    review_2 = model.Review('user',company2, "Title", 'Software Engineering',
        "Position", company_rating=4, education="M.S.", interview_desc="I did this x y z dsdsasddddddddddddddddddd",
        interview_rat=4, offer=False, accepted=False, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")


    placeholder = [review_1 for _ in range(3)]
    placeholder.extend([review_2 for _ in range(3)])
    users = db.users
    reviews = db.reviews
    user = users.find_one({"username":session["username"]})
    # user_reviews = [rev for rev in reviews.find({"user":user['username']})]
    return render_template('user.html',user=user, reviews=placeholder)

@app.route("/change_password/<username>", methods=["POST"])
def change_password(username):
    form = request.form
    users = db.users
    if session['username']:
        pw_input = form['currentPassword'].encode('utf-8')
        current = users.find_one({"username":session['username']})['password']
        if bcrypt.checkpw(pw_input,current):
            #user is valid
            user = {"username":username}
            salt = bcrypt.gensalt()
            new_pw = {
                "$set": {"password": bcrypt.hashpw(form['newPassword'].encode('utf-8'),salt)}
            }
            users.update_one(user,new_pw)
            return redirect(url_for("user"))
    else:
        return "Not the user!"

@app.route("/change_pfp/<username>", methods=['POST'])
def change_pfp(username):
    users = db.users
    if session['username']:
        pf = request.files['profile_image']
        filename = model.hash_profile_name(pf.filename)
        mongo.save_file(filename,pf)
        user = {"username":username}
        new_pf = {
            "$set" : {"profile_pic":filename}
        }
        users.update_one(user,new_pf)
        return redirect(url_for("user"))
    else:
        return "Not the user!"

@app.route("/reviews", methods=["GET"])
def reviews():
    rev = db.reviews.find({})
    return render_template("reviews.html",reviews=rev)

@app.route("/reviews/<review_id>")
def view_review(review_id):
    review = db.reviews.find_one({"_id":ObjectId(review_id)})
    if not review:
        return redirect(url_for("reviews")) #NOTE: should redirect with flag to indicate non-existing review
    return render_template("view_review.html",review=review)


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
        interview_rat=5,offer=True, accepted=True, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")

    review_2 = model.Review('user',company2, "Title", 'Software Engineering',
        "Position", company_rating=4, education="M.S.", interview_desc="I did this x y z dsdsasddddddddddddddddddd",
        interview_rat=4, offer=False, accepted=False, start_date="05-23-2022",
        intern_desc="desc", work_rat=None, culture_rat=None, location=("San Francisco", "California"),
        pay=35.25, bonuses="Bonus")


    placeholder = [review_1 for _ in range(3)]
    placeholder.extend([review_2 for _ in range(3)])
    company1.company_rat = 3.8
    company1.work_rat = 3
    company1.culture_rat = 2.5

    company2.company_rat = 5


    companies = [company1, company2, company1, company1, company2, company1, company2]

    if 'username' in session:
        current_user = db.users.find_one({"username":session['username']})
        if not current_user:
            return render_template("index.html", recent_reviews=placeholder, companies=companies, user=None)
        return render_template("index.html", recent_reviews=placeholder, companies=companies, user=current_user)
    return render_template("index.html", recent_reviews=placeholder, companies=companies, user=None)

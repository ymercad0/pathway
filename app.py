from flask import Flask, redirect, url_for, render_template, request, session, flash
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
                return 'Invalid username/password combination.'
        else:
            return 'User not found.'
    else:
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


@app.route('/create_company', methods=['POST'])
def create_company():
    if 'add_comp_button' in request.form and request.form['add_comp_button'] == "clicked":
        # save company logo image
        logo_img = request.files['comp_logo_img']
        logo_filename = model.hash_profile_name(logo_img.filename)
        mongo.save_file(logo_filename, logo_img)

        if 'comp_banner_img' in request.files:
            banner_img = request.files['comp_banner_img']

        else:
            banner_img = url_for('static', filename='Images/Icons/default-banner.jpg')

        banner_filename = model.hash_profile_name(banner_img.filename)
        mongo.save_file(banner_filename, banner_img)


        new_comp = {"name": request.form['comp_name'], "category": request.form['comp_category'],
            "logo_img": logo_filename, "description": request.form['comp_description'],
            "banner_img": banner_filename}

        # initialize all the hidden company attributes
        new_comp = model.Company(new_comp["name"], new_comp["category"], new_comp["logo_img"],
                            new_comp["description"], new_comp["banner_img"])

        db.companies.insert_one(new_comp.to_json())
        flash(f"{new_comp.name} was added to the list of companies!", "success")

    return render_template("company-admin.html", categories=model.company_categories)

@app.route('/signup', methods=["GET"])
def signup():
    """Endpoint for 'signup.html'
    """
    return render_template('signup.html')


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

@app.route('/company-admin', methods=['GET', 'POST'])
def company_admin():
    return render_template("company-admin.html", categories=model.company_categories)

from flask import Flask, redirect, url_for, render_template, request, session, flash
from bson.objectid import ObjectId
import bcrypt
import model

app = Flask(__name__)
app.config.from_object('config')
mongo = model.PyMongoFixed(app)
db = mongo.db

for collection in model.collections:
    if collection not in db.list_collection_names():
        db.create_collection(collection)

        if collection == "companies":
            with app.app_context():
                model.reset_comp_collection()


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


@app.route('/company-admin/created', methods=['POST'])
def create_company():
    if 'add_comp_button' in request.form and request.form['add_comp_button'] == "clicked":
        comp_name = request.form['comp_name']
        if db.companies.find_one({"name": comp_name}):
            flash(f"{comp_name} already exists!", "danger")

        else:
            # save company logo image
            logo_img = request.files['comp_logo_img']
            logo_filename = model.hash_profile_name(logo_img.filename)
            mongo.save_file(logo_filename, logo_img)

            # banner was not selected
            # empty FileStorage objects evaluate as False
            if not request.files.get('comp_banner_img', None):
                # default banner img
                banner_filename = "../static/Images/Backup/default-banner.jpg"

            else:
                banner_img = request.files['comp_banner_img']
                banner_filename = model.hash_profile_name(banner_img.filename)
                mongo.save_file(banner_filename, banner_img)

            # initialize all the hidden company attributes
            new_comp = model.Company(comp_name, request.form['comp_category'], logo_filename,
                                request.form['comp_description'], banner_filename)

            db.companies.insert_one(new_comp.to_json())
            flash(f"{new_comp.name} was added to the list of companies!", "success")

    return redirect(url_for('company_admin'))

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
    if db.reviews.count_documents({}) == 0:
        reviews = None
    else:
        # '.limit()' limits the amount of documents queried
        reviews = db.reviews.find().sort('date_posted', -1).limit(5)

    # -1 sorts in descending order
    companies = db.companies.find().sort("company_rat", -1).limit(4)
    return render_template("index.html", recent_reviews=reviews, companies=companies, to_comp_obj=model.to_company_obj,
                            user=None)

@app.route('/company-admin', methods=['GET', 'POST'])
def company_admin():
    # in case anyone resets all of the companies
    if db.companies.count_documents({}) == 0:
        model.reset_comp_collection()

    if request.method == 'POST':
        # remove companies
        if 'remove_comp_button' in request.form and request.form['remove_comp_button'] == "clicked":
            to_remove = request.form['comp_remove']
            if not db.companies.find_one_and_delete({'name': to_remove}):
                flash(f"{to_remove} doesn't exist!", "danger")

            else:
                flash(f"{to_remove} was removed from the database!", "success")

    return render_template("company-admin.html", categories=model.company_categories)

@app.route('/companies/', methods=['GET'])
def companies():
    # displays the top 10 highest rated companies
    comps = db.companies.find().sort("company_rat", -1).limit(10)
    return render_template("companies.html", companies=comps, to_comp_obj=model.to_company_obj)

@app.route('/companies/<company_name>', methods=['GET'])
def company_page(company_name):
    comp = db.companies.find_one({"name_lower": company_name})

    if not comp:
        flash("Accessed an invalid URL.", "danger")
        return redirect(url_for('companies'))

    # if db.reviews.count_documents({}) == 0:
    #     reviews = None
    # else:
    #     reviews = db.reviews.find().sort('date_posted', -1).limit(5)

    return render_template('company.html', company=model.to_company_obj(comp), reviews = None)

from flask import Flask, redirect, url_for, render_template, request, session
# from flask_pymongo import PyMongo
import model
import bcrypt



app = Flask(__name__) 
app.config.from_object('config')
mongo = model.PyMongoFixed(app)
db = mongo.db
if "users" not in db.list_collection_names():
    db.create_collection("users")
    #TODO: Use save_file to store default.jpg for non-logged in users or default pic.


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
    users = db.users
    reviews = db.reviews
    user = users.find_one({"username":session["username"]})
    user_reviews = [rev for rev in reviews.find({"user":user['username']})]
    return render_template('user.html',user=user, reviews=user_reviews)


@app.route("/")
@app.route("/index") 
def index():
    """Route for index page. Renders 'index.html' file. Currently has 
    placeholder data for debugging/visualization of work.
    """

    if 'username' in session:
        current_user = db.users.find_one({"username":session['username']})
        if not current_user:
            return render_template("index.html", recent_reviews=placeholder, user=None)
        return render_template("index.html", recent_reviews=placeholder, user=current_user)
    return render_template("index.html", recent_reviews=placeholder, user=None)
        

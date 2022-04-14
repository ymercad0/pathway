from datetime import datetime
import bcrypt
import re

company_categories = ["Software", "Hardware", "Computing", "Finance", "Government", "Defense", "Aerospace",
                      "Restaurant", "Automobiles", "Aviation", "Retail", "Other"]

job_categories = ["Software Engineering", "Computer Science", "Information Technology", "System Administrator",
                  "Computer Engineering", "Eletrical Engineering", "Data Science", "Security Engineering",
                  "Other"]

degrees = ["B.S.", "B.A.", "M.S.", "M.A.", "Ph.D.", "Other"]

states = {
    'Alaska': 'AK',
    'Alabama': 'AL',
    'Arkansas': 'AR',
    'Arizona': 'AZ',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'District of Columbia': 'DC',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Iowa': 'IA',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Massachusetts': 'MA',
    'Maryland': 'MD',
    'Maine': 'ME',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Missouri': 'MO',
    'Mississippi': 'MS',
    'Montana': 'MT',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Nebraska': 'NE',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'Nevada': 'NV',
    'New York': 'NY',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Virginia': 'VA',
    'Vermont': 'VT',
    'Washington': 'WA',
    'Wisconsin': 'WI',
    'West Virginia': 'WV',
    'Wyoming': 'WY',
    'Remote': 'N/A'
    }

def is_url(url:str)->bool:
    """
    Uses urrlib library to parse URL, then checks if parsed url is valid.
    Taken from https://bit.ly/3ObxIjB

    Args:
        url (str): The url to validate

    Returns:
        bool: Indicates URL validity
    # """
    regex = ("((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" +
            "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (url is None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, url)):
        return True
    else:
        return False

def validate_date(date:str)->None:
    """Validates a given date. Raises
       a value error if the date isn't
       in the correct month, date, year
       format.

    Args:
        date (str): The date, as a string, to validate.

    Raises:
        ValueError: Raised if the given date isn't in the requested
                    month, day, year format.
    """
    try:
        datetime.strptime(date, '%m-%d-%Y')

    except ValueError:
        raise ValueError("Incorrect date format. Should be MM-DD-YYYY")

def validate_email(email:str)->bool:
    """Validates an email.

    Args:
        email (str): The email string to validate.

    Returns:
        bool: A boolean indicating whether the email, passed in as a parameter, is valid.
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex,email):
        return True
    return False

def hash_profile_name(name:str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(name.encode("utf-8"),salt)
    return hashed.decode("utf-8")

class Company:
    """Represents an existing and reviewable company.
        Contains internal information on the amount
        of reviews submitted to that company as well
        as the company's status on Pathway.

        Attributes:
            name: A string, representing the company's name.
            category: A string, representing the category the company belongs to.
            logo_img:
            description: A string, representing the company's description.
            banner_img:
            company_rat: The average of the company's overall rating, as a float.
            work_rat: The average of the company's workplace reviews, as a float.
            culture_rat: A float denoting the average of the company's culture reviews.
            num_company_reviews: The total number of ratings under the overall rating category, as an integer.
            num_work_reviews: The total number of workplace reviews, as an integer.
            num_culture_reviews: An integer denoting the total number of work culture reviews.
            total_reviews: An integer representing the overall, singular number of reviews.
            status: A string representing the company's status. Must be a valid CSS color keyword.
    """
    def __init__(self, name:str, category:str, logo_img:str, description:str="", banner_img:str="")->None:
        """Initializes a reviewable Company.

        Args:
            name (str): The company's name.
            category (str): The category the company falls under.
            logo_img (str):
            description (str, optional): A description on the current company.
            banner_img (str, optional):

        Raises:
            TypeError: Raised if any of the arguments aren't of the expected types.
            ValueError: Raised if the company's name, categories, and more are of the correct types but not supported.
        """
        #type checks
        if type(name) is not str:
            raise TypeError(f"Error: Company name must a string. Given type '{type(name)}'.")
        if type(category) is not str:
            raise TypeError(f"Error: Company category must be a string. Given type '{type(category)}'.")
        if type(logo_img) is not str:
            raise TypeError(f"Error: Company logo_img must be a string. Given type '{type(logo_img)}'.")
        if type(description) is not str:
            raise TypeError(f"Error: Company description must be a string. Given type '{type(description)}'.")
        if type(banner_img) is not str:
            raise TypeError(f"Error: Company banner_img must be a string. Given type '{type(banner_img)}'.")

        #value checks
        if len(name) == 0:
            raise ValueError("Error: Company name cannot be empty.")

        if len(category) == 0:
            raise ValueError("Error: Company category cannot be empty.")

        if category not in company_categories:
            raise ValueError("Error: Invalid company category.")

        if not is_url(logo_img):
            raise ValueError("Error: Invalid URL given for company logo.")

        if not is_url(banner_img) and banner_img != "":
            raise ValueError("Error: Invalid URL given for banner image.")

        self.name = name
        self.category = category
        self.logo_img = logo_img
        self.description = description
        self.banner_img = banner_img
        # None simply means that no scores have been
        # added. There must be a way to distinguish a
        # company from having a score of 0 and a
        # company that has no ratings
        self.company_rat = None
        self.work_rat = None
        self.culture_rat = None
        # number of reviews in each category,
        # prevents the need to have to query
        # and search through the whole database
        # each time
        self.num_company_reviews = 0
        self.num_work_reviews = 0
        self.num_culture_reviews = 0
        # the total amount of reviews
        # the previous entries dont count
        # as individual reviews
        self.total_reviews = 0
        # a company will have a color border
        # around them depending on their rating.
        # the status must be a supported CSS
        # color keyword
        self.status = "grey"

    def update_status(self)->None:
        """Updates the company's status. A company
           status is a color indicating whether the
           company has had favorable reviews or not.
           This manifests around the company logo's
           circumference on the front end. Changes
           based on what numerical ranges the company's
           overall reviews fall under.
        """
        if self.company_rat is not None:
            if self.company_rat == 5:
                self.status = "green"

            elif self.company_rat >= 4 and self.company_rat < 5:
                self.status = "lightgreen"

            elif self.company_rat >= 3 and self.company_rat < 4:
                self.status = "orange"

            elif self.company_rat >= 2 and self.company_rat < 3:
                self.status = "red"

            # rating of 0-1.99
            else:
                self.status = "black"

class User:
    """Represents a user class. Contains the user's information such as
       their username, email, password, and more.

        Attributes:
            username: A string, representing the user's username.
            email: The user's email, as a string.
            password: The user's confirmed password, as plaintext. Hashed once the account is created.
            profile_pic:
            creation_time: A datetime object, containing the time the user account was created.
    """
    def __init__(self, username:str, email:str, pswd:str, profile_pic:str="default.jpg")->None:
        """Initializes a user given the information
           the user decides to input.

        Args:
            username (str): The user's username.
            email (str): The user's email.
            pswd (str): The user's password, as plaintext.
            profile_pic (str, optional):

        Raises:
            TypeError: Raised if none of the parameters match the expected types.
            ValueError: Raised if the parameters match the expected types but fail any validation checks.
        """
        #type checks
        if type(username) is not str:
            raise TypeError(f"Error: username must a string. Given type '{type(username)}'.")
        if type(email) is not str:
            raise TypeError(f"Error: email must a string. Given type '{type(email)}'.")
        if type(pswd) is not str:
            raise TypeError(f"Error: password must a string. Given type '{type(pswd)}'.")
        if type(profile_pic) is not str:
            raise TypeError(f"Error: profile_pic must a string. Given type '{type(profile_pic)}'.")

        #value checks
        if len(username) <= 3:
            raise ValueError("Error: usernames must have more than 3 characters.")
        if not validate_email(email):
            raise ValueError(f"Error: Invalid email. Given email {email} with type {type(email)} ")
        if len(pswd) < 8:
            raise ValueError("Error: Password must be 6 or more characters.")
        if len(profile_pic) == 0:
            raise ValueError("Error: Invalid Profile Picture name.")

        self.username = username
        self.email = email
        self.password = self.generate_password(pswd)
        self.profile_pic = profile_pic
        self.creation_time = datetime.now()

    def generate_password(self, unhashed:str)->bytes:
        """Generates a secure, hashed version of
           the user's password, initially passed
           in as plaintext, with bcrypt's methods.

        Args:
            unhashed (str): The user's password as plaintext.

        Returns:
            bytes: A hashed representation of the user's password, in bytes.
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(unhashed.encode("utf-8"), salt)
        return hashed

    def set_profile_pic(self,link:str)->bool:
        if type(link) is not str:
            raise TypeError("Error: Link to profile picture must be a string.")

        if not is_url(link):
            return False
        self.profile_pic = link
        return True 

    def to_json(self)->dict:
        return {
            "username":self.username,
            "email":self.email,
            "password":self.password,
            "profile_pic":self.profile_pic,
            "creation_time":self.creation_time
        }

class Review:
    """Represents a review posted to a specific company.
       Contains information pertaining to the user's intern
       experience at the company reviewed along with the date
       the review was posted. Affects the company's score
       based on what the user rated.

        Attributes:
            user: A string indicating which user account created the review.
            company: The Company object of the company to be rated by the user.
            job_cat: The general job category the internship falls under, as a string.
            position: A string representing the position the user had at the company.
            company_rating: An integer denoting the overall company rating.
            education: A string representing the current level of education pursued by the user.
            interview_desc: The review description, as a string, of the company's interview process and more.
            interview_rat: An integer, denoting the interview process experience at the company.
            offer: A boolean, indicating whether the user was presented with an offer from the company.
            accepted: A boolean, indicating whether the user accepted an offer at the company.
            start_date: The internship start date, as a string.
            intern_desc: The internship experience description, as a string.
            work_rating: An integer denoting whether the company's work culture was good or not.
            culture_rating: An integer quantifying the company's culture, enviroment, and values.
            location: A tuple of strings in city, state format containing the internship location.
            pay: The internship pay per hour, as a float.
            bonuses: A string of any extra bonuses the company might offer at the internship.
            date_posted: A datetime object, representing the date the internship was posted.
    """
    def __init__(self, user:str, company:'Company', title:str, job_cat:str, position:str, company_rating:int, education:str,
                interview_desc:str, interview_rat:int, offer:bool=False, accepted:bool=False,
                start_date:str="", intern_desc:str="", work_rat:int=None, culture_rat:int=None,
                location:tuple=("None", "Remote"), pay:float=None, bonuses:str="")->None:

        """Initializes a Review object based on the parameters passed;
           the fields the user decides to fill out.

        Args:
            user(str): The username of the account that created the review.
            company (Company): The company to rate.
            job_cat (str): The general job category the internship falls under.
            position (str): The position held at the company.
            company_rating (int): The overall company rating.
            education (str): The degree currently pursued by the user.
            interview_desc (str): A description of the interview process.
            interview_rat (int): The interview process rating.
            offer (bool, optional): Whether the company presented an offer to the user.
            accepted (bool, optional): Whether the user accepted the offer.
            start_date (str, optional): The internship start date.
            intern_desc (str, optional): The internship description.
            work_rating (int, optional): The company's work culture rating.
            culture_rating (int, optional): The company's culture, enviroment, and values rating.
            location (tuple, optional): The location of the internship in city, state format.
            pay (float, optional): The internship pay per hour.
            bonuses (str, optional): Any bonuses granted by the company to the user not mentioned
                                     in any of the previous categories.

        Raises:
            TypeError: Raised if any of the arguments don't match the expected types.
            ValueError: Raised if the arguments are of the correct types but aren't supported
                        by the website.
        """
        if type(user) != str:
            raise TypeError("Username that created the review must be a string!")

        if not user or len(user) <= 3:
            raise ValueError("Invalid username!")

        if type(company) != Company:
            raise TypeError("Company to review must be a company object!")

        if type(title) != str:
            raise TypeError("Review title must be a string!")

        if not title:
            raise ValueError("Review title cannot be empty!")

        if type(job_cat) != str:
            raise TypeError("Job category must be a string!")

        if job_cat not in job_categories:
            raise ValueError("Invalid job category!")

        if type(position) != str:
            raise TypeError("Position within the company must be a string!")

        if not position:
            raise ValueError("Position held at the company cannot be empty!")

        for words in position.split():
            if not words.isalpha():
                raise ValueError("Special or empty characters cannot be present in the position title!")

        if type(company_rating) != int:
            raise TypeError("Company rating must be an integer!")

        if company_rating < 0 or company_rating > 5:
            raise ValueError("Cannot rate a company more than the max or min allowed score.")

        if type(education) != str:
            raise TypeError("Your education level must be a string!")

        if education not in degrees:
            raise ValueError(f"{education} is not a valid degree!")

        if type(interview_desc) != str:
            raise TypeError("Interview description must be formatted as a string!")

        if not interview_desc:
            raise ValueError("Interview description cannot be empty!")

        if type(interview_rat) != int:
            raise TypeError("Interview rating must be an integer!")

        if interview_rat < 0 or interview_rat > 5:
            raise ValueError("Cannot rate an interview more than the max or min allowed score.")

        # optional params
        if type(offer) != bool:
            raise TypeError("An offer must be a boolean!")

        if type(accepted) != bool:
            raise TypeError("Accepting an offer must be a boolean!")

        if not offer and accepted:
            raise ValueError("Cannot accept an offer without having an offer.")

        if type(start_date) != str:
            raise TypeError("Start date must be formatted as a string!")

        # will raise a Value Error if the start date isn't formatted correctly
        # and start_date isn't its default value
        if start_date != "":
            validate_date(start_date)

        if type(intern_desc) != str:
            raise TypeError("Internship description must be a string!")

        if work_rat != None:
            if type(work_rat) != int:
                raise TypeError("Internship rating must be an integer!")

            if work_rat < 0 or work_rat > 5:
                raise ValueError("Work rating cannot be lower or greater than the allowed min or max values.")

        if culture_rat != None:
            if type(culture_rat) != int:
                raise TypeError("Culture rating must be an integer!")

            if culture_rat < 0 or culture_rat > 5:
                raise ValueError("Culture rating cannot be lower or greater than the allowed min or max values.")

        if type(location) != tuple:
                raise TypeError("Internship location must be formatted as a tuple!")

        if len(location) != 2:
            raise ValueError("Tuple must only contain a city and a state.")

        city, state = location

        if type(city) != str:
            raise TypeError("City must be a string!")

        if type(state) != str:
            raise TypeError("State must be a string!")

        if state not in states:
            raise ValueError("Invalid state! States must not be abbreviated.")

        for words in city.split():
            if not words.isalpha():
                raise ValueError("City must only contain alphabetical characters.")

        if pay != None:
            if type(pay) not in [int, float]:
                raise TypeError("Hourly pay must be a numerical value!")

            if pay < 0:
                raise ValueError("Hourly pay cannot be negative!")

        if type(bonuses) != str:
            raise TypeError("Any additional info on bonuses must be a string!")

        self.user = user
        self.company = company
        self.job_cat = job_cat
        self.position = position
        self.company_rating = company_rating
        self.education = education
        self.interview_desc = interview_desc
        self.interview_rat = interview_rat
        self.offer = offer
        self.accepted = accepted
        self.start_date = start_date
        self.intern_desc = intern_desc
        self.work_rating = work_rat
        self.culture_rating = culture_rat
        self.location = location
        self.pay = pay
        self.bonuses = bonuses
        self.date_posted = datetime.now()

    def update_scores(self)->None:
        """Once a review is posted, updates the scores of the reviewed
           company of the category rated. The algorithm to update
           each company's score runs in constant space and time
           and only modifies that company's attributes. The scores
           submitted by the user are kept in the review object.
        """

        def score_formula(old_score:float, num_reviews:int, new_score:int)->float:
            """Returns the updated rating of any field without having to re-calculate
               the previous averages.

            Args:
                old_score (float): The previous average of the scores.
                num_reviews (int): The number of reviews submitted for the category to be rated.
                new_score (int): The new score to be entered into the average calculation.

            Returns:
                float: The updated average of the company's reviews.
            """
            return ((old_score * num_reviews) + new_score)/(num_reviews + 1)

        # number of reviews in each category
        num_reviews = [self.company.num_company_reviews, self.company.num_work_reviews,
                      self.company.num_culture_reviews]

        for index, num_scores in enumerate(num_reviews):
            match index:
                case 0:
                    # this indicates the user rated this field
                    if self.company.company_rat is None:
                        # this is initially None.
                        # it sets the old score avg to 0
                        # in order to calculate the initial
                        # avg. Remember there is a distinction
                        # between a company with a review avg of 0
                        # and no reviews
                        self.company.company_rat = 0

                    # this field must always be reviewed. Not optional in the
                    # Review class constructor
                    self.company.company_rat = score_formula(self.company.company_rat,
                                                            num_scores, self.company_rating)
                    self.company.num_company_reviews += 1
                    # any review needs at least the company attribute
                    # rated
                    self.company.total_reviews += 1

                case 1:
                    if self.work_rating is not None:
                        # first time work is reviewed
                        if self.company.work_rat is None:
                            self.company.work_rat = 0

                        self.company.work_rat = score_formula(self.company.work_rat,
                                                             num_scores, self.work_rating)

                        self.company.num_work_reviews += 1


                case 2:
                    if self.culture_rating is not None:
                        # first time culture is reviewed
                        if self.company.culture_rat is None:
                            self.company.culture_rat = 0

                        self.company.culture_rat = score_formula(self.company.culture_rat,
                                                             num_scores, self.culture_rating)

                        self.company.num_culture_reviews += 1


local_companies = {Company("Microsoft", "Software", "https://bit.ly/3uWfYzK", banner_img="https://bit.ly/3xfolJs")}
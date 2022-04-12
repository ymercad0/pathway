from datetime import datetime

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
    }

def is_url(url:str)->bool:
    """
    Uses urrlib library to parse URL, then checks if parsed url is valid.
    Taken from https://bit.ly/3ObxIjB

    Args:
        url (str): The url to validate
    Returns:
        bool indicating validity
    """
    from urllib.parse import urlparse
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
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

class Company:
    def __init__(self, name:str, category:str, logo_img:str, description:str="", banner_img:str="")->None:
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

class User:
    def __init__(self, username:str, email:str, pswd:str, profile_pic:str="")->None:
        pass

class Review:
    def __init__(self, company:'Company', title:str, job_cat:str, position:str, company_rating:int, education:str,
                interview_desc:str, interview_rat:int, offer:bool=False, accepted:bool=False,
                start_date:str="", intern_desc:str="", work_rat:int=None, culture_rat:int=None,
                location:tuple=None, pay:float=None, bonuses:str="")->None:

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

        if location != None:
            if type(location) != tuple:
                raise TypeError("Internship location must be formatted as a tuple!")

            if len(location) != 2:
                raise ValueError("Tuple must only contain a city and a state.")

            city, state = location

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

    def update_scores(self, num_reviews:list)->None:
        """Once a review is posted, updates the scores of the reviewed
           company of the category rated.

        Args:
            reviews (list): A list containing the number of reviews in each category.
                            The first index contains the number of reviews submitted
                            for the company rating, the second the number of reviews
                            for the workplace ratings, and the third and last index
                            contains the amount of reviews for that company's culture.

        Raises:
            TypeError: If any of the arguments don't correspond to the expected types.
            ValueError: If the reviews list isn't of the expected size or its contents
                        aren't integers.
        """

        def score_formula(old_score:float, num_reviews:int, new_score:int)->float:
            """Returns the updated rating of any previously rated field without
               having to re-calculate the previous averages.

            Args:
                old_score (float): The previous average of the scores.
                num_reviews (int): The number of reviews submitted for that category.
                new_score (int): The new score to be entered into the average calculation.

            Returns:
                str: The final orders' total in pennies, as a string.
            """
            return ((old_score * num_reviews) + new_score)/(num_reviews + 1)

        if type(num_reviews) != list:
            raise TypeError("The number of reviews for each category must be a list!")

        if len(num_reviews) != 3:
            raise ValueError("Review score's list cannot be empty.")

        for num_scores in num_reviews:
            # can be None because None simply means that field wasn't completed
            if num_scores != None:
                if type(num_scores) != int:
                    raise TypeError("The number of new scores must be an integer!")

                if num_scores < 1:
                    raise ValueError("Must have a negative or nonzero number of reviews in any category.")

        for index, num_scores in enumerate(num_reviews):
            # for when the first review is submitted
            if num_scores is None:
                num_scores = 0

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

                    # this field must always be reviewed
                    self.company.company_rat = score_formula(self.company.company_rat,
                                                            num_scores, self.company_rating)

                case 1:
                    if self.work_rating is not None:
                        # first time work is reviewed
                        if self.company.work_rat is None:
                            self.company.work_rat = 0

                        self.company.work_rat = score_formula(self.company.work_rat,
                                                             num_scores, self.work_rating)

                case 2:
                    if self.culture_rating is not None:
                        # first time culture is reviewed
                        if self.company.culture_rat is None:
                            self.company.culture_rat = 0

                        self.company.culture_rat = score_formula(self.company.culture_rat,
                                                             num_scores, self.culture_rating)

local_companies = {Company("Microsoft", "Software", "https://bit.ly/3uWfYzK", banner_img="https://bit.ly/3xfolJs")}
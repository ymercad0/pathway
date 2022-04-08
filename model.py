from dataclasses import dataclass, asdict
from datetime import datetime

company_categories = ["Software", "Hardware", "Computing", "Finance", "Government", "Defense", "Aerospace",
                      "Restaurant", "Automobiles", "Aviation", "Retail", "Other"]

job_categories = ["Software Engineering", "Computer Science", "Information Technology", "System Administrator",
                  "Computer Engineering", "Eletrical Engineering", "Data Science", "Security Engineering"]

degrees = ["B.S.", "B.A.", "M.S.", "M.A.", "Ph.D."]

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
    def __init__(self, name:str, comp_cat:str, logo_img:str, description:str="", banner_img:str="")->None:
        pass

class User:
    def __init__(self, username:str, email:str, pswd:str, profile_pic:str="")->None:
        pass

@dataclass
class Review:
    def __init__(self, company:str, job_cat:str, position:str, company_rating:int, education:str,
                interview_desc:str, interview_rat:int, offer:bool=False, accepted:bool=False,
                start_date:str="", intern_desc:str="", work_rat:int=None, culture_rat:int=None,
                location:tuple=(), pay:float=None, bonuses:str="")->None:

        if type(company) != str:
            raise TypeError("Company to review must be a string!")

        if not company:
            raise ValueError("Company must not be an empty string!")

        if type(job_cat) != str:
            raise TypeError("Job category must be a string!")

        if job_cat not in job_categories:
            raise ValueError("Invalid job category!")

        if type(position) != str:
            raise TypeError("Position within the company must be a string!")

        for words in position.split():
            if not words.isalpha():
                raise ValueError("Special or empty characters cannot be present in the position title!")

        if type(company_rating) != int:
            raise TypeError("Company rating must be an integer!")

        if company_rating > 5 or company_rating < 0:
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

        if type(work_rat) != int and work_rat != None:
            raise TypeError("Internship rating must be an integer!")

        if work_rat < 0 or work_rat > 5:
            raise ValueError("Work rating cannot be lower or greater than the allowed min or max values.")

        if type(culture_rat) != int and culture_rat != None:
            raise TypeError("Culture rating must be an integer!")

        if culture_rat < 0 or culture_rat > 5:
            raise ValueError("Culture rating cannot be lower or greater than the allowed min or max values.")

        if type(location) != tuple:
            raise TypeError("Internship location must be formatted as a tuple!")

        if len(tuple) != 2:
            raise ValueError("Tuple must only contain a city and a state.")

        state, city = location

        if state not in states:
            raise ValueError("Invalid state! States must not be abbreviated.")

        for words in city.split():
            if not words.isalpha():
                raise ValueError("City must only contain alphabetical characters.")

        if type(pay) not in [int, float] and pay != None:
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
        self.work_rat = work_rat
        self.culture_rat = culture_rat
        self.location = location
        self.pay = pay
        self.bonuses = bonuses

local_companies = {Company("Microsoft", "Software", "https://bit.ly/3uWfYzK", banner_img="https://bit.ly/3xfolJs")}
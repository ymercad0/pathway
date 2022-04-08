from dataclasses import dataclass, asdict

# job categories, more must be added
categories = ["Software Engineer", "System Administrator"]

class Company:
    def __init__(self, name:str)->None:
        pass

@dataclass
class User:
    def __init__(self, username:str, email:str, pswd:str)->None:
        pass


@dataclass
class Review:
    def __init__(self, category:str, position:str, company_rating:int, education:str,
                interview_desc:str, interview_rat:int, offer:bool=False, start_date:str="",
                intern_desc:str="", intern_rat:int=None, location:str="",
                pay:float=None, bonuses:str=""):
        pass
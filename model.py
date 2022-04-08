from dataclasses import dataclass, asdict

# list of jobs
jobs = []

class Company:
    def __init__(self, name:str)->None:
        pass

@dataclass
class User:
    def __init__(self, username:str, email:str, pswd:str)->None:
        pass


@dataclass
class Review:
    def __init__(self, job:str, education:str, interview_desc:str, interview_rat:int, \
                offer:bool=False, intern_desc:str="", intern_rat:int=None,
                location:str="", pay:float=None, bonuses:str=""):
        pass
import os
SECRET_KEY = os.urandom(16).hex()
#TODO: reset this password bc it's in plaintext
MONGO_URI= f"mongodb+srv://admin:Rqs7wmYA1qkMzh8X@pathway.rgqhh.mongodb.net/pathway?retryWrites=true&w=majority"
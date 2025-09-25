from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://zeelmavani113_db_user:Po0KTJ49jzQB2C8s@payroll.tohit33.mongodb.net/?retryWrites=true&w=majority&appName=Payroll"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.payroll     

def get_next_id(name):
    counter = db.counters.find_one_and_update(
        {"_id": name},
        {"$inc": {"sequence_value": 1}},
        return_document=True
    )
    return counter["sequence_value"]


#users collection
user_collection = db["users"]
collection = db["teams"]
collection = db["expense"]
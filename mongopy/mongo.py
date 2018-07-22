import pprint
from pymongo import MongoClient


client = MongoClient('localhost', 27017)  # connecting to MongoDB running locally in Docker
mydb = client['testdb']  # creating a database
collection = mydb['mytable']  # creating a table (called "collection" in Mongo)

test_record = {
    "who": "me",
    "loves kittens": "very much",
    "want to have at least": 10
}

records = mydb.records
record_id = records.insert_one(test_record).inserted_id
pprint.pprint(records.find_one())

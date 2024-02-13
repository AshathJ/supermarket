import pymongo

url= 'mongodb://localhost:27017'

client = pymongo.MongoClient(url)

#db = client['products']   #database connection
ndb = client['shop'] 
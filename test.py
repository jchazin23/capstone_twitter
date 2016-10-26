## this should be run once connected to the aws instance


from twython import Twython
from pymongo import MongoClient

client = MongoClient()
db = client.twitter_final
col = db.tweets

col.find_one() ## this returns one tweet


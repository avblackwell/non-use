import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'rWd3sX5kVIohvjwcrKc7o9x8d'
consumer_secret = 'ns8JDYzsLygjZ6918bQHAcJhDhvJPmOthKeJyOXI3BTMVHd1Ug'
access_token = '762437887-qfxkHDGNklifOZBojhhK8Dnh4rEmaVkr7HdkOQrp'
access_token_secret = '3am3SzATYTwqMLtmRvcrrcCnRb6sxw1VC7xsvJWJdn72h'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####Delete Facebook Hash
# Open/Create a file to append data
csvFile = open('df.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="delete facebook",count=100,
                           lang="en",
                           since="2017-01-01").items():
    print ("Name:", tweet.author.name.encode('utf8'))
    print ("Tweet created:", tweet.created_at)
    print ("Tweet:", tweet.text.encode('utf8'))
    print ("Location:", tweet.user.location.encode('utf8'))
    print ("Geo:", tweet.geo)
    csvWriter.writerow([tweet.author.name.encode('utf8'), tweet.created_at, tweet.text.encode('utf-8'), tweet.user.location.encode('utf8'), tweet.geo])
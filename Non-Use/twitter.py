import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'rWd3sX5kVIohvjwcrKc7o9x8d'
consumer_secret = 'ns8JDYzsLygjZ6918bQHAcJhDhvJPmOthKeJyOXI3BTMVHd1Ug'
access_token = '762437887-qfxkHDGNklifOZBojhhK8Dnh4rEmaVkr7HdkOQrp'
access_secret = '3am3SzATYTwqMLtmRvcrrcCnRb6sxw1VC7xsvJWJdn72h'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

api.update_status('@jonarbuckles')
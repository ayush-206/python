#1)What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
#solution-

#An access token is an object encapsulating the security identity of a process or thread.
# A token is used to make security decisions and to store tamper-proof information about some system entity. 
# While a token is generally used to represent only security information, 
# it is capable of holding additional free-form data that can be attached while the token is being credited
# Tokens can be duplicated without special privilege, for example to create a new token with lower levels
# of access rights to restrict the access of a launched application An access token is used by Windows 
# when a process or thread tries to interact with objects that have security descriptors (securable objects).
# An access token is represented by the system object of type Token.

#Access Token	101012352121221120-xSxN7yBqebXudfjhdhffjejd
#Access Token Secret	LOHq16guQhgjhkjhlk1k;lkk_iyjkh454hgh206


 
#2)Get the IP address of some common sites like Google, Facebook by using DNS lookup.
#ip address of google
nslookup google.com
Non-authoritative answer:
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Name:    google.com
Addresses:  2404:6800:4002:803::200e
          172.217.24.238
		  
#ip address of facebook		  
nslookup facebook.com
Non-authoritative answer:
Server:  google-public-dns-a.google.com
Address:  8.8.8.8

Name:    facebook.com
Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
          157.240.13.35

#3)Using Tweepy library try to extract tweets from Twitter
import tweepy
consumer_key='qFyDvjojCEu9jNuhfjhjjfkjvkff'
consumer_secret='VMJR1xe8sAMufsYfifoifok34oj6jhdfhghi68fgkggj5'
access_token='1011137942021115906-xSxgopio4505jgjogot0tkt505ugogi'
access_token_secret='LOHq16guQpmLyQlxcDgtu50ogu5-rkgt5tpho96ygi0t8'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#jobs',lang="en",count=10,tweet_mode="extended")
for tweet in tweets:
 print("..........")
 print(tweet.full_text)
 print("..........")

#4)What is a difference between library and API . Figure it out with examples.
#solution-Difference between a library and an API


# API is a part of library which defines how an application communicates with external code
# .
# API can be written in any language.
# Library is written in same language which is a collection of all the functionalities required for the use case.
# For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# We can create our own APIs using Python Framework like Django and Flask which can be used in websites.























'''
todo 
1. Automate download of timeYourWeb CSV 
2. Automate open/close/delete of csv 
'''

import csv 
import random 
from venmo_api import Client
import config


def addTime(filter, reader):
    totalTime = 0
    for row in reader: 
        for each in filter: 
            if each in row[0]:
                totalTime += int(row[2])
    return totalTime

socialMedia = ["www.youtube.com", "www.netflix.com", "wwww.twitter.com"]
accessToken = Client.get_access_token(username = config.USERNAME , password = config.PASSWORD )
venmo = Client(access_token = accessToken)
friends = venmo.user.get_user_friends_list("nevansawmadonna")

for friend in friends: 
    print(friend.username, friend.id)
randomFriend = friends[random.randint(0, len(friends))]


activeTime = 0 
#limit is in seconds
limit = 60 * 60 

with open('../../../Downloads/Summary - Tue 2nd Jun 2020 (Today).csv') as csvFile:
    reader = csv.reader(csvFile)
    activeTime += addTime(socialMedia, reader)

#Check if time spent on youtube is over the limit 
if activeTime > limit: 
    difference = (activeTime -  limit)/60
    print("EXCEEDED TIME LIMIT BY " , activeTime-limit, " minutes | ENDURE THE PUNISHMENT")
    venmo.payment.request_money(difference, "I have no self control", randomFriend.id)
else:
    print("YOU HAVE STAYED WITHIN THE LIMIT | YOU HAVE ESCAPED PUNISHMENT")

venmo.log_out("Bearer " + accessToken)
import os
import time
import datetime

eventList = []

# list to store the people in, and have the program print a message 
# to invite the people to your event.  Be sure the invite message 
# prints the person, and the invite, including the name of the event 
# you are inviting them to
def printEventList():
  print()
  
  for invitee, addInvitee in enumerate(eventList, start = 1):
    print(f"{invitee}.\t {addInvitee}")

# While loop for adding event invites
while True:
    # listMenu - would you like to add a name to the beginning, middle, or end of the list

    addInvitee = input("Invitee's first and last name: ")

    if(addInvitee) not in eventList:
       eventList.append(addInvitee)
       print(f"{addInvitee} has been added to the event")
       print()

    elif (addInvitee) in eventList:
       print("Invitee already added to Event")
       print()
    




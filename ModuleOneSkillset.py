import os
import datetime

eventList = []

for i in eventList:
   print(i)

while True:
    addInvitee = input("Invitee's first and last name: ")

    if(addInvitee) not in eventList:
       eventList.append(addInvitee)
       print(f"{addInvitee} has been added to the event")
       print()

    elif (addInvitee) in eventList:
       print("Invitee already added to Event")
       print()
    



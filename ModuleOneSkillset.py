


eventList = []

print("Event Invitation Maker")
print()
eventChoice = input("What is the name of your Event? ")
print()

# list to store the people in, and have the program print a message 
# to invite the people to your event.  Be sure the invite message 
# prints the person, and the invite, including the name of the event 
# you are inviting them to
def printEventList():
	print()
  
	for invitee in eventList:
		print(f"Welcome, you have been invited to attend the Event: {eventChoice}")
		print(f"Hello {invitee} your presense at the {eventChoice} has been requested!\n{messageRequest()}")

def messageRequest():
	eventMessage = input("Please enter your event message here: ")
	return eventMessage


# While loop for adding event invites
while True:
    # listMenu - would you like to add a name to the beginning, middle, or end of the list
	eventMenu = input("Do you want to view, add, edit, or clear Event List: ").strip().lower()
   
	if eventMenu == "add":
		addInvitee = input("Invitee's first and last name: ").strip().capitalize()

		if(addInvitee) not in eventList:
			eventList.append(addInvitee)
			print(f"{addInvitee} has been added to the event")
			print()

		elif (addInvitee) in eventList:
			print("Invitee already added to Event")
			print()
    
	elif eventMenu == "edit":
		addInvitee = input("Who do you want to remove? ").strip().capitalize()
		confirmation = input(f"Are you sure you wish to clear {addInvitee} from the Event List? ").strip().lower()
        
		if addInvitee in eventList and confirmation == "yes":
			eventList.remove(addInvitee)
			print(f"{addInvitee} Has been removed from the list")
        
		elif addInvitee in eventList and confirmation == "no":
			print()
			print(f"The Invitee {addInvitee} will remain in the list")
     	
		else:
			print()
			print("{addInvitee} not in Event List")
        
	elif eventMenu == "view":
		print()
		printEventList()
		
	elif eventMenu == "clear":
		confirmation = input(f"Are you sure you want to clear All Invitees from the Event List?" ).strip().lower()

		if confirmation == "yes":
			print("The EventList has been cleared")
			eventList.clear()

		elif confirmation == "no":
			print("List will not be cleared")
	
	else:
		break
	
	# time.sleep(1)
	# os.system("clear")

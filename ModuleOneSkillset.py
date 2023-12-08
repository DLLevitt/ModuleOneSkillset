import random


eventList = ["Charles", "Shaun", "Amy", "Malissa", "Jeremiah"]
foodList = ["Appetizer", "Meal", "Dessert", "Drink"]
ageList = []
eventFoodDict = {}
nameAgeFoodDict = []

print("Event Invitation Maker")
print()
eventChoice = input("What is the name of your Event? ")
print()

# # function to print Event Invitations
# def printEventList():
# 	eventMessage = messageRequest()
	
# 	for invitee in eventList:
# 		print(f"Welcome, you have been invited to attend the Event: {eventChoice}")
# 		print(f"Hello {invitee} your presense at the {eventChoice} has been requested!\n{eventMessage}")

# function to create event message
def messageRequest():
	messageChoice = input("Press Enter to add your own Event Message or type Default: ").strip().lower()
	eventMessage = ""

	if messageChoice != "default":
		eventMessage = input("Please enter your event message here: ")
		for invitee in eventList:
			print()
			print(f"{invitee}, We cordially invite you to join us for our {eventChoice} Event!\n{eventMessage}\nWe Hope to see you there!")
			print()
	
	elif messageChoice == "default":
		for invitee in eventList:
			eventMessage = f"Welcome {invitee}, \nYour presence is being requested. \nyou have been invited to attend the Event: {eventChoice}!"
			print()
			print(f"{eventMessage}\n")
	
	# return eventMessage

# add names to beginning, middle, and end of list
def listEntries(eventList):
	for name in range(4):
		userInput = input("Invitee's Name to add: ").strip().capitalize()
		if name == 0:
			eventList.insert(0, userInput)
		elif name == 1 or name == 2:
			findMid = len(eventList) // 2
			eventList.insert(findMid, userInput)
		elif name == 3:
			eventList.append(userInput)
	return eventList


# Takes Invitees from eventList and food from foodList to create a meal plan dictionary
def mealPlanMaker():
	for count, name in enumerate(eventList):
		eventFoodDict[name] = [food + chr(ord("A") + count) for food in foodList]
	return eventFoodDict

def nameAgeFoodMaker():
	if not eventFoodDict:
		mealPlanMaker()
	for eachName in eventList:
		randomAge = random.randint(1, 100)
		nameAgeFood = {"first name": eachName, "age": randomAge, "food": eventFoodDict[eachName]}
		nameAgeFoodDict.append(nameAgeFood)
	return nameAgeFoodDict

# binary search for age
def binaryAgeSearch(list, age):

	if len(list) == 0:
		return False

	sortedList = sorted(list, key=lambda x: x["age"])
	middle = len(sortedList)//2

	if sortedList[middle]["age"] == age:
		return True
	
	if sortedList[middle]["age"] < age:
		return binaryAgeSearch(sortedList[middle+1:], age)

	else:
		return binaryAgeSearch(sortedList[0:middle], age)
  
# binary search for food
def binaryFoodSearch(list, food):
	if len(list)  == 0:
		return False

	sortedList = sorted(list, key = lambda x: x["food"][0])
	middle = len(sortedList) // 2
  
	if sortedList[middle]["food"][0] == food:
		return True
    
	if sortedList[middle]["food"][0] < food:
		return binaryFoodSearch(sortedList[middle+1:], food)
    
	else:
		return binaryFoodSearch(sortedList[0:middle], food)

# print(binaryAgeSearch(nameAgeFoodDict, 9))

# While loop to bring all desired output together
while True:
    # listMenu - would you like to add a name to the beginning, middle, or end of the list
	eventMenu = input("Do you want to view, add, or edit Event List: ").strip().lower()
	print()
	if eventMenu == "add":
		addInvitee = listEntries(eventList)

		if(addInvitee) not in eventList:
			eventList.append(addInvitee)
			print(f"{addInvitee} has been added to the event")
			print()

		elif (addInvitee) in eventList:
			print("Invitee already added to Event")
			print()
    
	elif eventMenu == "edit":

		confirmation = input("Do you want to sort the list yes/no")
		if confirmation == "yes":
			eventList.sort(reverse = True)
			print(eventList)

		elif confirmation == "no":
			print("List will not be sorted in reverse")
		# addInvitee = input("Who do you want to remove? ").strip().capitalize()
		# confirmation = input(f"Are you sure you wish to clear {addInvitee} from the Event List? ").strip().lower()
        
		# elif eventMenu == "clear":
		# 	confirmation = input(f"Are you sure you want to clear All Invitees from the Event List?" ).strip().lower()
		# if confirmation == "yes":
		# 	print("The EventList has been cleared")
		# 	eventList.clear()

		# elif confirmation == "no":
		# 	print("List will not be cleared")

		# if addInvitee in eventList and confirmation == "yes":
		# 	eventList.remove(addInvitee)
		# 	print(f"{addInvitee} Has been removed from the list")
        
		# elif addInvitee in eventList and confirmation == "no":
		# 	print()
		# 	print(f"The Invitee {addInvitee} will remain in the list")
     	
		# else:
		# 	print()
		# 	print("{addInvitee} not in Event List")
        
	elif eventMenu == "view":

		viewMenu = input("What would you like to view: (1 - Invitation, 2 - Reverse Order list, 3 - Number of Invitees, 4 - Full Course, 5 - Binary search: ")

		if viewMenu == "1":
			print()
			# printEventList()
			messageRequest()
		
		elif viewMenu == "2":
			print()
			print(sorted(eventList, reverse = True))
			print()
			print(f"Original order of List: {eventList}")

		elif viewMenu == "3":
			print()
			print(f"There are {len(eventList)} people invited to attend your {eventChoice} event.")

		elif viewMenu == "4":
			print()
			mealPlanMaker()
			print(eventFoodDict)

		elif viewMenu == "5":
			print()
			print(sorted(nameAgeFoodMaker(), key = lambda x: x['age']))
			print()

			guessAge = int(input("Enter an Age: "))
			searchedPerson = binaryAgeSearch(nameAgeFoodDict, guessAge)

			if searchedPerson is True:
				for person in nameAgeFoodDict:
					if person["age"] == guessAge:
						print(f"{person['first name']}, {person['age']}, {person['food']}")
						print()
			
			else:
				print("No person with the specified age found")

			foodChoice = input("Enter a food:")
			searchedFood = binaryFoodSearch(nameAgeFoodDict, foodChoice)

			if searchedFood is True:
				for food in nameAgeFoodDict:
					print(f"{food['first name']}, {food['age']}, {food['food']}")

			else:
				print("No food with specified name found")

	
	else:
		break
	
	# time.sleep(1)
	# os.system("clear")

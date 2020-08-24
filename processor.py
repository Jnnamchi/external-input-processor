# Welcome the user with a welcome message
def welcomeUser():
	print("\nWelcome to the external input processor, I will process and analyze data from anywhere!\n")

# Get Username from terminal input
def getUsername():
	# Print message prompting user to input their name
	usernameFromInput = input("To begin, please enter your username:\n")
	return usernameFromInput

# Say hello to the user, acknowledging you have their username
def greetUser(name):
	print("Hello, " + name)

welcomeUser()
username = getUsername()
greetUser(username)

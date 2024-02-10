passDict = {
	"Ahmed" : 1394,
	"Ali" : 6078,
	"Amr" : 9354
}

def authentication(username, password):
	if username in passDict:
		if int(password) == passDict[username]:
			return True
		return False

username = input("Please enter your username\n").capitalize()
password = input("Please enter your password\n")

if authentication(username, password):
    print(f"Welcome, {username}!\n")
else:
    print("Incorrect username or password!\n")
"""
LAMBDA (anonymous) functions 
"""
# map()
# reduce()
# filter()

area_of_rectangle = lambda l, w : l * w
print(f"Area of a given rectangle is: {area_of_rectangle(4, 5)}")

def displayGreeting():
	count = 0
	global user_name # global keyword makes it accessible outside the function
	user_name = "Dover, Ben" # input("What's your name: ")
	
	def numOfLogins():
		nonlocal count # avails outer variable to inside function only
		count += 1
		return f"You've logged on, {count} time(s)!"
	
	msg = numOfLogins()
	return (f"Hello, {user_name}. {msg}")

print(displayGreeting())
print(user_name) # accessible due to global keyword

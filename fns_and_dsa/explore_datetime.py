import datetime

def display_current_datetime():	
	current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # format this way YYYY-MM-DD HH:MM:SS
	return current_date

def calculate_future_date():
	number_of_days = int(input("Enter the number of days to add to the current date: "))

	# now + number of days
	future_date = datetime.datetime.strptime(display_current_datetime(), "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=number_of_days)  
	
	return "Future date: " + future_date.strftime("%Y-%m-%d")

print(f"Current date and time: {display_current_datetime()}")
print(calculate_future_date())
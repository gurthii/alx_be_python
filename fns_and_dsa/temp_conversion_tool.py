FAHRENHEIT_TO_CELSIUS_FACTOR = 9/5
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
	result = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
	return f"{fahrenheit}°F is {result}°C"

def convert_to_fahrenheit(celsius):
	result = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
	return f"{celsius}°C is {result}°F"


def main():
	temperature = int(input("Enter the temperature to convert: "))
	temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

	if temp_unit == "F" or "f":
		print(convert_to_celsius(temperature))
	elif temp_unit == "C" or "c":
		print(convert_to_fahrenheit(temperature))
	else:
		print("Invalid temperature. Please enter a numeric value.”")


if __name__ == "__main__":
    main()
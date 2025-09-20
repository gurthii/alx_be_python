num1, num2 = int(input("Enter the first number: ")), int(input("Enter the second number: "))
operation_type = input("Choose the operation (+, -, *, /): ")

match operation_type:
	case operation_type if operation_type == "+":
		print(f"The result is [{num1 + num2}].")
	case operation_type if operation_type ==  "-":
		print(f"The result is [{num1 - num2}].")
	case operation_type if operation_type == "*":
		print(f"The result is [{num1 * num2}].")
	case operation_type if operation_type == "/":
		try:
			num1 / num2
			print(f"The result is [{num1 / num2}].")
		except ZeroDivisionError:
			print("Cannot divide by zero.")

	case _:
		print("Something went haywire!")
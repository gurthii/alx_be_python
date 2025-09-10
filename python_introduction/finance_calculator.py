monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthtly expenses: "))

savings = monthly_income - total_expenses
interest = 0.05

projected_savings = int(savings * 12 + (savings * 12 * 0.05))

print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
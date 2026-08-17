print("*"*50)
print("👩Personal Finance Tracker")
print("*"*50)
print("Track your monthly income and expenses!")
print("Get insights into your spending habits")
print("*"*50)

# Personal Information
name = input("Enter User Name: ")
age = int(input("Enter User Age: "))
salary = float(input("Enter Monthly Salary: "))
saving = input("Do You Have Saving Account? (TRUE/FALSE): ")
financial = input("Enter Your Financial Goal: ")

# Income Details
main_job_salary = float(input("Enter Your Main Job Salary: "))
side_income = float(input("Enter Your Side Income: "))
other_income = float(input("Enter Your Other Income: "))

# Monthly Expenses
rent = int(input("Enter Monthly Rent: "))
food = int(input("Enter Monthly Food Expenses: "))
transport = int(input("Enter Monthly Transportation Expenses: "))
entertainment = int(input("Enter Monthly Entertainment Expenses: "))
utilities = int(input("Enter Monthly Utilities Expenses: "))
miscellaneous = int(input("Enter Monthly Miscellaneous Expenses: "))

# Calculations
total_income = main_job_salary + side_income + other_income
total_expenses = rent + food + transport + entertainment + utilities + miscellaneous

monthly_savings = total_income - total_expenses
annual_savings = monthly_savings * 12

saving_ratio = (monthly_savings / total_income) * 100
expense_ratio = (total_expenses / total_income) * 100

rent_per = (rent / total_expenses) * 100
food_per = (food / total_expenses) * 100
transport_per = (transport / total_expenses) * 100
entertainment_per = (entertainment / total_expenses) * 100
utilities_per = (utilities / total_expenses) * 100
miscellaneous_per = (miscellaneous / total_expenses) * 100

saving_money = monthly_savings > 0
overspending = total_expenses > total_income

# Financial Summary
print("\n" + "*"*50)
print(" 📝FINANCIAL SUMMARY")
print("*"*50)

print("User Name:", name)
print("User Age:", age)
print("Monthly Salary:", salary)
print("Saving Account:", saving)
print("Financial Goal:", financial)

print("\n" + "*"*50)
print("💰INCOME DETAILS")
print("*"*50)
print("Main Job Salary:", main_job_salary)
print("Side Income:", side_income)
print("Other Income:", other_income)
print("Total Income:", total_income)

print("\n" + "*"*50)
print("🏧EXPENSE DETAILS")
print("*"*50)
print("Rent:", rent)
print("Food:", food)
print("Transportation:", transport)
print("Entertainment:", entertainment)
print("Utilities:", utilities)
print("Miscellaneous:", miscellaneous)
print("Total Expenses:", total_expenses)

print("\n" + "*"*50)
print("💸SAVINGS DETAILS")
print("*"*50)
print("Monthly Savings:", monthly_savings)
print("Annual Savings:", annual_savings)
print("Saving Ratio:", saving_ratio, "%")
print("Expense Ratio:", expense_ratio, "%")

print("\n" + "*"*50)
print("✨EXPENSE PERCENTAGE")
print("*"*50)
print("Rent:", rent_per, "%")
print("Food:", food_per, "%")
print("Transportation:", transport_per, "%")
print("Entertainment:", entertainment_per, "%")
print("Utilities:", utilities_per, "%")
print("Miscellaneous:", miscellaneous_per, "%")

print("\n" + "*"*50)
print("📌FINANCIAL STATUS")
print("*"*50)
print("Saving Money:", saving_money)
print("Overspending:", overspending)

print("*"*50)
print("🙏Thank You for Using Personal Finance Tracker")
print("*"*50)
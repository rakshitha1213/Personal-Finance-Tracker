# 👩 Personal Finance Tracker

A simple **Python Personal Finance Tracker** that helps users calculate their monthly income, expenses, savings, and spending percentages. This project demonstrates basic Python programming concepts such as user input, data types, arithmetic operators, comparison operators, and formatted output.

## Features

* 👤 **Personal Information**

  * Collects user's name and age.
  * Records monthly salary.
  * Records whether the user has a savings account.
  * Captures the user's financial goal.

* 💰 **Income Details**

  * Accepts main job salary.
  * Accepts side income.
  * Accepts other sources of income.
  * Calculates total monthly income.

* 🏧 **Expense Details**

  * Records monthly rent.
  * Records food expenses.
  * Records transportation expenses.
  * Records entertainment expenses.
  * Records utility expenses.
  * Records miscellaneous expenses.
  * Calculates total monthly expenses.

* 💸 **Savings Calculation**

  * Calculates monthly savings.
  * Calculates estimated annual savings.
  * Calculates saving ratio.
  * Calculates expense ratio.

* 📊 **Expense Percentage**

  * Calculates the percentage spent on:

    * Rent
    * Food
    * Transportation
    * Entertainment
    * Utilities
    * Miscellaneous expenses

* 📌 **Financial Status**

  * Determines whether the user is saving money.
  * Determines whether the user is overspending.

## Concepts Used

This project demonstrates:

* `input()` for user input
* `int()` and `float()` type conversion
* Variables and data types
* Arithmetic operators
* Comparison operators
* Boolean values
* Basic calculations
* String formatting and concatenation
* Formatted console output
* Basic financial calculations

## Calculations Used

### Total Income

```text
Total Income = Main Job Salary + Side Income + Other Income
```

### Total Expenses

```text
Total Expenses = Rent + Food + Transportation + Entertainment + Utilities + Miscellaneous
```

### Monthly Savings

```text
Monthly Savings = Total Income - Total Expenses
```

### Annual Savings

```text
Annual Savings = Monthly Savings × 12
```

### Saving Ratio

```text
Saving Ratio = (Monthly Savings / Total Income) × 100
```

### Expense Ratio

```text
Expense Ratio = (Total Expenses / Total Income) × 100
```

### Expense Percentage

For each expense category:

```text
Expense Percentage = (Category Expense / Total Expenses) × 100
```

## How It Works

1. The program displays the **Personal Finance Tracker** title.
2. The user enters personal information.
3. The user enters income details.
4. The user enters monthly expenses.
5. The program calculates:

   * Total income
   * Total expenses
   * Monthly savings
   * Annual savings
   * Saving ratio
   * Expense ratio
   * Individual expense percentages
6. The program determines the financial status using Boolean expressions.
7. A complete financial summary is displayed.

## Example Input

```text
**************************************************
👩Personal Finance Tracker
**************************************************
Track your monthly income and expenses!
Get insights into your spending habits
**************************************************

Enter User Name: Rakshitha
Enter User Age: 22
Enter Monthly Salary: 30000
Do You Have Saving Account? (TRUE/FALSE): TRUE
Enter Your Financial Goal: Save for future

Enter Your Main Job Salary: 30000
Enter Your Side Income: 5000
Enter Your Other Income: 2000

Enter Monthly Rent: 8000
Enter Monthly Food Expenses: 5000
Enter Monthly Transportation Expenses: 2000
Enter Monthly Entertainment Expenses: 1500
Enter Monthly Utilities Expenses: 2000
Enter Monthly Miscellaneous Expenses: 1000
```

## Example Output

```text
**************************************************
 📝FINANCIAL SUMMARY
**************************************************
User Name: Rakshitha
User Age: 22
Monthly Salary: 30000
Saving Account: TRUE
Financial Goal: Save for future

**************************************************
💰INCOME DETAILS
**************************************************
Main Job Salary: 30000
Side Income: 5000
Other Income: 2000
Total Income: 37000

**************************************************
🏧EXPENSE DETAILS
**************************************************
Rent: 8000
Food: 5000
Transportation: 2000
Entertainment: 1500
Utilities: 2000
Miscellaneous: 1000
Total Expenses: 19500

**************************************************
💸SAVINGS DETAILS
**************************************************
Monthly Savings: 17500
Annual Savings: 210000
Saving Ratio: 47.29 %
Expense Ratio: 52.70 %

**************************************************
✨EXPENSE PERCENTAGE
**************************************************
Rent: 41.02 %
Food: 25.64 %
Transportation: 10.25 %
Entertainment: 7.69 %
Utilities: 10.25 %
Miscellaneous: 5.12 %

**************************************************
📌FINANCIAL STATUS
**************************************************
Saving Money: True
Overspending: False
**************************************************
🙏Thank You for Using Personal Finance Tracker
**************************************************
```

## Validation

The current beginner-level version performs basic calculations and comparison-based validation:

* Calculates total income.
* Calculates total expenses.
* Calculates savings.
* Checks whether monthly savings are greater than zero.
* Checks whether expenses are greater than income.

> **Note:** The program currently assumes that the user enters valid numeric values. Non-numeric input may cause a `ValueError`.

## Future Improvements

Some possible improvements for this project:

* 📅 Add monthly transaction dates.
* 💾 Store financial records in a file or database.
* 📊 Add charts for income and expenses.
* 📈 Track finances across multiple months.
* 🎯 Add financial goal tracking.
* ⚠️ Add advanced input validation.
* 🧾 Add detailed transaction history.
* 👥 Support multiple users.
* 📱 Create a graphical user interface.
* 📊 Export financial reports to Excel or CSV.

## Author

**Personal Finance Tracker**

A beginner-friendly Python project created to practice **Python fundamentals, data types, operators, user input, and basic financial calculations**.


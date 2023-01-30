import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Constants
FILE_NAME = 'expenses.csv'
HEADER = ['date', 'category', 'description', 'amount']

# Function to add an expense
def add_expense(date, category, description, amount):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

# Function to predict expenses and make recommendations
def predict_expenses(expenses, category):
    expenses = expenses[expenses['category'] == category]
    expenses['date'] = pd.to_datetime(expenses['date'])
    expenses.sort_values('date', inplace=True)
    expenses['month'] = expenses['date'].dt.month
    expenses['year'] = expenses['date'].dt.year
    expenses_grouped = expenses.groupby(['year', 'month']).sum()

    X = expenses_grouped.index.codes[0].reshape(-1, 1)
    y = expenses_grouped['amount'].values

    model = LinearRegression().fit(X, y)
    prediction = model.predict(X[-1].reshape(1, -1) + 1).tolist()[0]

    print("Predicted expense for next month: ", prediction)
    print("Recommendation:")
    if prediction > expenses_grouped['amount'].mean():
        print("You should try to reduce expenses in the", category, "category.")

# Check if the CSV file exists and create it if not
try:
    with open(FILE_NAME) as file:
        pass
except FileNotFoundError:
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)

# Continuously prompt the user to add expenses
while True:
    date = input("Enter date (YYYY-MM-DD): ")
    if not re.match(r'\d{4}-\d{2}-\d{2}', date):
        print("Invalid date format. Try again.")
        continue

    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    if not re.match(r'\d+(\.\d{2})?', amount):
        print("Invalid amount format. Try again.")
        continue

    add_expense(date, category, description, amount)
    expenses = pd.read_csv(FILE_NAME)
    predict_expenses(expenses, category)


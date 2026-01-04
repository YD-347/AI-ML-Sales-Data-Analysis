import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("expenses.csv")
print(data)

amount=np.array(data["Amount"])
print("Total Expense:",np.sum(amount))
print("Average Expense:",np.mean(amount))
print("Highest Expense:", np.max(amount))

category_expense = data.groupby("Category")["Amount"].sum()
print(category_expense)

plt.figure()
category_expense.plot(kind="bar")
plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

plt.figure()
plt.pie(category_expense, labels=category_expense.index, autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()



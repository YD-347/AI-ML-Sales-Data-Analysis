import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("sales_data.csv")
print(data)

sales=np.array(data["Sales"])

total_sales=np.sum(sales)
print("Total Yearly sales:",total_sales)

average_sales=np.mean(sales)
print("Average Monthly sales:",average_sales)

max_sales=np.max(sales)
print("Highest Monthly sales:",max_sales)

min_sales=np.min(sales)
print("Lowest Monthly sales:",min_sales)

best_month=data.loc[data["Sales"].idxmax()]
worst_month=data.loc[data["Sales"].idxmin()]

print("Best Month:")
print(best_month)

print("Worst Month:")
print(worst_month)

plt.figure()
plt.plot(data["Month"], data["Sales"])
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure()
plt.bar(data["Month"], data["Sales"])
plt.xticks(rotation=45)
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

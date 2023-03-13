name = "My Matplotlib module"

import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("VS project\exercises\company_sales_data.csv")
profit = df['total_profit'].tolist()
months = df['month_number'].tolist()
plt.plot(months, profit, label = "the graph of knowing stuff", color = "blue", linestyle ="--", linewidth ="3", marker = "o", markerfacecolor = "black")
plt.xlabel('month label')
plt.ylabel('profit')
plt.xticks(months)
plt.yticks([100000, 200000, 300000, 400000, 500000]) 
plt.title("company profits a year")
plt.legend(loc='upper left')
plt.show()
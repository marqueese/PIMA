name = "My Matplotlib module"

import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("VS project\exercises\company_sales_data.csv")
profit = df['total_profit'].tolist()
months = df['month_number'].tolist()
facecream = df["facecream"].tolist()
facewash = df["facewash"].tolist()
toothpaste = df["toothpaste"].tolist()
bathingsoap = df ['bathingsoap'].tolist()
shampoo = df ['shampoo'].tolist()
moisturizer = df ['moisturizer'].tolist()

plt.plot(facecream, label = "facewash sales", color = "blue", linestyle ="--", linewidth ="3", marker= "o")
plt.plot(facewash, label = "facewash sales", color = "red", linestyle ="--", linewidth ="3",  marker= "o")
plt.plot(toothpaste, label = "toothpaste sales", color = "green", linestyle ="--", linewidth ="3",  marker= "o")
plt.plot(bathingsoap, label = "bathingsoap sales", color = "orange", linestyle ="--", linewidth ="3",  marker= "o")
plt.plot(shampoo, label = "shampoo sales", color = "red", linestyle ="--", linewidth ="3",  marker= "o")
plt.plot(moisturizer, label = "moisturizer sales", color = "pink", linestyle ="--", linewidth ="3",  marker= "o")

plt.xlabel('month label')
plt.ylabel('profit')
plt.xticks(months)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title("company profits a year")
plt.legend(loc='upper left')
plt.show()
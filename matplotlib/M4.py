name = "My Matplotlib module"

import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("VS project\exercises\company_sales_data.csv")
profit = df['total_profit'].tolist()
months = df['month_number'].tolist()
toothpaste = df["toothpaste"].tolist()

plt.scatter(months, toothpaste, label = 'Tooth paste Sales data')
plt.xlabel('months')
plt.ylabel('profit')
plt.xticks(months)
plt.title("tooth paste sales")
plt.legend(loc='upper left')
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()
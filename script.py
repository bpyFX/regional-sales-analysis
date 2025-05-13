import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("mock_sales.csv")

# Total revenue by region
region_revenue = df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)
print("Total Revenue by Region:")
print(region_revenue)

# Optional: Save plot to file instead of showing
sns.barplot(x=region_revenue.index, y=region_revenue.values)
plt.title("Total Revenue by Region")
plt.ylabel("Revenue ($)")
plt.xlabel("Region")
plt.savefig("revenue_by_region.png")

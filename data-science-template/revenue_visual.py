from calculations import revenue_per_industry
import matplotlib.pyplot as plt

# Get the data for revenue per industry
revenue_data = revenue_per_industry()

# Sort the data by revenue in descending order and select the top 25
top_25_revenue_data = revenue_data.sort_values(ascending=False).head(25)

# Creating the bar graph
plt.figure(figsize=(10, 6))
plt.bar(top_25_revenue_data.index, top_25_revenue_data.values)

plt.title("Revenue for Top 25 Industries (sorted by Revenue)")
plt.xlabel("Industry")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

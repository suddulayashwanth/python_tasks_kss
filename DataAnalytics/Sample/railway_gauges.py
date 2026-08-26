import pandas as pd
from matplotlib import pyplot as plt

#Load CSV file
df =  pd.read_csv('Sample/railway_gauges.csv')
print(df.head())

df.iloc[[df['Total'].idxmax()]]


# Plot data using bar chart
df = df.drop('Total', axis=1)
ax = df.plot(x="Year", kind="bar")
plt.xticks (rotation=70)
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Gauges: Number of railway tracks installed per year')
plt.savefig('rail_gauges.png')
plt.show()

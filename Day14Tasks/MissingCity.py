import pandas as pd

cities = pd.Series({"Delhi": 2000000, "Mumbai": 3000000,"Chennai": 1500000})

required_cities = ["Delhi","Chennai","Bangalore"]

result = cities.reindex(required_cities)

missing_cities = result.index[result.isna()].tolist()
print(result)
print("Missing cities:", missing_cities)
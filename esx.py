import pandas as pd
import numpy as np
data = pd.read_csv("C:\\Users\\rayiv\\Downloads\\ecommerce_customers_unit1.csv")
print(data)
data = data.isnull()
data["age"] = data["age"].fillna(data["age"].mean())
print(data)
print(data.head(20))
print(data.info())

data = data.drop_duplicates()
print(data.isnull().sum())
data = data.fillna(data.mode().iloc[0])
print(data.isnull().sum())
data.to_csv(index=False)


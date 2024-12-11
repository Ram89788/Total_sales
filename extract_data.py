import pandas as pd

# Read data from a CSV file
data = pd.read_csv('sales_data.csv')
print("Data extracted successfully!")
data.to_csv('extracted_data.csv', index=False)

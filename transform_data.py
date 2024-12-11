import pandas as pd

# Read the extracted data
data = pd.read_csv('extracted_data.csv')

# Perform some transformation (e.g., adding a new column)
data['Total_Sales'] = data['Quantity'] * data['Price']

# Save the transformed data
data.to_csv('transformed_data.csv', index=False)
print("Data transformed successfully!")

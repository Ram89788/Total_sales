import pandas as pd

# Read the transformed data
data = pd.read_csv('transformed_data.csv')

# Display the data in the Jenkins console output
print(data)

# Alternatively, save the data to a file that can be accessed from the Jenkins console
data.to_csv('report.csv', index=False)
print("Data saved to report.csv!")


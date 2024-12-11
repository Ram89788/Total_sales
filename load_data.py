import pandas as pd
from sqlalchemy import create_engine

# Read the transformed data
data = pd.read_csv('transformed_data.csv')

# Save data into a MySQL database
engine = create_engine('mysql+pymysql://user:password@localhost/sales_db')
data.to_sql('sales_summary', con=engine, if_exists='replace', index=False)
print("Data loaded successfully!")

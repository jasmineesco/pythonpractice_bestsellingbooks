import pandas as pd

df = pd.read_csv('C:/Users/internproddev/Documents/[JE] SQL + Python Practice/bestsellingbooks/bestsellers with categories.csv')

# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
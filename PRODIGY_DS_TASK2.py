import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file
data = pd.read_csv('test.csv')

# View the first few rows of the dataset
print(data.head(10))

# Get the column names
column_names = data.columns.tolist()
print("Column Names:", column_names)


#data cleaning or data pre-processing
# print("Missing values before cleaning:")
# print(data.isnull().sum())

# Drop rows with missing values
data.dropna(inplace=True)

print("Missing values after cleaning:")
print(data.isnull().sum())

# Handle duplicates
print("Duplicate rows before cleaning:")
print(data.duplicated().sum())

# Drop duplicate rows
data.drop_duplicates(inplace=True)

print("Duplicate rows after cleaning:")
print(data.duplicated().sum())


print(data.head(10))

# Histogram of Age
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


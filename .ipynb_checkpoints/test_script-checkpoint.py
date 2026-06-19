import pandas as pd

file = pd.read_csv('employee.csv')


df = pd.DataFrame(file)
print(df.head())

data = {"Student Name":["Cao","Victoria","Yeng","Luke","Heeso"],"Student ID":[100,101,102,103,104], }
print(pd.DataFrame(pd.read_csv('titanic.csv')).describe())
print(pd.DataFrame(pd.read_csv('titanic.csv')).info())


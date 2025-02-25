#Plotting Graphics with Matplotlib
#By:   Silvana Paredes
#Date: 24/02/2025

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Open the file, which should be in the same directory:
excel_file = 'Canada.xlsx'

df_can = pd.read_excel(
    excel_file,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data downloaded and read into a dataframe!')

df_can.head()
df_can.tail()

#Print a short summary of the dataframe:
df_can.info(verbose=False)

df_can.columns
df_can.index
print(type(df_can.columns))
print(type(df_can.index))

#To get the index and columns as lists:
df_can.columns.tolist()
df_can.index.tolist()
print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))

#To view the dimensions of the dataframe, we use the shape instance variable of it:
df_can.shape

#Drop columns: clean the data set to remove a few unnecessary columns:
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

#Rename columns so that they make sense, by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

#Add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1, numeric_only=True)
df_can.isnull().sum()

#Print a quick summary of each column in our dataframe:
print(df_can.describe())

#Print the dataframe
print(df_can.to_string())

#Filter on column names:
print("\nPrint specific column names after filtering:")
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

#Filter on rows:
print("\nPrint Ecuador's information:")
df_can.set_index('Country', inplace=True)
print(df_can.loc['Ecuador'])

#Filter on row number:
print("\nPrint when the index is 0:")
print(df_can.iloc[0])

#Filter on row and column
print("\nPrint when the country is Japan and the year is 2013:")
print(df_can.loc['Japan', 2013])

#Filter on row and columns
print("\nPrint when the country is Japan and the years are between 1981 and 1984:")
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984]])

#Filter on a based criteria
print("\nPrint the countries in Asia:")
condition = df_can['Continent'] == 'Asia'
print(condition)

#Print Haiti's information
print("\nPrint Haiti's information:")
#years = list(map(str, range(1980, 2014)))
years = list(range(1980, 2014))
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

#First graphic
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='line')
plt.show()

#Second graphic
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. Syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show() 













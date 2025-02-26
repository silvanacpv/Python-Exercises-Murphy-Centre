#Plotting Graphics with Matplotlib:
#1. Area Plot
#2. Histogram
#3. Bar Chart
#4. Horizontal Bar Chart
#5. Pie Chart
#6. Box Plot
#7. Scatter Plot
#By:   Silvana Paredes
#Date: 25/02/2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Open the file, which should be in the same directory:
excel_file = 'Canada.xlsx'

df_can = pd.read_excel(
    excel_file,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data downloaded and read into a dataframe!')

#Drop columns: clean the data set to remove a few unnecessary columns:
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#Rename columns so that they make sense, by passing in a dictionary of old and new names as follows:
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

#Add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
df_can['Total'] = df_can.sum(axis=1, numeric_only=True)

#Set index
df_can.set_index('Country', inplace=True)

#Print Haiti's information
years = list(range(1980, 2014))
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column

#First graphic: Area Plots
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='line')
plt.show()

#Second graphic: Histogram
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='hist')
plt.show()

#Third graphic: Bar Chart
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='bar')
plt.show()

#Fourth graphic: Horizontal Bar Chart
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='barh')
plt.show()

#Fifth graphic: Pie Chart
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='pie')
plt.show()

#Sixth graphic: Box Plot
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
haiti.plot(kind='box')
plt.show()

#Seventh graphic: Scatter Plot
#Convert Haiti in a DataFrame for scatter plot
haiti_df = haiti.reset_index()
haiti_df.columns = ['Year', 'Total']  # Rename columns

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(haiti_df['Year'], haiti_df['Total'], color='darkblue')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()




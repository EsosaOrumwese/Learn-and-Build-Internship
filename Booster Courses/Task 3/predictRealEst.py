'''
The market historical data set of real estate valuation are collected from Sindian Dist., 
New Taipei City, Taiwan.

The inputs are as follows
- TransactionDate = the transaction date (for example, 2013.250=2013 March, 
                    2013.500=2013 June, etc.)
- HouseAge = the house age (unit: year)
- Dist to Nearest MRT Station = the distance to the nearest MRT (Mass Rapid Transit) station 
                                (unit: meter)
- No of Convenience Stores = the number of convenience stores in the 
                             living circle on foot (integer)
- Latitude = the geographic coordinate, latitude. (unit: degree)
- Longitude = the geographic coordinate, longitude. (unit: degree)

The output is as follow
- House Price of Unit Area = house price of unit area (10000 New Taiwan Dollar/Ping, 
                             where Ping is a local unit, 
1 Ping = 3.3 meter squared)
'''

def fitModel():
      '''
      Fits the model based on historical data and returns the model
      '''
      import pandas as pd
      import numpy as np
      from sklearn.linear_model import LinearRegression
      realEstateVal = pd.read_excel("realEstateVal.xlsx")
      
      ## Renaming Columns
      colNames = ['No', 'TransactionDate', 'HouseAge', 'Dist to Nearest MRT Station',
                  'No of Convenience Stores', 'Latitude', 'Longitude', 
                  'House Price of Unit Area']
      realEstateVal.columns = colNames
      
      # deleting 'No' column since is not needed
      del realEstateVal['No']
      
      # creating input and targets
      input_cols = ['TransactionDate', 'HouseAge', 'Dist to Nearest MRT Station', 
                    'No of Convenience Stores', 'Latitude', 'Longitude']
      inputs = realEstateVal[input_cols]
      target = realEstateVal['House Price of Unit Area']
      
      # create and fit model
      model = LinearRegression()
      model.fit(inputs, target)
      
      return model


def realEstateVal():
      '''
      Get the real estate valuation of properties in Sindian Dist., New Taipei City, Taiwan.
      '''
      print('''
            Time to predict the evaluation of real estates in Sindian district, Taiwan.
            ''')
      # collecting arguments
      year = int(input("Enter the year of Transaction: "))
      month = int(input("Enter the month number of transaction (Ex. March = 2): "))
      transactionDate = year + month/12
      houseAge = float(input('Enter House age in years: '))
      distMRT = float(input("What is the distance to the nearest MRT Station (meters)? "))
      noOfStores = int(input("How many stores are around the property? "))
      latitude = float(input("What is its latitude? "))
      longitude = float(input("What is its longitude? "))
      
      # generating prediction
      predictors = [transactionDate, houseAge, distMRT, noOfStores, latitude, longitude]
      model = fitModel()
      prediction = model.predict([predictors])
      print()
      print(f'the value of the house is {prediction[0]:.2f} per unit area'\
             ' (10000 New Taiwan Dollar/Ping)')
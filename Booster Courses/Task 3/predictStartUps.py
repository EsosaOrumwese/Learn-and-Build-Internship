'''
The data is based on records gotten 50 startups from 3 states.

The inputs are as follows 
 0   R&D Spend       : Research and Development expenses
 1   Administration  : Administration expenses
 2   Marketing Spend : Marketing expenses
 3   State           : State in the US. 
 4   Profit          : Profit made by each startup

'''

def fitModel():
      '''
      Fits the model based on historical data and returns the model
      '''
      import pandas as pd
      import numpy as np
      from sklearn.linear_model import LinearRegression
      from sklearn.preprocessing import OneHotEncoder
      startUp = pd.read_csv("50_startups.csv")
      
      ## one hot encoding for the `State` column
      enc = OneHotEncoder()
      enc.fit(startUp[['State']])
      one_hot = enc.transform(startUp[['State']]).toarray()
      startUp[enc.categories_[0]] = one_hot
      
      # create inputs and target
      input_cols = ['R&D Spend', 'Administration', 'Marketing Spend',
                    'California', 'Florida', 'New York']
      inputs = startUp[input_cols]
      target = startUp['Profit']

      # create and train the model
      model = LinearRegression()
      model.fit(inputs, target)
      
      return model


def startUpEval():
      '''
      Get the expected profit of a start up based on some variables.
      '''
      print('''
            Time to predict the profit of your startup.
            ''')
      # collecting arguments
      RDspend = float(input("What is the R&D expense? "))
      admin = float(input("What is the Administration expense? "))
      marketing = float(input("What is the Marketing expense? "))
      state = input("What state is the startup in? [California / Florida / New York] ")
      state = state.lower()
      # converting state into one hot encoded variables
      california, florida, newyork = 0,0,0
      if state == "california":
            california = 1
      elif state == "florida":
            florida = 1
      elif state == "new york":
            newyork = 1
      else:
            print("Invalid state added")
            return
      
      # generating prediction
      predictors = [RDspend, admin, marketing, california, florida, newyork]
      model = fitModel()
      prediction = model.predict([predictors])
      print()
      print(f'This startup is expected to make a profit of ${prediction[0]:.2f}')

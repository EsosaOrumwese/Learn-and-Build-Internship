'''
For predicting the medical charges of patients in a hospital based on age, 
bmi, sex, smoker/non smoker,
number of children and region in the US
'''

def fitModel():
      '''
      Fits the model based on historical data and returns the model
      '''
      import pandas as pd
      import numpy as np
      from sklearn.linear_model import LinearRegression
      from sklearn.preprocessing import OneHotEncoder
      medicalCharges = pd.read_csv("medicalcharges.csv")
      
      # converting categorical data into 1s and 0s
      sex_codes = {'female':0,'male':1}
      smoker_codes = {'yes':1, 'no':0}
      medicalCharges['sex_code'] = medicalCharges.sex.map(sex_codes)
      medicalCharges['smoker_code'] = medicalCharges.smoker.map(smoker_codes)
      
      # one hot encoding the region column
      enc = OneHotEncoder()
      enc.fit(medicalCharges[['region']])
      one_hot = enc.transform(medicalCharges[['region']]).toarray()
      medicalCharges[enc.categories_[0]] = one_hot
      
      # Create inputs and target
      input_cols = ['age', 'bmi', 'children', 'sex_code','smoker_code', 
                    'northeast', 'northwest', 'southeast','southwest']
      inputs = medicalCharges[input_cols]
      target = medicalCharges.charges

      # create and train the model
      model = LinearRegression()
      model.fit(inputs, target)
      
      return model


def medicalChargesCalc():
      '''
      Get how much a customer will pay as a premium each year
      '''
      print('''
            Time to predict your annual medical charge.
            ''')
      
      # collecting arguments
      age = int(input("Enter your age: "))
      bmi = float(input('Enter your BMI (Body Mass Index): '))
      children = int(input("How many children do you have? "))
      smoker = input("Are you a smoker? [Yes/No] ")
      smoker = smoker.lower()
      if smoker == "yes":     # to find the smoker_code based on response
            smoker_code = 1
      else:
            smoker_code = 0
      
      sex = input("What is your gender [Male/Female]? ")
      sex = sex.lower()
      if sex == "male":     # to find the sex code based on response
            sex_code = 1
      else:
            sex_code = 0
      region = input("What region are you from? NorthEast or NorthWest"\
                     " or SouthEast or SouthWest? ")
      region = region.lower()
      northeast, northwest, southeast, southwest = 0,0,0,0
      if region == "northeast":
            northeast = 1
      elif region == "northwest":
            northwest = 1
      elif region == "southeast":
            southeast = 1
      else:
            southwest = 1
      
      # generating prediction
      predictors = [age, bmi, children, smoker_code, sex_code, 
                    northeast, northwest, southeast, southwest]
      model = fitModel()
      prediction = model.predict([predictors])
      print()
      print(f'Your expected medical charge is ${prediction[0]:.2f} per year')

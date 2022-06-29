'''
Module for downloading the data for the prediction app
'''

def downloadData():
      '''
      This function downloads the real estate, medical charges and startup data for the 
      prediction app
      '''
      from urllib.request import urlretrieve
      
      # real estate data
      url_realEstate = "https://archive.ics.uci.edu/ml/machine-learning-databases/00477/"\
                        "Real%20estate%20valuation%20data%20set.xlsx"
      urlretrieve(url_realEstate, "realEstateVal.xlsx")
      
      # medical charges data
      url_medical = "https://raw.githubusercontent.com/JovianML/opendatasets/"\
                    "master/data/medical-charges.csv"
      urlretrieve(url_medical, "medicalcharges.csv")
      
      # startups data
      url_startup = "https://gist.githubusercontent.com/GaneshSparkz/"\
                    "b5662effbdae8746f7f7d8ed70c42b2d/raw/"\
                    "faf8b1a0d58e251f48a647d3881e7a960c3f0925/50_Startups.csv"
      urlretrieve(url_startup, "50_startups.csv")
      
      print("Done!!")
      
      return

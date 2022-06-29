print("-----"*10)
print("\t\tPrediction App")
print("-----"*10)

i = 1
while i == 1:
      # printing options
      print('''
      Choose your option. Remember to dowonload data
      [1]   Download the required data
      [2]   Predict Real Estate values of properties in Taiwan
      [3]   Predict Medical Charges of patients at Bowen hospital
      [4]   Predict profit of startups in the US 
      ''')

      userOpt = int(input("What is your option? "))
      if userOpt == 1:
            import datadownload
            print("Downloading required data")
            datadownload.downloadData()
      elif userOpt == 2:
            import predictRealEst
            predictRealEst.fitModel()
            predictRealEst.realEstateVal()
            
            cont = input("\nWill you like to continue? [Yes/No]")
            if cont.lower() == 'yes':
                  i = 1
            else:
                  i = 0
      elif userOpt == 3:
            import predictMedical
            predictMedical.fitModel()
            predictMedical.medicalChargesCalc()
            
            cont = input("\nWill you like to continue? [Yes/No]")
            if cont.lower() == 'yes':
                  i = 1
            else:
                  i = 0
      elif userOpt == 4:
            import predictStartUps
            predictStartUps.fitModel()
            predictStartUps.startUpEval()
            
            cont = input("\nWill you like to continue? [Yes/No]")
            if cont.lower() == 'yes':
                  i = 1
            else:
                  i = 0
      else:
            print("Wrong option entered")
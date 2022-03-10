class bmi_cal:

    #def __init__(self, feet, inches, weight):  
        #self.feet = feet  
        #self.inches = inches
        #self.weight = weight  

    def calculate_bmi(person, feet, inches, weight):
        person.feet = feet
        person.inches = inches
        person.weight = weight

        
        if person.feet == 0 and person.inches == 0: 
            s = "Height can't be zero"
            return s
        elif person.feet < 0 or person.inches < 0: 
            s = "Height can't be negative"
            return s
        elif person.feet >= 10:
            return("Height can't be 10 feet or more")
        elif person.inches not in range(0,11):
            return ("Inches value should be in between 0 to 11")
        elif person.weight <= 0:
            return ("Weight can not be zero or negative")
        
        else:
            leng = float(((person.feet*12)+person.inches)*0.025)
            wt = float(person.weight*0.45)
            bmi = float(wt/(leng*leng))
            if bmi <= 0:
                return ("BMI can not be negative or zero. Sorry there must be something wwrong")
            elif bmi < 18.5:
                return ("Your bmi is {} and you are under weight".format(bmi))
            elif bmi >= 18.5 and bmi <=24.9:
                return ("Your bmi is {} and you are normal weight".format(bmi))
            elif bmi >= 24.9 and bmi <=29.9:
                return ("Your bmi is {} and you are over weight".format(bmi))
            elif bmi >= 30:
                return ("Your bmi is {} and you are obese".format(bmi))
from tkinter import Y



class Food:
    def __init__(self,name,cal,grams_protein,grams_carbs,grams_fat):
        self.name = name
        self.calories = cal
        self.protein=grams_protein
        self.carbs=grams_carbs
        self.fat=grams_fat

def calculate_BMI(weight,height):
    sum =   ((weight*703) / (height*height))
    return sum

def calorie_Factor(choice):
    rate = 0
    if choice == 1:
        rate = 1.2
    if choice == 2:
        rate = 1.375
    if choice == 3:
        rate = 1.55
    if choice == 4:
        rate = 1.725
    if choice == 5:
        rate = 1.9
        
    return rate

def bmi_category_calculator(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi <= 24.9:
        return "Normal Weight"
    if bmi <= 29.9:
        return "Overweight"
    if bmi >= 30:
        return "Obese"
    
def calculate_BMR(weight,totalInches,age,isMale):
    if(isMale):
        sum = 66.47 + (6.24 * weight) + (12.7 * totalInches) - (6.75 * age)
    else:
        sum = 65.51 + (4.35 * weight) + (4.7 * totalInches) - (4.7 * age)
    
    return sum
    
    
        
        
def main():
    mylist = []
    
    print("Calculate Daily Calories:")
    weight = int(input("What is your weight in pounds? "))
    heightFeet = int(input("What is your height in feet? "))
    heightInches = int(input("What is your height in inches? "))
    totalInches = (12*heightFeet) + heightInches
    age = int(input("What is your age? "))
    male_female = (input("Are you a Male or Female? "))
    isMale = False
    if(male_female == "male" or male_female == "Male"):
          isMale = True
          
    print("")
    print("How many times do you excersise per week?")
    print("1. Little/no excerise (sedentary lifestyle)")
    print("2. Little excerise (1-2 times a week)")
    print("3. Moderate Excerise (3-5 times a week)")
    print("4. Physical Job or Hard Excerise (6-7 times a week)")
    print("5. Professinal Athelte")
    choice = int(input("Choice: "))
    rate = calorie_Factor(choice)
    
    print("")
    
          
    bmi = calculate_BMI(weight,totalInches)
    bmi_category = bmi_category_calculator(bmi)
    print(f"Your BMI is {bmi}")
    print("You are in the " + bmi_category + " category")
    bmr = calculate_BMR(weight,totalInches,age,isMale)
    print(f"The minimum number of calories that your body needs is {int(bmr)}")
    totalIntake = (rate*bmr)
    print(f"Daily Calorie Intake should be {int(totalIntake)}")
    print("")
    
    
    repeat = input("Would you like to enter in Food?(y/n)")
    while repeat != "n":
        name = input("Food Name:")
        cal = int(input("Calories:"))
        protein = int(input("Protein(Grams): "))
        carbs = int(input("Carbs(Grams):"))
        fat = int(input("Fat(Grams)):"))
        mylist.append(Food(name,cal,protein,carbs,fat))
        repeat = input("Would you like to enter in additonal Food?(y/n)")
    

    i = 0
    calories_remaining = totalIntake
    while i < len(mylist):
        a = mylist[i]
        calories_remaining = calories_remaining - a.calories
        protein = a.protein + protein
        carbs = a.carbs + carbs
        fat = a.fat + fat
        
        
        

        
        
        i+=1
    total_grams = protein + carbs + fat
    protein_percentage = protein / total_grams
    carb_percentage = carbs/ total_grams
    fat_percentage = fat/ total_grams
    
    
    print(f"Calories Left: {int(calories_remaining)}")
    print(f"Percent of Protein in Diet: {int(protein_percentage *100)}%")
    print(f"Percent of Carbohydrates in Diet: {int(carb_percentage*100)}%")
    print(f"Percent of Fats in Diet: {int(fat_percentage*100)}%")
    


main()
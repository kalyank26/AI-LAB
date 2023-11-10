def age_criteria(age):
    if (age<2):
        print("infants")
    elif (age<12):
        print("kids")
    elif (age<20):
        print("teens")
    elif (age<59):
        print("senior citizens") 

age=int(input("enter the age\n"))
age_criteria(age)             

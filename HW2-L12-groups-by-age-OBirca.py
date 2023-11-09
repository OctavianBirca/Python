# 1-3 ani - "baby"
# 4-9 ani - "kid"
# 10-15 ani - "teen"
# 16-18 ani - "young"
# 19-50 ani - "adult"
# 51+ ani - "old"


import datetime

current_year = datetime.datetime.now().year #importing current year
#print(current_year)


print("\n")

print("  === GYM for ALL === \n")

student_year = int(input('Enter your year of birth:')) #input birth year of the gym student
student_age = current_year - student_year # student age calculator

print("\n")

### year or years 
if student_age == 1:
     years = "year"
else: 
     years = "years"


print (f"The student is {student_age} {years} old")

### group determinator ###

     ### the student must be born between 1900 and the last year 
if student_age >= 124 or student_age <= 0: 
    print("Sorry, the enetered year must be wrong")

    ### 1-3 ani - "baby" 
elif student_age  >= 1 and  student_age  <= 3:
        print("He/She is the BabyGym Group, on Monday}" )

    ### 4-9 ani - "kid"
elif student_age  >= 4 and  student_age  <= 9:
    print("He/She is the KinnderGym Group, on Tuesday}" )

    ###  "10-15 ani - "teen"
elif student_age  >= 10 and  student_age  <= 15:
    print("He/She is the TeenGym Group, on Wenesdays}" )

    ### 16-18 ani - "young"
elif student_age  >= 16 and  student_age  <= 18:
    print("He/She is the YoungGym Group, on Thursdays}" )

    ### 19-50 ani - "adult"
elif student_age  >= 19 and  student_age  <= 50:
    print("He/She is the AdultGym Group, on Fridays}" )

    ### 51+ ani - "old"
elif student_age  >= 51 and  student_age  <= 123:
    print("He/She is the YoungGym Group, on Saturdays}" )
   
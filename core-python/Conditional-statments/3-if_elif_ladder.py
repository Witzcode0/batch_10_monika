# syntax: 

# if(condition-1):
#     block of code
# elif (conditition-2):
#     block of code
# elif (condition-3):
#     block of code
#     ...
# else:
#     block of code

score = float(input("Enter your score : "))
if (score <= 100 and score >= 0):
    if(score >= 80):
        print("First class")
    elif (score >= 60):
        print("Second class")
    elif (score >= 40):
        print("Third class")
    else:
        print("Sorry, you are failed")
else:
    print("Invalid score")
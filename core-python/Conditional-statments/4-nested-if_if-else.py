age = int(input("Enter age: "))

if(age >= 18):
    weight = float(input("Enter weight : "))
    if(weight >= 50):
        print("you can donate")
    else:
        print("You can not donate")
else:
    print("You can not donate")
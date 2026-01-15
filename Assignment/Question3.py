#Use of for loop 
age = int(input("Enter your age: "))
name = input("Enter your name: ")
study_class = int(input("Enter your class: "))
district = input("Enter your district name: ")

if age < 18:
    print("You are under age. Please go away!")

else:
    if study_class < 10:
        print("Please complete 10th class first")
    else:
        if district == "Bhaktapur":
            print("You are eligible for voting. Go vote!")
        else:
            print("You are not eligible for voting (district issue)")




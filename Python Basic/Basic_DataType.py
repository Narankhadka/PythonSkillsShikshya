#Basic data type

age=21.                #int
height = 5.9            #float
name = "Naran Khadka"    #string
is_student = True       #boolean


#control structure

if age >= 18:
    print( "adult.")
elif age==18:
    print("just become adult.")
else:
    print(" minor.")


    # for loop
for i in range(5): 
    print(f"Number: {i}")


   # while_loop

    count = 0
while count < 3:
    print("counting:", count)
    count += 1


    #function
    def greet(name):
        return f"Hello, {name}!"
    

#function call 
    print(greet("Naran"))


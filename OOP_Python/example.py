def my_function(x):
    print("4")
    print("the number is =",x)



def my_decorator(some_function,num):
    def wrapper(num):
        print("1")
        print("Inside wrapper to check odd/even")
        if num%2 == 0:
            print("2")
            ret="Even"

        else: 
            print("3")
            ret="Even"
        
        some_function(num)
        print("5")
        return ret
    print("wrapper function is called")
    return wrapper


num=10
my_function = my_decorator(my_function,num)
# print("It is ",my_function(num))
print("it is ",my_function(num))
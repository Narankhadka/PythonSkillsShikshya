
def testReference(arg):
    print("ID inside the function is : " , id(arg))
    arg=arg+1
    print("New object after increment",arg, id(arg))

var=10
#var="Hi Naran how are you doing"
print("Id Before Passing: ",id(var))
testReference(var)
print("Value after function call",var)

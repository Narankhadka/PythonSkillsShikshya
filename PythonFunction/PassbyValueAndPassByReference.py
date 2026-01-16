
def testReference(arg):
    print("ID inside the function is : " , id(arg))


var="Hi Naran how are you doing"
print("Id Before Passing: ",id(var))
testReference(var)

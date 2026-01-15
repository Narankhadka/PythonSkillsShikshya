#check the given numeber is palindrome or not 

number = int(input("Enter a number to check palindrome or not: "))

q = number
result = 0

while q != 0:
    remainder = q % 10
    result = result * 10 + remainder
    q = q // 10

if result == number:
    print("Yes, it is palindrome number")
else:
    print("It is not palindrome number")

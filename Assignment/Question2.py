#check if anagram or not

def check_anagram(s,t):

    if len(s)!=len(t):
        return False

    result = ''.join(sorted(s))
    result1 = ''.join(sorted(t))
    if result==result1:
        return True
    else:
        return False
    
first_string="anagram"
second_string="nagrama"
r=check_anagram(first_string,second_string)
if r==True:
    print("Yes anagarm")
else:
    print("No")



    
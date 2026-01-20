


from collections import defaultdict


d=defaultdict(int)

d["a"] +=1
print(d)


d=defaultdict(list)

d["b"].append(1)
print(d)

#using a custom function as the default factory 

def default_value():
    return "N/A"
    

    
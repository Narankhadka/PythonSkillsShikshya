original_dict={"name":"Alice","age":25,"skills":["python","data Science"]}
shallow_copy = original_dict.copy()

#Modifying the shallow copy 

shallow_copy["age"]= 26 
shallow_copy["skills"].append("Machine Learning")

print("Original dictionary:", original_dict)
print("shallow copy:",shallow_copy)

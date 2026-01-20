#Define an empty outer dictionary 
nested_dict ={}

#add key-value pairs to the outer dictionary 

outer_key = ["outer_key1" , "outer_key2"]
for key in outer_key:
    nested_dict[key] = {"inner_key1":"value1","inner_key2":"values2"}

print(nested_dict)



student_info={
    "name": "Alice",
    "age": 21, 
    "major": "Computer Science"

}

all_keys=student_info.keys()
all_values=student_info.values()
print("Keys:", all_keys)
print("Values",all_values)

# using the items() method to get key-value paris
all_items=student_info.items()
print("Items",all_items)

#Itereting through the key value pairs
print("Iterating through key-value pairs")
for key, value in all_items:
    print(f"{key}: {value}")
#orginal tuple
T1=(10,20,30,40)
#converting the tuple to a list
list_T1=list(T1)
update_list = [item + 100 for item in list_T1]

updated_tuple = tuple(update_list)
print("Original tuple",T1)
print("Updated Tuple:", updated_tuple)
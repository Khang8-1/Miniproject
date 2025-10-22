
my_list = [2, 4, 6, 8, 10, 12]
print(my_list)
my_list.append(14)
print(my_list)

# 3. Report the length of the list
list_length = len(my_list)
print(f"The length of my list is: {list_length}")
element_at_2 = my_list[2]
print(f"The element at index 2 is: {element_at_2}")
my_list.insert(2, 100)
print(my_list)
element_at_2_after_insert = my_list[2]
print(f"The element at index 2 is: {element_at_2_after_insert}")
del my_list[1]
print(my_list)
element_at_2_after_remove = my_list[2]
print(f"The element at index 2 is: {element_at_2_after_remove}")
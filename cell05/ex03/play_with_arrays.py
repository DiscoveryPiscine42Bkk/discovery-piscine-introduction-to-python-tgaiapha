original_array = [2, 8, 9, 48, 8, -12, 2]
print(original_array)
new_set = (x + 2 for x in original_array if x > 5)
print(new_set)

def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers

# Input and output examples
list1 = [22, -7, -12, 25, -14]
list2 = [12, -14, 95, -3]

output1 = print_positive_numbers(list1)
output2 = print_positive_numbers(list2)

print("Input:", list1, "Output:", output1)
print("Input:", list2, "Output:", output2)




 

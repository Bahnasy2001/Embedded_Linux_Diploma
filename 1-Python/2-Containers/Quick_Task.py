#Find the largest item from a given list using loop
def find_largest_num(input_list):
	# Check if the list is empty
	if not input_list:
		return None      # Return None if the list is empty
		# Initialize the maximum value with the first item of the list

	max_num = input_list[0]

		# Iterate through the list starting from the second item
	for num in input_list[1:]:
		# Compare each item with the current maximum value
		if num > max_num:
			max_num = num # Update the maximum value if a larger item is found

	return max_num  # Return the maximum value


my_list = [10,5,20,8,15]
largest_number = find_largest_num(my_list)
print("The largest num in the list is : ",largest_number)
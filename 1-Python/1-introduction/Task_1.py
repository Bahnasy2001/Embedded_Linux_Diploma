#Write a Python program to count the number 4 in a given list.

my_list = [1,4,5,6,7,4]

count = 0

for x in my_list:
	if x == 4:
		count += 1
	else:
		pass

print(count)
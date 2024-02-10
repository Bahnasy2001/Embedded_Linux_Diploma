#Write a Python program to test whether a passed letter is a vowel or not.

vowel = ['a','e','i','o','u']

x = input("Enter a Character:")


if x.lower() in vowel:
	print(f"{x} is vowel")
else:
	print(f"{x} is not vowel")
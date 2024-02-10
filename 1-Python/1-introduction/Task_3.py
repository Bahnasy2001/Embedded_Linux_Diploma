import os

# Get a specific environment variable
username = os.getenv('USERNAME')
print(f'Username: {username}')

# Get all environment variables
all_env_vars = os.environ
print('All Environment Variables: ')
for key,value in all_env_vars.items():
	print(f"{key} : {value}")

#We use the os.getenv() function to retrieve the value of a specific environment variable (USERNAME in this case).
#We use os.environ to get a dictionary containing all environment variables,then iterate over it and print each variable along with its value.
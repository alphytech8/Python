# Prompt the user to enter the names
names = input("Enter the names, separated by commas: ")

# Split the input string into a list of names
names_list = names.split(",")

# Remove leading and trailing whitespace from each name
names_list = [name.strip() for name in names_list]

# Sort the list of names in alphabetical order
names_list.sort()

# Remove duplicates from the list of names
names_list = list(set(names_list))

# Print the final list of names
print("Final list:")
for name in names_list:
    print(name)

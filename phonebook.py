

# load phonebook from file
f = open('phonebook.txt', 'r')
lines = f.readlines()
f.close()

# number of entries in the phonebook
print("The phone book currently has " + str(len(lines) / 2) + " entries!");

# show phone book entries
# for i in range(0, len(lines), 2):
#	print("Name: " + lines[i])
#	print("Phone number: " + lines[i+1])
# alternatively: i = 0
# while i < count: 
# i = i + 2;

# search phone number by name
new_search_name = input("Enter a name to search for: ");
# for v in lines:
for i in range(0, len(lines), 2):
	if (lines[i] == new_search_name.strip("\n")):
		print("Found name in phone book! The phone number is " + lines[i+1])
	else:
		print("Name does not exist in phone book!")

# insert phone number
new_name = input("Please add an entry now! Name to add: ");

lines.append(new_name+"\n")

new_phone_number = input("Phone number to add: ");

lines.append(new_phone_number+"\n")

# save phonebook into a file
g = open("phonebook.txt", "w")
for v in lines:
	g.write(v)
g.close()

print("Entry added! Phone book has " + str(len(lines) / 2) + " entries now!");
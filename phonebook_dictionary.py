phone_book = {}
file_name = "phonebook2.txt"

# load phonebook from file
f = open(file_name, 'r')
lines = f.readlines()
f.close()

# parse entries into dictionary
for i in lines:
	phone_book[i.split(":::")[0]] = i.split(":::")[1].strip('\n');

# number of entries in the phone book
print("The phone book currently has " + str(len(phone_book.keys())) + " entries!");

new_search_name = input("Enter a name to search for: ");
# for v in lines:
if new_search_name in phone_book:
	print("Found name in phone book! The phone number is " + phone_book[new_search_name])
else:
	print("Name does not exist in phone book!")

# insert phone number
new_name = input("Please add an entry now! Name to add: ");
new_phone_number = input("Phone number to add: ");

phone_book[new_name] = new_phone_number


# save phone book into file
lines = ""
g = open(file_name, "a") # append
g.write(new_name + ":::" + new_phone_number + "\n")
g.close()

print("Entry added! Phone book has " + str(len(phone_book.keys())) + " entries now!");


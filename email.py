"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

#This is equal to the email addresses entered
addresses = []
#This is a prompt for a user to answer if they have an email address to enter or not
more = input("Do you have an email address to enter (y/n)? ")
#If the user selected Yes, or Y, they must now enter an email address, then once an address is entered they have the option to enter a secondary address if they so choose. If no, then they do not enter an address.
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
    
print(addresses)
#^ This command prints the entered addresses.
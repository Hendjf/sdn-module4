"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


addresses = []
#This is prompting the user for information, specifically if they have an email or not
more = input("Do you have an email address to enter (y/n)? ")

#This is prompting the user to enter a string of additional email address, it appears as though it would create some kind of table
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")

#This command prints the addresses in said table    
print(addresses)

"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

##appears to be creating a list of addresses using addresses = input
addresses = []

##assigns the value yes/no to more
more = input("Do you have an email address to enter (y/n)? ")

##creating a loop, while "yes" is true, a new email address will be added until the loop hits "n"
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")

##prints the list of addresses that was fed into the list    
print(addresses)

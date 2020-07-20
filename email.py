"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

#Creates addresses variable
addresses = []

more = input("Do you have an email address to enter (y/n)? ")
#While loop that takes the y/n input and either asks you to enter the address and ask for another or break the loop if n
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#print addresses   
print(addresses)

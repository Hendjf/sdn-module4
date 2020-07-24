"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


addresses = []
#code above is where the recorded addresses are displayed showing which are current
more = input("Do you have an email address to enter (y/n)? ")
#prompts user to confirm whether or not an address needs to be added
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#this portion of code allows yuo to add more than one email if there are multiple to add
print(addresses)
#this displays the updated list of addresses

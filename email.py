"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

# creates list named addresses, it's size is not defined
addresses = []
# user prompt and input saved in more value
more = input("Do you have an email address to enter (y/n)? ")
# while loop should keep going when Y is input
while more == "y": #compare user prompt saved in more variable with "y" is true the contents are ran
    email = input("Enter the address: ") #user prompt for address, value save in email variable
    addresses.append(email) #email value is added to addresses list
    more = input("Do you have another address(y/n)? ") #user prompt, value saved in more variable
    while more != "y": #compare more value to "y", true with more is not equal to "y"
        if more == "n": #compare more value to "n", true is more is equal to "n"
            break# is more equal to "n" break used to end while loop
        else:
            more = input("Please enter a y or n: ")# prmplt used if "y" or "n" not value in more
# addreses list is printed    
print(addresses)

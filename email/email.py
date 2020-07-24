"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

I think the script could be used to sign people up to recieve advertising emails from a company. 

"""

#sets variable addresses
addresses = []
#prompts user to answer if they have an email address
more = input("Do you have an email address to enter (y/n)? ")
#If y(yes) to question, prompts to enter email address
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
 #Prompts question is there another email address
    more = input("Do you have another address(y/n)? ")
    #loop for more email addresses
    while more != "y":
    #if n (no) to any questions end script
        if more == "n":
            break
            #if anything entered besides y or n to questions, it prompts you to only enter y or n
        else:
            more = input("Please enter a y or n: ")
    #prints all email addresses entered by user
print(addresses)

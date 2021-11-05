# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages
def divisible(n):
    if n%7==0 or n%4==0:
        return True
    else:
        return False
def divisible_both(n):
    if n%7==0 and n%4==0:
        return True
    else:
        return False
given_number=input()
divisible_or=divisible(int(given_number))
divisible_and=divisible_both(int(given_number))
print("Is the given number:",int(given_number),"is divisible by 4 OR 7",divisible_or)
print("Is the given number:",int(given_number),"is divisible by 4 AND 7",divisible_and)
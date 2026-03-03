"""
Lab 8: UPC Validator
Author: Ben Garcia
Program that validates user provided 12 digit UPC-A codes,

"""
def find_UPC(upc):
    """Checks if the provided UPC code is valid or not.
    Args:
        upc: A string representing a UPC code."""
    #initialize odd and even sums for algorithm
    sum_odd = 0
    sum_even = 0
    #loop through odd sums and multiply by 3, using range function to skip even numbers
    for i in range(0, 11, 2):
        sum_odd += int(upc[i])
    sum_odd *= 3
    #loop through even sums, using range function to skip odd numbers
    for i in range(1, 11, 2):
        sum_even += int(upc[i])

    total_sum = sum_odd + sum_even

    #calculate check digit (= total sum mod 10, if 0 check digit is 0, otherwise it is 10 - mod 10)
    modulo = total_sum % 10
    if modulo == 0:
        check_digit = 0
    else:
        check_digit = 10 - modulo 
    
    return check_digit


#Main program
print("Welcome to the UPC Validator!\n")
invalid_entry = True
while invalid_entry:
    upc = input("Please enter a 12 digit UPC code to validate: ")

    if(len(upc) != 12 or not upc.isdigit()):
     print("Invalid input. Please enter a 12 digit UPC code.")
    else:
        invalid_entry = False
        print("Validating UPC code...")
        break
check_digit = find_UPC(upc)
#cast the last digit of the UPC code to an integer and compare it to the calculated check digit
if check_digit == int(upc[-1]):
    print("The UPC code is valid.")
else:
    print("The UPC code is invalid.")

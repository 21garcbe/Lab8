"""
Lab 8: UPC Validator
Author: Ben Garcia
Program that validates user provided 12 digit UPC-A codes

"""
def find_UPC(upc):
    """Checks if the provided UPC code is valid or not.
    Args:
        upc: A string representing a UPC code.    

        Algorithm steps:
        1. Sum odd and even digits seperately using range function to iterate over UPC integer
        assign sums seperately to sum_odd, sum_even variables
        2. Multiply sum_odd by 3
        3. Add sum_odd and sum_even together to get total_sum
        4. Calculate check digit by taking total_sum mod 10, 
        if the result is 0 then check digit is 0, otherwise it is 10 - (total_sum mod 10)
        5. Compare the calculated check digit to the last digit of the UPC code (cast to an integer) 
        and print if the UPC code is valid or not.
        """
    print(f"The first 11 digits are: {upc[:-1]}.")
    print(f"\nThe provided check digit is {upc[-1]}")
    print("\nCalculating check digit...")
    sum_odd = 0
    sum_even = 0
    
    for i in range(0, 11, 2):
        sum_odd += int(upc[i])
    sum_odd *= 3
    
    for i in range(1, 11, 2):
        sum_even += int(upc[i])

    total_sum = sum_odd + sum_even

    #calculate check digit 
    modulo = total_sum % 10
    if modulo == 0:
        check_digit = 0
    else:
        check_digit = 10 - modulo 
    print(f"\nThe calculated check digit is {check_digit}.")
    
    #compare provided check digit to the calculated check digit
    if check_digit == int(upc[-1]):
        print("The UPC code is valid.")
    else:
        print("The UPC code is invalid.")



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

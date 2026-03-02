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

    #calculate total sum
    total_sum = sum_odd + sum_even


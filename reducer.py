#!/usr/bin/env python

import sys

# The input will be in the form of key-value pairs
# It is sorted according to the key
# Each key value pair will be in a new line
# The key and the value are seperated by a tab (\t)
# The key is the payment type and the value is the sales
# Example input data (Key=Payment, Value=Sales)
# Input is ordered by the key
# Visa  205.96
# Cash  11.32
# Cash  444.19

# We want to sum all values with the same key
# Example output data (Key=Payment, Value=Sum of Sales)
# Visa  205.96
# Cash  455.51

# Sum of all sales (values) is initialized with zero, we just started
sum_of_values = 0
# Count of values for each category
count = 0
# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # The result is a tuple with 2 elements
    data = line.strip().split("\t")

    # Store the 2 elements of this line in separate variables
    key, value = data

    # Do we have a previous_key (previous_key != None) and 
    # is the new key different than the previous key?
    # This means the line starts with a new key (key changes e.g. from "Visa" to "Cash")
    # Remember that our keys are sorted
    if previous_key is not None and previous_key != key:
        # Then write the result of the old key (Key=category, Value=Average Sales)
        # to the standard output (stdout)
        # Key and value are separated by a tab (\t)
        # Line ends with a new line (\n)
        average_sales = sum_of_values / count if count > 0 else 0
        sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))
        
        # Reset sum of values and count for the new category
        sum_of_values = 0
        count = 0

    # Add the value to the total sales
    # a += b is the same as a = a + b
    # the float function transforms the value
    # to a float data type (like decimal)
    sum_of_values += float(value)
    # Increment the count for each value
    count += 1
    # the previous key for the next iteration is the current key of this iteration 
    previous_key = key

# write the last result to stdout
average_sales = sum_of_values / count if count > 0 else 0
sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))


"""
    You are going to design a magical calculator with the following functions.
    • Function that takes input and calculates it’s factorial. (A)
    • Function that takes input and calculate it’s sum of digits. (B)
    • Function that takes input and find’s the largest digit in the input. (C)
    - Implement all the above functions.
    - Get input and pass the input to factorial function (A), get the output from
    factorial function and pass it as input to sum of digits function (B). Get the output
    from sum of digits function, add the output with random 5 digit number and pass
    the outcome to largest digit function (C) and print the output that you receive from
    function C.
"""
def fact(val):

    if(val == 1):
        return val
    else:
        return val*fact(val-1)

def sum_of_digits(fact_val):

    sum = 0
    while(fact_val != 0):
        sum = sum+int(fact_val%10)
        fact_val = fact_val/10
    return sum

def largest_digit(ld_input):

    initial = list(str(ld_input))
    return max(initial)

val = int(input("Input: "))
fact_val = fact(val)
sod_value = sum_of_digits(fact_val)
ld_input = sod_value+12345
large = int(largest_digit(ld_input))
print(val,"! =",fact_val)
print("Sum of Their Digit:",sod_value)
print("Greatest Digit among them:",large)
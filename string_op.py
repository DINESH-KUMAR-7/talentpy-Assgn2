"""
    Implement String calculator with following functions.
    • Function that reverses the given string S. (A)
    • Function that returns total A’s available (it can be ‘a’ or ‘A’) int given
    string S. (B)
    • Function that takes 2 inputs string S and index and returns element at
    given index. If the index is not available, it should return 0 as the
    output. (C)
    • Function that multiples given string 5 times (D)
    - Implement all the above functions.
    - Get input and pass it to the reverse function, get the output from it and call
    function C, function C takes 2 params, first param should be output from function
    A and second param should be output from function B. Get the output. If the
    output is not 0, call function D and print output. Else call print “Completed without
    multiply” as the output.
"""
def rev(in_put):
    reversed_str = in_put[::-1]
    return reversed_str

def no_of_a(in_put):
    count=0
    for _ in range(len(in_put)):
        if(in_put[_]=='a'or in_put[_]=='A'):
            count = count+1
    return count

def get_the_char(rev_str,index):
    return rev_str[index]

def multi_str(find):
    return find*5


in_put = input("INPUT: ")
rev_str = rev(in_put)
print("Reversed String: ",rev_str)
index = no_of_a(in_put)
find = get_the_char(rev_str,index)
print("Element:",find,"Index:",index)

if(index==0):
    print("Completed without multiply")
else:
    print("MULTIPLE String:",multi_str(find))
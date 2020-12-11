import string


# Write a function that checks whether a number is in a given range (inclusive of high and low
def ran_check(num,low,high):
    return low <= num <= high


# Write a Python function that accepts a string
# and calculates the number of upper case letters and lower case letters.
def up_low(s):
    num_lower = 0
    num_higher = 0
    for letter in s:
        if  letter.isupper():
            num_higher = num_higher+1
        elif letter.islower():
            num_lower = num_lower+1
        else:
            pass

    return "Number of upper case characters: " + str(num_higher) + " Number of lower case characters: " + str(num_lower)


# Write a Python function that takes a list
# and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    num = 1
    for number in numbers:
        num *= number

    return num


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


# Write a Python function to check whether a string
# is pangram or not. (Assume the string passed in does not have any punctuation)
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    str1_set = set(str1)
    alpha_set = set(alphabet)
    return str1_set == alpha_set

if __name__ == '__main__':
    print(ran_check(5,2,7))
    print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
    print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
    print(multiply([1,2,3,-4]))
    print(palindrome('nurses run'))
    print(ispangram("The quick brown fox jumps over the lazy dog"))
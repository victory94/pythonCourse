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
        if letter == " " or letter == "," or letter == '?' or letter == ".":
            continue
        elif letter.isupper():
            num_higher = num_higher+1
        else:
            num_lower = num_lower+1

    return "Number of upper case characters: " + str(num_higher) + " Number of lower case characters: " + str(num_lower)


# Write a Python function that takes a list
# and returns a new list with unique elements of the first list.
def unique_list(lst):
    return [x for x in set(lst)]


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    num = 1
    for number in numbers:
        num = num*number

    return num


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


#Write a Python function to check whether a string
# is pangram or not. (Assume the string passed in does not have any punctuation)
def ispangram(str1, alphabet=string.ascii_lowercase):
    lowercase_string = str1.lower()
    lowercase_no_space = lowercase_string.replace(" ", "")
    is_pangram = True
    for letter in lowercase_no_space:
        if letter in alphabet:
            continue
        else:
            is_pangram = False

    return is_pangram

if __name__ == '__main__':
    print(ran_check(5,2,7))
    print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
    print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
    print(multiply([1,2,3,-4]))
    print(palindrome('helleh'))
    print(ispangram("The quick brown fox jumps over the lazy dog"))
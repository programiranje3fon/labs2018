# Task 1:
# Write a function that receives an integer value (n) and
# generates and prints a dictionary with entries in the
# form x:x*x, where x is a number between 1 and n.

def create_dict(n):
    a_dict = dict()
    for x in range(1, n+1):
        a_dict[x] = x*x
    for key, val in a_dict.items():
        print(f"{key}:{val}")



# Task 2:
# Write a function that receives a string as its input parameter and
# calculates the number of digits and letters in this string.
# The function returns the dictionary with the computed values.

def digiti_letter_counter(a_string):
    dl_dict = {"digits":0, "letters":0}
    for ch in a_string:
        if ch.isdigit():
            dl_dict['digits'] += 1
        elif ch.isalpha():
            dl_dict['letters'] += 1
    return dl_dict



# Task 3:
# Write a function that receives two lists and returns a list that contains
# only those elements (without duplicates) that appear in both input lists.

# Option 1
# def common_elements(l1, l2):
#     common = list()
#     s1 = set(l1)
#     s2 = set(l2)
#     for item in s1:
#         if item in s2:
#             common.append(item)
#     return common


# Option 2
# def common_elements(l1, l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     return list(s1.intersection(s2))


# Option 3
def common_elements(l1, l2):
    return [item for item in set(l1) if item in set(l2)]



# Task 4:
# Write a function that receives two strings and checks if
# the second string when reversed is equal to the first one.
# The comparison should be based on letters and digits only
# (alphanumerics) and should not be case sensitive.
# The function returns appropriate boolean value.

# Option 1
def compare_reversed(str1, str2):
    str1_alnum = list()
    for ch in str1:
        if ch.isalnum(): str1_alnum.append(ch.lower())
    str2_rev_alnum = list()
    for ch in reversed(str2):
        if ch.isalnum(): str2_rev_alnum.append(ch.lower())
    return str1_alnum == str2_rev_alnum

# Option 2
# def compare_reversed(str1, str2):
#     str1 = [ch.lower() for ch in str1 if ch.isalnum()]
#     str2 = [ch.lower() for ch in reversed(str2) if ch.isalnum()]
#     return str1 == str2



# Task 5:
# Write a function that asks the user for a string and prints out
# whether this string is a palindrome or not.

def palindrom():
    an_input = input("Please enter a string to check if it is palindrom:\n")
    an_input = [ch.lower() for ch in an_input if ch != " "]
    input_rev = [ch.lower() for ch in reversed(an_input) if ch != " "]

    response = "palindrom" if an_input == input_rev else "NOT palindrom"
    print(f"Your input is {response}")



# Task 6:
# Write a function to check whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: use ascii_lowercase from the string module to get all letters

from string import ascii_lowercase

# Option 1
# def pangram(a_string):
#     letters = [ch for ch in a_string.lower() if ch.isalpha()]
#     letters = sorted(set(letters))
#     return letters == list(ascii_lowercase)

# Option 2
def pangram(a_string):
    letters = [ch for ch in a_string.lower() if ch.isalpha()]
    return len(set(ascii_lowercase).difference(set(letters))) == 0



# Task 7:
# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is even. The numbers that match this criterion
# should be printed in a comma-separated sequence.

def all_even_digits():
    result = list()
    for num in range(100, 401):
        digits = [int(d) for d in str(num)]
        all_even = True
        for d in digits:
            if d % 2 != 0:
                all_even = False
                break
        if all_even:
            result.append(num)
    print(", ".join([str(num) for num in result]))



# Task 8:
# Write a function that accepts a string input and returns slices of that
# string according to the following rules:
# - if the input string is less than 3 characters long, returns a list
#   with the input string as the only element
# - otherwise, returns a list with all string slices more than 1 character long
# Examples:
# input: 'are'
# result: ['ar', 'are', 're']
# input: 'table'
# result: ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']

def string_slices(a_string):
    if len(a_string) < 3:
        return [a_string]
    result = []
    for i in range(0, (len(a_string)-1)):
        for j in range(i+1, len(a_string)):
            result.append(a_string[i:(j+1)])
    return result




if __name__ == '__main__':

    # create_dict(6)

    # print(digiti_letter_counter("Today is October 14, 2018"))

    # a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 5, 10]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements(a,b))

    # print(compare_reversed("Cat?", "tac!!!"))
    # print(compare_reversed("Hello there!", "hello world!!!"))

    # palindrom()

    # print(pangram("The quick brown fox jumps over the lazy dog"))
    # print(pangram("The quick brown fox jumps over the lazy cat"))

    # all_even_digits()
    print(string_slices('are'))
    print(string_slices('table'))
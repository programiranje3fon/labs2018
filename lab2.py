# Write a function that receives two lists and returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure the function works on
# two lists of different sizes.


def common_elements_with_sets(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    s = s1.intersection(s2)
    return s


def common_elements_lists_only(l1, l2):
    common = [item for item in l1 if item in l2]
    unique = []
    for item in common:
        if item not in unique:
            unique.append(item)
    return unique


# Write a function that asks the user for a string and prints out
# whether this string is a palindrome or not.

def palindrom():
    a_string = input("Please enter a string:\n")
    #JJ: the next (probably too complicated line) can be substituted with:
    # chars = list(a_string)
    # if we assume that the input string does not contain spaces
    chars = [ch for ch in list(a_string) if ch != " "]
    chars_reversed = list(reversed(chars))
    #JJ: note that chars.reverse() could not be used as it reverses
    # the list in-place, that is, modifies the original list (chars)
    if chars == chars_reversed:
        print("This string is a palindrom")
    else:
        print("This string is NOT a palindrom")
    # VD: alternatively:
    # if ''.join(chars_reversed) == a_string:
    #     print("This string is a palindrom")
    # else:
    #     print("This string is NOT a palindrom")


# Write a function to check whether a given string is a pangram or not.
# Pangrams are sentences containing every letter of the alphabet at least once.
# (e.g.: "The quick brown fox jumps over the lazy dog")
#
# Hint: use ascii_lowercase from the string module to get all letters
from string import ascii_lowercase

def pangram(a_string):
    unique_letters = set(a_string.lower())
    # print(unique_letters)
    unique_letters.remove(' ')
    if unique_letters == set(ascii_lowercase):
        print("This string is pangram")
    else:
        print("This string is NOT pangram")


# Write a function that finds numbers between 100 and 400 (both included)
# where each digit of a number is an even number. The numbers obtained
# should be printed in a comma-separated sequence.

def all_even():
    even = []
    for num in range(100, 401):
        digits = list(str(num))
        only_even = True
        for d in digits:
            if int(d) % 2 == 0:
                only_even = False
                break
        if only_even:
            even.append(num)
    print(", ".join([str(e) for e in even]))


# Write a function that accepts a string input and returns slices
# according to the following rules:
# - if the input string is less than 3 characters long, returns a list
#   with the input string as the only element
# - otherwise, returns a list with all string slices more than 1 character long
# Examples:
# input: 'are'
# result: ['ar', 'are', 're']
# input: 'table'
# result: ['ta', 'tab', 'tabl', 'table', 'ab', 'abl', 'able', 'bl', 'ble', 'le']

def slices(a_string):
    str_len = len(a_string)
    if str_len < 3:
        return list(a_string)
    result = []
    for pos, ch in enumerate(a_string):
        for i in range(pos+1, str_len):
            result.append(a_string[pos:i+1])
    return result


if __name__ == '__main__':

    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(common_elements_with_sets(a, b))
    # print(common_elements_lists_only(a, b))

    # palindrom()

    # pangram("The quick brown fox jumps over the lazy dog")
    # pangram("The quick brown fox jumps over the lazy cat")

    # all_even()

    print(slices("table"))
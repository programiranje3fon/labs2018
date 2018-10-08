# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

def odd_or_even():
    num = input("Please enter an integer value:\n")

    # Option 1:
    # if int(num) % 2 == 0:
    #     print("You've entered an EVEN number")
    # else:
    #     print("You've entered an ODD number")

    # Option 2:
    result = 'even' if int(num) % 2 == 0 else 'odd'
    print('This is an', result.upper(), 'number')


# Write a function to calculate the factorial of a number.
# The function accepts the number (a non-negative integer)
# as an argument.

def factorial(num):
    f = 1
    for i in range(num, 1, -1):
        f *= i
    return f



# Write a function that returns nth lowest value of a list
# (or an iterable in general). Return the lowest if n (2nd argument)
# is greater than the number of elements in the iterable.

def nth_lowest(an_iterable, n):
    sorted_iter = sorted(an_iterable)
    if n > len(an_iterable):
        n = 1
    return sorted_iter[n-1]



# Write a function that receives a list of numbers and returns
# a tuple with the following elements:
# - the list element with the smallest absolute value
# - the list element with the largest absolute value
# - the sum of all positive elements in the list
# - the product of all negative elements in the list

def list_stats(a_list):
    sum_pos = 0
    prod_neg = 1
    smallest = largest = abs(a_list[0])
    for num in a_list:
        if abs(num) < smallest:
            smallest = abs(num)
        elif abs(num) > largest:
            largest = abs(num)
        if num > 0:
            sum_pos += num
        elif num < 0:
            prod_neg *= num
    return smallest, largest, sum_pos, prod_neg



# Write a function that receives a list of numbers and a
# threshold value (number). The function:
# - makes a new list that has unique elements from the input list
#   that are less than the given number
# - prints the number of elements in the new list
# - sorts the elements in the list and prints them, an element per line

# Option 1:
# def print_new_list(numbers, threshold):
#     selection = set()
#     for num in numbers:
#         if num < threshold:
#             selection.add(num)
#     print("Number of elements in the new list:", str(len(selection)))
#     selection = list(selection)
#     selection.sort(reverse=True)
#     for num in selection:
#         print(num)

# Option 2:
def print_new_list(a_list, threshold):
    new_list = []
    for item in set(a_list):
        if item < threshold:
            new_list.append(item)
    print(f'The new list has {len(new_list)} elements.')
    for item in sorted(new_list, reverse=True):
        print(item)


# Write a function that receives two strings and checks if they
# are anagrams (assume input consists of alphabets only).
# The function returns appropriate boolean value.

def anagrams(str1, str2):
    str2_rev = list(reversed(str2.lower()))

    # Option 1:
    # return list(str1.lower()) == str2_rev

    # Option 2:
    return ''.join(str1.lower()) == ''.join(str2_rev)


# Write a function that generates and prints a dictionary with entries
# in the form x:x*x, where x is a number between 1 and n

def create_dictionary(n):
    num_dict = dict()
    for x in range(1, n+1):
        num_dict[x] = x*x
    for key, val in num_dict.items():
        print(f"{key}:{val}")



# Write a function that receives a string as its input parameter and 
# calculates the number of digits and letters in this string. 
# The function returns a dictionary with the computed values.

def digits_letters_counter(a_string):
    str_stats = {'letters':0, 'digits':0}
    for ch in a_string:
        if ch.isdigit():
            str_stats['digits'] += 1
        elif ch.isalpha():
            str_stats['letters'] += 1
    return str_stats



# Write a function to play a guessing game: to guess a number between 1 to 9.
# (scenario: user is prompted to enter a guess. If the user guesses wrong then
# the prompt reappears until the guess is correct; on successful guess, user
# should get a "Well guessed!" message, and the function terminates
#
# Hint: use function randint from random package to generate a number to
# be guessed in the game
import random

def guess_number():
    num = random.randint(1,9)
    while True:
        val = input("Guess the number (1-9) or enter q to exit the game:\n")
        if val.lower() == 'q':
            print("Better luck next time!")
            return
        if int(val) == num:
            print("Correct! Congrats!")
            return
        else:
            print("Wrong! Try again")



if __name__ == '__main__':

    # odd_or_even()

    # print(factorial(7))

    # a = [31, 72, 13, 41, 5, 16, 87, 98, 9]
    # print(nth_lowest(a, 3))
    # print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))
    # print(nth_lowest('today', 6))

    # print(list_stats([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, 81]))

    # print_new_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 9)

    # print(anagrams('Cat', 'Tac'))
    # print(anagrams('Bob', 'Bill'))

    # create_dictionary(5)

    # print(digits_letters_counter('Tuesday, Oct 9, 2018'))

    guess_number()
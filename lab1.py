# Write a function that asks the user for a number, and depending on whether
# the number is even or odd, prints out an appropriate message.

"""
VD: Sta mislis o varijanti da pisemo komentare ovako kao sto sam stavio dole, tj. kao docstrings, po PEP 8 preporukama:
https://www.python.org/dev/peps/pep-0008/#documentation-strings
Ja sam to ubacio samo za ovu prvu funkciju, pa ako usvojis tu ideju mozemo da prebacimo i u ostale.
Ta prica, koliko kapiram PEP 8, vazi za fungcije, klase i metode.

A na pocetku svakog modula mozemo da napisemo neki komentar za ceo modul.
"""


def odd_or_even():
    """VD: Write a function that asks the user for a number, and depending on whether
    the number is even or odd, prints out an appropriate message.
    """

    num = input("Please enter an integer value:\n")
    if int(num) % 2 == 0:
        print("You've entered an EVEN number")
    else:
        print("You've entered an ODD number")


# Write a function to calculate the factorial of a number.
# The function accepts the number (a non-negative integer)
# as an argument.

def factorial(num):
    f = 1
    for i in range(num, 1, -1):
        f *= i
    return f


# Write a function that returns nth lowest number of a list (or an iterable in general).
# Return the lowest if n (2nd argument) is greater than the number of elements in the iterable.

# VD: U gornjem komentaru spominjes samo lowest NUMBER.
# Sta mislis o tome da demonstriras i jedan primer kad an_iterable nije lista BROJEVA (nth_lowest ce i tada da radi)?
# Stavio sam jedan takav primer pod komentarima dole u if __name__ == '__main__' delu.
# Cisto zbog njihovog navikavanja na to da parametar funkcije nema unapred fiksiran tip.

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
    smallest = abs(a_list[0])
    largest = abs(a_list[0])
    sum_pos = 0
    prod_neg = 1
    for num in a_list:
        if abs(num) < smallest: smallest = abs(num)
        elif abs(num) > largest: largest = abs(num)
        if num > 0: sum_pos += num
        elif num < 0: prod_neg *= num
    return smallest, largest, sum_pos, prod_neg


# Write a function that receives a list of numbers and a number.
# The function:
# - makes a new list that has unique elements from the input list
#   that are less than the given number
# - prints the number of elements in the new list
# - sorts the elements in the list and prints them, an element per line

def print_new_list(numbers, threshold):
    selection = set()
    for num in numbers:
        if num < threshold:
            selection.add(num)
    print("Number of elements in the new list:", str(len(selection)))
    selection = list(selection)
    selection.sort(reverse=True)
    for num in list(selection):
        print(num)


# Write a function that receives two strings and checks if they
# are anagrams (assume input consists of alphabets only).
# The function returns appropriate boolean value.

def anagrams(str1, str2):
    str2_rev = list(reversed(str2.lower()))
    return list(str1.lower()) == str2_rev


# Write a function that generates and prints a dictionary that contains
# a number (between 1 and n) in the form (x, x*x)

def create_dictionary(n):
    num_dict = dict()
    for x in range(1, n+1):
        num_dict[x] = x*x
    for key, val in num_dict.items():
        print(f"{key}:{val}")


# Write a function that accepts a string and calculates the number
# of digits and letters. The function returns a dictionary with
# the computed values.

def digits_letters_counter(a_string):
    str_stats = {'letters':0, 'digits':0}
    for ch in a_string:
        if ch.isdigit():
            str_stats['digits'] += 1;               # VD: Zasto si ovde stavila ';'? Navika iz Jave, ili nesto drugo?
        elif ch.isalpha():
            str_stats['letters'] += 1;              # VD: Zasto si ovde stavila ';'? Navika iz Jave, ili nesto drugo?
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
        # VD: Ovo pod komentarima je moj dodatak.
        # Too heavy za prvi cas, ali treba biti svestan toga da neko moze da ukuca i nesto sto nije ni int ni 'q'.
        # try:
        #     if int(val) == num:
        #         print("Correct! Congrats!")
        #         return
        #     else:
        #         print("Wrong! Try again")
        if int(val) == num:
            print("Correct! Congrats!")
            return
        else:
            print("Wrong! Try again")


if __name__ == '__main__':

    # odd_or_even()

    # print(factorial(7))

    # print(nth_lowest(b, 16))
    # print(nth_lowest(['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c'], 6))   # VD comment

    # print(list_stats([1.2, 3.4, 5.6, -4.2, -5.6, 9, 11.3, -23.45, 81]))

    # print_new_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 9)

    # print(anagrams('Cat', 'Tac'))

    # create_dictionary(5)

    # print(digits_letters_counter('comma-separated_123'))

    guess_number()
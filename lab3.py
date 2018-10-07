# Write a function that receives a piece of text and computes the frequency of
# the words appearing in the text.
# The words and their frequencies are to be stored in a dictionary. The function
# prints words and their frequencies after sorting them alphanumerically.
#
# After testing the function, alter it so that the dictionary entries are printed
# in the decreasing order of the words' frequencies.
# (hint: use itemgetter() f. from the operator module)

import operator

def word_frequencies(text):
    words_dict = dict()
    words = text.split()
    words = [word.lower() for word in words]
    for word in words:
        if word in words_dict.keys():
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    # for word in sorted(words_dict.keys()):
    #     print(word, ":", str(words_dict[word]))
    for word, freq in sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True):
        print(word, ":", str(freq))


# Write a function that accepts a sequence of comma separated passwords
# and checks their validity using the following criteria:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length: 6
# 5. Maximum length: 12
# Passwords that match the criteria should be printed in one row separated by a comma.

import string

def password_check(passwords):
    valid_ones = []
    passwords = passwords.split(',')
    passwords = [pword.strip() for pword in passwords]
    for pword in passwords:
        criteria_met_cnt = 0
        if 6 <= len(pword) <= 12:
            criteria_met_cnt += 2
        for ch in pword:
            if ch in string.ascii_lowercase:
                criteria_met_cnt += 1
                break
        for ch in pword:
            if ch in string.ascii_uppercase:
                criteria_met_cnt += 1
                break
        for ch in pword:
            if ch in range(0,10):
                criteria_met_cnt += 1
                break
        for ch in pword:
            if ch in ['$','#','@']:
                criteria_met_cnt += 1
                break
        if criteria_met_cnt == 5:
            valid_ones.append(pword)
    print(", ".join(valid_ones))


# Write a function that prompts the user for name, age, and height of a couple of people
# (e.g. members of a sports team) and stores the input values as a list of tuples of
# the form (name, age, height), where name is string, whereas age and height are numbers.
# The function then sorts and prints the list based on name, then age and finally score
# (so, the following sorting criteria should be applied: 1) name, 2) age, 3) score).

def sorted_tuples():
    print("You will be kindly asked to provide name, age, and height for your team members")

    members = []
    done = False
    while not done:
        name = input("Name: ")
        age = int(input("Age: "))
        height = int(input("Height (in cm): "))
        members.append((name, age, height))
        answer = input("Do you want to continue (Y/N)? ")
        if answer.lower() == 'n':
            done = True
    members = sorted(members, key=operator.itemgetter(0,1,2))
    for m in members:
        print(m)


# Write a function that prompts the user for name, age, height (in meters), weight (in kg), and
# competition score (0-100) of members of a sports team. All data items for one member should be
# entered in a single line, separated by a comma (e.g. Bob, 19, 1.78, 75, 55).
# The function should store the input values as a list of dictionaries
# (e.g. {name:Bob, age:19, height: 1.78, weight:75, score:55}), where name is string, age is integer,
# and the other 3 attributes are real values. This list should be the return value of the function.

def members_list():
    print("You'll be kindly asked to provide name, age, height, and score for each of your team members")
    print("Enter \'done\' to terminate\n")

    members = []
    while True:
        member_data = input("Please enter name, age, height, weight, and score separated by a comma:\n")
        member_data = member_data.split(',')
        member_data = [data_item.strip() for data_item in member_data]

        if member_data[0].lower() == 'done':
            break

        dict_keys = ['name', 'age', 'height', 'weight', 'score']

        # Option 1:
        # m_dict = dict()
        # for i, key in enumerate(dict_keys):
        #     value = member_data[i]
        #     if key == 'age': value = int(value)
        #     elif key in ['height', 'weight', 'score']: value = float(value)
        #     m_dict[key] = value

        # Option 2:
        member_data[1] = int(member_data[1])
        for i in range(2,5):
            member_data[i] = float(member_data[i])
        m_dict = dict(zip(dict_keys, member_data))

        members.append(m_dict)
    return members


# Write a function that takes as its input the list of dictionaries created by the previous function
# and computes and prints the following statistics:
# - the average (mean) age, height and weight of the team members.
# - median score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations

from statistics import mean, median

def team_stats(members):
    age_list = []
    weight_list = []
    height_list = []
    score_list = []
    for mem_dict in members:
        age_list.append(mem_dict['age'])
        weight_list.append(mem_dict['weight'])
        height_list.append(mem_dict['height'])
        score_list.append(mem_dict['score'])
    print(f"Average age: {mean(age_list):.2f}, "
          f"average weight: {mean(weight_list):.2f}, "
          f"and average height: {mean(height_list):.2f}")
    print(f"Median score: {median(score_list)}")

    max_score = 0
    max_name = ""
    for mem_dict in members:
        if (mem_dict['age'] < 21) and (mem_dict['score'] > max_score):
            max_score = mem_dict['score']
            max_name = mem_dict['name']
    if max_name != "":
        print(f"Young player with the highest score: {max_name}")


# Write a function that creates and prints a dictionary from the two given lists
# (assume the lists to be of equal length).
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.

def lists_to_dict(l1, l2):
    d = dict()
    zipped = zip(l1, l2)
    for cl, num in zipped:
        d[cl] = num
    for cl in sorted(d.keys()):
        print(cl, ":", d[cl])


# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size
#
# Hint: consider using defaultdict from the collections module

from collections import defaultdict
from operator import itemgetter

def stud_per_class(class_data):
    class_dict = defaultdict(int)
    for cl, num in class_data:
        class_dict[cl] += num
    for cl, num in sorted(class_dict.items(), key=itemgetter(1), reverse=True):
        print(cl, ":", num)


if __name__ == '__main__':
    # word_frequencies("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

    # password_check("ABd1234@1, a F1#, 2w3E*, 2We3345")

    # sorted_tuples()

    # team = members_list()
    # print(team)

    team = [{'name': 'Bob', 'age': 18, 'height': 1.77, 'weight': 79.0, 'score': 50.0},
                 {'name': 'Tim', 'age': 17, 'height': 1.78, 'weight': 80.0, 'score': 84.0},
                 {'name': 'Jim', 'age': 19, 'height': 1.98, 'weight': 90.0, 'score': 94.0}]
    team_stats(team)

    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA"]
    # lists_to_dict(countries, dishes)

    # stud_per_class([('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)])
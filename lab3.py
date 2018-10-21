# Task 1
# Write a function that receives a piece of text and computes the frequency of
# the tokens appearing in the text (a token is a string of contiguous characters
# between two spaces, or between a space and punctuation marks).
# Tokens and their frequencies are to be stored in a dictionary. The function
# prints tokens and their frequencies after sorting the tokens alphanumerically.
#
# After testing the function, alter it so that the dictionary entries are printed
# in the decreasing order of the tokens' frequencies.
# (hint: use itemgetter() f. from the operator module)

from operator import itemgetter

# Option 1
# def token_frequences(text):
#     tokens = text.split()
#     token_dict = dict()
#     for token in set(tokens):
#         token_dict[token.lower()] = 0
#     for token in tokens:
#         token_dict[token.lower()] += 1
#     # for key, val in sorted(token_dict.items()):
#     #     print("{0}:{1}".format(key, val))
#     for key, val in sorted(token_dict.items(), key=itemgetter(1), reverse=True):
#         print("{0}:{1}".format(key, val))

# Option 2
from collections import defaultdict

def token_frequences(text):
    tokens = text.split()
    tokens_dict = defaultdict(int)
    for token in tokens:
        tokens_dict[token.lower()] += 1
    print("Alphabetical sorting:")
    for key, val in sorted(tokens_dict.items()):
        print("{0}:{1}".format(key, val))
    print("\nFrequency-based sorting:")
    for key, val in sorted(tokens_dict.items(), key=itemgetter(1), reverse=True):
        print("{0}:{1}".format(key, val))



# Task 2
# Write a function that accepts a sequence of comma separated passwords
# and checks their validity using the following criteria:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length: 6
# 6. Maximum length: 12
# Passwords that match the criteria should be printed in one row
# separated by a comma.

import string

def check_passwords(passwords):
    valid_passwords = []
    passwords = passwords.split(',')
    for password in passwords:
        # print(password)
        password = password.lstrip()
        conditions = [False]*6
        for ch in password:
            if ch in string.ascii_lowercase:
                conditions[0] = True
            if ch in string.digits:
                conditions[1] = True
            if ch in string.ascii_uppercase:
                conditions[2] = True
            if ch in ['$','#','@']:
                conditions[3] = True
        if 6 <= len(password) <= 12:
            conditions[4] = conditions[5] = True
        if all(conditions):
            valid_passwords.append(password)
    print(", ".join(valid_passwords))



# Task 3
# Write a function that prompts the user for name, age, and height (in cm) of a couple of
# people (e.g. members of a sports team) and stores the input values as a list of tuples of
# the form (name, age, height), where name is string, whereas age and height are numbers.
# After entering these data items for one person, the user is asked if he/she wants to
# continue or not. When the entry is finished the function sorts and prints the list
# based on name, then height and finally age (so, the following sorting criteria should
# be applied: 1) name, 2) height, 3) age).

def team_members_data():
    members = []
    print("You are kindly asked to provide information about your team members")
    while True:
        name = input("Member's name:\n")
        age = input("Age:\n")
        height = input("Height (in cm):\n")
        members.append((name, int(age), int(height)))

        response = input("More members to add (Yes/No)?")
        if response.lower() in ['no', 'n']:
            break

    # print(members)

    for name, age, height in sorted(members, key=itemgetter(0,2,1)):
        print("{0}, age:{1}, height:{2}".format(name, age, height))




# Task 4
# Write a function that prompts the user for name, age, height (in meters), weight (in kg), and
# competition score (0-100) of members of a sports team. All data items for one member should be
# entered in a single line, separated by a comma (e.g. Bob, 19, 1.78, 75, 55). The entry stops
# when the user enters 'done'.
# The function stores the data for each team member as a dictionary, such as
# {name:Bob, age:19, height: 1.78, weight:75, score:55}
# where name is string, age is integer, and the other 3 attributes are real values.
# The data for all team members should form a list of dicitonaries; this list is the return
# value of the function.


def team_data():
    print("You are kindly asked to provide some information about each team member:\n",
          "Enter 'done' to terminate the entry")

    members = []
    dict_keys = ['name', 'age', 'height', 'weight', 'score']
    while True:
        member_data = input("Please enter name, age, height, weight, and competition score\n")
        if member_data.lower() == 'done':
            break

        member_data = member_data.split(',')

        # Option 1
        # member_dict = dict()
        # for item_id, data_item in enumerate(member_data):
        #     data_item = data_item.strip()
        #     if item_id == 1:
        #         data_item = int(data_item)
        #     elif item_id in [2,3,4]:
        #         data_item = float(data_item)
        #     member_dict[dict_keys[item_id]] = data_item

        # Option 2
        member_data = [data_item.strip() for data_item in member_data]
        member_data[1] = int(member_data[1])
        for i in range(2,5):
            member_data[i] = float(member_data[i])
        member_dict = dict(zip(dict_keys, member_data))

        members.append(member_dict)

    return members



# Task 5
# Write a function that takes as its input the list of dictionaries created by the previous function
# and computes and prints the following statistics:
# - the average (mean) age, height, and weight of the team members
# - the team's median score
# - name of the player with the highest score among those under 21 years of age
#
# Hint: the 'statistics' module provides functions for the required computations

from statistics import median, mean

def team_stats(members):

    # Option 1
    # age_list = []
    # height_list = []
    # weight_list = []
    # score_list = []
    # for member in members:
    #     age_list.append(member['age'])
    #     height_list.append(member['height'])
    #     weight_list.append(member['weight'])
    #     score_list.append(member['score'])
    # averages = [mean(age_list), mean(height_list), mean(weight_list)]
    # print("Average age:{0}, height:{1:.2f}, weight:{2:.2f}".format(*averages))
    # print("Median score:{0:.2f}".format(median(score_list)))

    # Option 2
    avg_age = mean([member['age'] for member in members])
    avg_height = mean([member['height'] for member in members])
    avg_weight = mean([member['weight'] for member in members])
    med_score = median([member['score'] for member in members])
    print("Average age:{0}, height:{1:.2f}, weight:{2:.2f}".format(avg_age, avg_height, avg_weight))
    print("Median score:{0:.2f}".format(med_score))

    best_score = -1
    best_name = ""
    for member in members:
        if (member['age'] < 21) and (member['score'] > best_score):
            best_score = member['score']
            best_name = member['name']
    print('Member with the best score ({0:.2f}) is {1}'.format(best_score, best_name))



# Task 6
# Write a function that creates a dictionary from the two given lists.
# Assure the lists are of equal length. Print the dictionary sorted based on
# the key values.
# Example: a list of countries and a list of the countries' national dishes
# should be turned into a dictionary where keys are country names and values
# are the corresponding dishes.

def lists_to_dict(l1, l2):
    if len(l1) != len(l2):
        print("lists have to be of the same lenght")
    else:
        a_dict = dict(zip(l1, l2))
        for key in sorted(a_dict):
            print(key + ": " + a_dict[key])



# Task 7
# Write a function to count the total number of students per class. The function receives
# a list of tuples of the form (<class>,<stud_count>). For example:
# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# The function creates a dictionary of classes and their student numbers; it then
# prints the classes and their sizes in the decreasing order of the class size.
#
# Hint: consider using defaultdict from the collections module

def total_class_counts(students_per_class):
    counts_dict = defaultdict(int)
    for cl, stud_count in students_per_class:
        counts_dict[cl] += stud_count
    for cl, stud_tot in sorted(counts_dict.items(), key=itemgetter(1), reverse=True):
        print(cl + ": " + str(stud_tot))




if __name__ == '__main__':

    # token_frequences("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

    # check_passwords("ABd1234@1, a F1#, 2w3E*, 2We3345")

    # team_members_data()

    # print(team_data())

    # team = [{'name': 'Bob', 'age': 18, 'height': 1.77, 'weight': 79.0, 'score': 50.0},
    #              {'name': 'Tim', 'age': 17, 'height': 1.78, 'weight': 80.0, 'score': 84.0},
    #              {'name': 'Jim', 'age': 19, 'height': 1.98, 'weight': 90.0, 'score': 94.0}]
    # team_stats(team)

    # dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    # countries = ["Italy", "Germany", "Spain", "USA"]
    # lists_to_dict(countries, dishes)

    l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
    total_class_counts(l)
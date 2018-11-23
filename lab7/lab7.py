import pickle
import csv
import shelve
from collections import Counter, defaultdict


# Task 1
# Write a function that reads in the content of the given text file, sorts it,
# and writes the (sorted) content to a new textual file ("task1_result.txt").
# Assume that the content of the given file consists of file names, some
# of which have an extension ('hello.txt'), others don't ('results').
# Each file name is given in a separate line.
# Sorting should be case insensitive and done in the ascending alphabetical
# order, as follows:
# - for files with extension: first based on the extension and then based
#   on the file name,
# - for files without extension, based on the file name.
# Include appropriate try except blocks to prevent program from crushing
# in case of non existing file, or a problem ocurring while reading
# from / writing to a file.

# Use the file 'file_q5c.txt'


def read_sort_write(src_file):
    with_extension = []
    no_extension = []

    def with_extension_sort(line):
        name, ext = line.lower().rsplit(".", maxsplit=1)
        return ext, name

    try:
        with open(src_file, 'r') as src:
            for line in src:
                line = line.rstrip('\n')
                if line.find(".") == -1:
                    no_extension.append(line)
                else:
                    with_extension.append(line)

        with_extension = sorted(with_extension, key=with_extension_sort)
        no_extension = sorted(no_extension, key=lambda item: item.lower())

        with open("task1_result.txt", "w") as dest:
            dest.write("\n".join(with_extension))
            dest.write("\n")
            dest.write("\n".join(no_extension))

    except FileNotFoundError as fnf_err:
        print(fnf_err)
    except IOError as io_err:
        print(io_err)



# Task 2
# The file cities_and_times.txt contains city names and times.
# Each line contains the name of the city, followed by abbreviated
# weekday (e.g. "Sun"), and the time in the form hh:mm.
# Read in the file and create an alphabetically ordered list of the form:
# [('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ...].
# Having created this list,
# - serialise it in a file, as a list object (using the pickle module)
# - write its content into a csv file, in the format:
#   city_name; weekday; hour; minute
# Include appropriate try except blocks to prevent program from crushing
# in case of non existing file, or a problem while reading from / writing
# to a file, or transforming data values.
#
# Note: file cities_and_times.txt downloaded from:
# https://www.python-course.eu/cities_and_times.txt
# 
# Note: for a list of things that can be pickled, see this page:
# https://docs.python.org/3/library/pickle.html#pickle-picklable

def read_write_city_data(src_file):

    def write_to_csv(fname, city_data):
        try:
            with open(fname, "w") as csvf:
                data_writer = csv.writer(csvf, delimiter=';')
                data_writer.writerow(('city_name', 'weekday', 'hour', 'minute'))
                for city, weekday, time in city_data:
                    data_writer.writerow((city, weekday, time[0], time[1]))
        except csv.Error as err:
            print("Error when trying to write the results to a csv file: " + str(err))


    data_list = []

    try:
        with open(src_file, 'r') as src:
            for line in src:
                city, weekday, time = line.rstrip().rsplit(maxsplit=2)
                hour, min = time.split(":")
                try:
                    data_list.append((city, weekday, (int(hour), int(min))))
                except ValueError as val_err:
                    print("Error when processing time data: {0}".format(val_err))

        data_list = sorted(data_list, key=lambda city_data: city_data[0])

    except FileNotFoundError as fnf_err:
        print(fnf_err)
        print("Not able to proceed...Terminating the function")
    except IOError as io_err:
        print("Error while trying to read from file {0}: {1}".format(src_file, io_err))

    else:
        serialise_to_file("task2_results.pkl", data_list)
        write_to_csv("task2_results.csv", data_list)



def serialise_to_file(fname, data):
    try:
        with open(fname, 'bw') as fw:
            pickle.dump(data, fw)
    except IOError as io_err:
        print("Error when serialising data to file {0}:\n".format(fname, io_err))
    except pickle.PickleError as pkl_err:
        print(pkl_err)



# Task 3
# You are given a text file that lists full file paths for a bunch of images
# (one image file path per line). Write a function that reads in the content
# of this text file and does the following:
# - counts the number of images in each category, and stores the computed
#   counts in a csv file in the format: category_name, image_count
# - creates and stores (in a file) a dictionary with the image category as
#   the key and a list of image names in the corresponding category as value;
#   for storage use 1) pickle and 2) shelve.
#
# Note: file Training_01.txt downloaded from:
# http://www.practicepython.org/assets/Training_01.txt
#
# Note: for a nice quick introduction to the shelve module, see: https://pymotw.com/3/shelve/


def image_categories(src_file):

    cat_file_list = []

    def get_file_category_tuple(fpath):
        category, file = fpath.rstrip().rsplit("/", maxsplit=1)
        return category[3:], file

    try:
        with open(src_file, 'r') as src_file:
            lines = src_file.readlines()
            cat_file_list = [get_file_category_tuple(line) for line in lines]

    except FileNotFoundError as fnf_err:
        print(fnf_err)
    except IOError as io_err:
        print(io_err)

    else:
        compute_and_store_category_counts(cat_file_list)
        create_and_store_img_dict(cat_file_list)


def compute_and_store_category_counts(cat_file_tuples):

    categories = [cat for cat, file in cat_file_tuples]
    category_counts = Counter(categories)

    # alternative:
    # from collections import defaultdict
    # category_dict = defaultdict(int)
    # for cat_file in cat_file_list:
    #     category_dict[cat_file[0]] += 1

    try:
        with open("task3_results.csv", "w") as csvf:
            csv_writer = csv.writer(csvf)
            csv_writer.writerow(('category_name', 'image_count'))
            for item in category_counts.items():
                csv_writer.writerow(item)
    except csv.Error as err:
        print("Error while writing category counts to csv file:\n{}".format(err))


def create_and_store_img_dict(cat_file_tuples):

    img_dict = defaultdict(list)
    for category, image in cat_file_tuples:
        img_dict[category].append(image)

    serialise_to_file("task3_results.pkl", img_dict)

    try:
        with shelve.open("task3_result_shelve") as s:
            for key, val in img_dict.items():
                s[key] = val
    except IOError as io_err:
        print(io_err)




# Task 4
# Write a function that receives two text files with lists of numbers (integers) in
# them. The function identifies the numbers present in both lists and writes them
# down in a new file (as a list of numbers).
# Note: it may happen that not all lines in the input files contain numbers, so,
# after reading in the content of the files, assure that only numerical values are
# considered for comparison.
#
# Note: based on this exercise:
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
# For testing use these files:
# list of prime numbers: http://www.practicepython.org/assets/primenumbers.txt
# list of happy numbers: http://www.practicepython.org/assets/happynumbers.txt

def write_common_numbers(fnum1, fnum2):

    def read_numbers_from_file(fname):
        num_list = list()
        try:
            with open(fname, 'r') as fobj:
                lines = [line.rstrip('\n') for line in fobj.readlines()]
                for line in lines:
                    try:
                        num_list.append(int(line))
                    except ValueError as val_err:
                        print("Cannot transform {0} to number due to: {1}".format(line, val_err))
        except FileNotFoundError as fnf_err:
            print(fnf_err)

        return num_list

    num_list_1 = read_numbers_from_file(fnum1)
    num_list_2 = read_numbers_from_file(fnum2)

    commons_list = [num for num in num_list_1 if num in num_list_2]
    # alternative:
    # commons_list = list(set(num_list_1).intersection(set(num_list_2)))

    serialise_to_file("task4_results.pkl", commons_list)



if __name__ == "__main__":

    # read_sort_write("data/file_q5c.txt")

    # read_write_city_data("data/cities_and_times.txt")

    # image_categories("data/Training_01.txt")

    # t4_f1 = "data/primenumbers.txt"
    # t4_f2 = "data/happynumbers.txt"
    # write_common_numbers(t4_f1, t4_f2)

    with open("task4_results.pkl", "rb") as bf:
        results = pickle.load(bf)
        print(results)
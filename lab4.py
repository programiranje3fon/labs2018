# Write a function that receives an arbitrary number of numeric values and computes their product.
# The function also receives a named argument "absolute" with the default value False, which determines
# if absolute value of the product is to be returned or not.
# Implement the function in two different ways:
#
# 1) using a for loop
# 2) using the reduce() f. from the functools package together with an appropriate lambda f.

from functools import reduce

# def product(*numbers, absolute = False):
#     result = 1
#     for number in numbers:
#         result *= number
#     if absolute:
#         result = abs(result)
#     return result

def product(*numbers, absolute = False):
    result = reduce(lambda x, y: x * y, numbers)
    if absolute:
        result = abs(result)
    return result


# Write a function that receives an arbitrary number of strings and returns a list
# of those strings where the first and the last character are the same and the
# total number of unique characters is above the given threshold. The threshold
# is given as a named argument with the default value of 3.
#
# Implement the function in two different ways:
# 1) using a for loop
# 2) using the filter() f. together with an appropriate lambda f.

# def filter_strings(*strings, min_unique = 3):
#     result = []
#     for s in strings:
#         if (s[0] == s[-1]) and (len(set(s)) > min_unique):
#             result.append(s)
#     return result

def filter_strings(*strings, min_unique = 3):
    result = filter(lambda s: (s[0] == s[-1]) and (len(set(s)) > min_unique), strings)
    return list(result)


# Write a function that receives a list of product orders, where each order is a 4-tuple
# of the form (order_id, product_name, quantity, price_per_item). The function returns
# a list of 2-tuples of the form (order_id, total_price) where total price (in USD) for
# an order is the product of the quantity and the price per item (in USD) plus the shipping
# cost for orders with total value less than 100 USD. The shipping cost is given as the
# value of the input argument 'shipping' with default value of 10 (USD).
#
# Implement the function in two different ways:
# 1) using a for loop
# 2) using the map() f. together with an appropriate lambda f.

# def process_orders(orders, shipping=10):
#     procesed_orders = []
#     for order in orders:
#         order_id, product, quantity, price = order
#         tot_price = quantity * price
#         if tot_price >= 100:
#             tot_price += shipping
#         procesed_orders.append((order_id, tot_price))
#     return procesed_orders

def process_orders(orders, shipping=10):
    f = lambda order: (order[0], order[2] * order[3]) if order[2] * order[3] < 100 \
                        else (order[0], order[2] * order[3] + shipping)
    return list(map(f, orders))


# Create a decorator that measures the time a function takes to execute and prints the duration to the console.
# Create also a couple of simple functions to test the decorator and decorate them accordingly.
# Hint 1: use the decorator-writing pattern:
# import functools
# def decorator(func):
#     @functools.wraps(func)			                # preserves func's identity after it's decorated
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
# Hint 2: to measure the time a function takes, use the time.perf_counter() function from the Python Standard Library.

def stopwatch(f):                                       # alt. names: runtime, running_time, timer, get_time, interval

    import functools                                    # can be imported somewhere on top of the module as well

    @functools.wraps(f)
    def stopwatch_wrapper(*args, **kwargs):
        import time                                     # can be imported somewhere on top of the module as well

        # Do something before
        print('Running', f.__name__ + '(' + ','.join([str(arg) for arg in args]) + ')...')
        start_time = time.perf_counter()

        v = f(*args, **kwargs)

        # Do something after
        end_time = time.perf_counter()
        print('Time:', '{0:.5f}'.format(end_time - start_time), 'sec.')

        return v

    return stopwatch_wrapper


@stopwatch
def sum_of_squares(n, **kwargs):                        # test function 1
    for _ in range(n):
        sum([i * i for i in range(10000)])

@stopwatch
def sum_of_powers(x, y, n):                             # test function 2
    if x not in range(1, 4):                            # constrain input parameters for the sake of running time
        x = 3
    if y not in range(1, 4):
        y = 3
    if n not in range(1, 1000):
        n = 999
    for _ in range(n):
        sum([i**x + i**y for i in range(10000)])


# Create a decorator that makes a function run with a delay of n sec (n should be the decorator parameter).
# Create also a couple of simple functions to test the decorator and decorate them accordingly.
# Hint 1: use the "extended" decorator-writing pattern:
# def decorator(arg1, arg2, ...):
#     def real_decorator(func):
#         import functools
#         @functools.wraps(func)			            # preserves func's identity after it's decorated
#         def wrapper_real_decorator(*args, **kwargs):
#             # Do something before
#             some_stuff()
#             some_stuff_with_arguments(arg1, arg2, ...)
#             value = func(*args, **kwargs)
#             # Do something after
#             more_stuff()
#             return value
#         return wrapper_real_decorator
#     return real_decorator
# Hint 2: use the time.sleep() function from the Python Standard Library to introduce the delay.

def delay(n):

    def wait(f):

        import functools                                # can be imported somewhere on top of the module as well

        @functools.wraps(f)
        def wrapper_wait(*args, **kwargs):
            import time                                 # can be imported somewhere on top of the module as well

            # Do something before
            time.sleep(n)                               # improves output visually
            print('Wait', n, 'sec...')
            time.sleep(n)

            v = f(*args, **kwargs)

            # Do something after

            return v

        return wrapper_wait

    return wait


@delay(1)
# @wait
def print_list_elements(l):
    while l:                                            # l != []
        print(l[0])
        del(l[0])
        print_list_elements(l)


if __name__ == '__main__':

    # print(product(1,-4,13,2))
    # print(product(1, -4, 13, 2, absolute=True))

    # # calling the product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # this is NOT a way to make the call:
    # print(product(num_list))
    # # instead, this is how it should be done:
    # print(product(*num_list)) # the * operator is 'unpacking' the list

    # str_list = ['yellowy', 'Bob', 'lovely', 'yesterday', 'too']
    # print(filter_strings(*str_list))

    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_orders(orders))

    # sum_of_squares(100)
    # sum_of_powers(2, 3, 200)

    l = ["Bruce Springsteen", "Patti Smith", "Alejandro Escovedo"]
    print_list_elements(l)


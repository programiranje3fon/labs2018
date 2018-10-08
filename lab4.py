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

    orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
              ("98762", "Programming Python, Mark Lutz", 5, 56.80),
              ("77226", "Head First Python, Paul Barry", 3, 32.95),
              ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]

    print(process_orders(orders))
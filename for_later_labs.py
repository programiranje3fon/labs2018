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
            print('Wait', n, 'sec...')
            time.sleep(n)
            # time.sleep(n/2)
            v = f(*args, **kwargs)
            # Do something after
            # time.sleep(n/2)
            # print('Done.')
            return v

        return wrapper_wait

    return wait

# def delay(n):
#
#     def wait(f):
#
#         import functools                                # can be imported somewhere on top of the module as well
#
#         @functools.wraps
#         def wrapper_wait(*args, **kwargs):
#             v = f(*args, **kwargs)
#             return v
#
#         return wrapper_wait
#
#     return wait

# def wait(f):
#
#     import functools                                # can be imported somewhere on top of the module as well
#
#     @functools.wraps(f)
#     def wrapper_wait(*args, **kwargs):
#         print("Before")
#         v = f(*args, **kwargs)
#         print("After")
#         return v
#
#     return wrapper_wait


@delay(1)
# @wait
def print_list_elements(l):
    while l:                                            # l != []
        print(l[0])
        del(l[0])
        print_list_elements(l)


if __name__ == '__main__':

    l = ["Bruce Springsteen", "Patti Smith", "Alejandro Escovedo"]
    print_list_elements(l)
def my_decorator(func):
    def wrapper(a, *args, **kwargs):
        print('Calling {}, {}, {}, {}'.format(func.__name__, a, args, kwargs))
        result = func(a, *args, **kwargs)
        print('Finished {}'.format(func.__name__),result)
    return wrapper


@my_decorator
def test_func(a, b=1, *args, **kwargs):
   print("argument a: ", a)
   print("argument b: ", b)
   print("argument args: ", args)
   print("argument kwargs: ", kwargs)

   return a + b

test_func(2, 3, 4, 5, c=6, d=7)
print()
test_func(2, c=5, d=6)
print()
test_func(10)
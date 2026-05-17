import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
    return wrapper_function  # Need to always return the wrapper function from inside the decorator function

@delay_decorator  # Decorates this other function with a time.sleep(2) delay
def say_hello():  # This is known as 'syntactic sugar'
    print("Hello!")

say_hello()

# So when you call say_hello() it will get passed through the decorator function,
# which adds the time delay, before being run

# The above is the same as
decorated_function = delay_decorator(say_hello)
decorated_function()
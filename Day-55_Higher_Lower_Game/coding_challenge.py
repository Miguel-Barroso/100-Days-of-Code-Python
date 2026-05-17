# I completed the challenge myself but let chatGPT annotate with comments so I can review later

# A decorator is just a function that takes another function as input
# and returns a new function (usually a wrapper) that adds extra behavior.

# Define the logging_decorator
def logging_decorator(function):
    # This is the "wrapper" function that will replace the original function
    def wrapper(*args, **kwargs):
        # Print the function name and the arguments it was called with
        print(f"You called {function.__name__}{args}")

        # Call the original function with all the given arguments
        # Save the result so we can both log it and return it
        result = function(*args, **kwargs)

        # Print the result of the function call
        print(f"It returned: {result}")

        # VERY IMPORTANT: Return the result, so the decorated function
        # still behaves like the original function
        return result

    # Return the wrapper function so it replaces the original
    return wrapper


# Apply the decorator using the @ syntax
# This means: a_function = logging_decorator(a_function)
@logging_decorator
def a_function(*args):
    # Just return the sum of all arguments passed in
    return sum(args)


# Call the decorated function
# Because of the decorator, this will now also log the call and return value
a_function(1, 2, 3)

"""
	•	Outer function → takes the original function as input.
	•	Wrapper → runs every time the decorated function is called.
	•	Always return the wrapper from the decorator.
	•	Always return the result from the wrapper if the original function returns something.
"""
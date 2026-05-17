# Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Ahmed")
new_user.is_logged_in = True
create_blog_post(new_user)

# In summary, the decorator function only executes if the user is logged in
# It checks the first positional argument, which in this case has to be a User object
# If the attribute (is_logged_in) of the user equals to True, then the code executes

# The reason to use args and kwargs here is to make the decorator generic.
# The decorator can work across many functions with any number of arguments.


import functools

user = {'username': 'jose123', 'access_level': 'admin'}


# This is how you make a decorator generic
# This is very important to do, otherwise only some functions will be able to use it
def user_has_permission(func):
    @functools.wraps(func)
    # *args is a tuple, **kwargs is a dictionary
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            # Must pass all arguments and keyword arguments to function
            return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allows us to retrive the password for the admin panel.
    """
    return f'Password for {panel} pane is 1234'


@user_has_permission
def another():
    pass


print(my_function.__name__)

print(my_function('movies'))
print(another())

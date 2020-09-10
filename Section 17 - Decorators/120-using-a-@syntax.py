user = {'username': 'jose123', 'access_level': 'admin'}

def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func

@user_has_permission
def my_function():
    """
    Allows us to retrieve the password fr the admin panel.
    """
    return 'Password for admin panel is 1234.'

@user_has_permission
def another():
    pass


print(my_function())
print(my_function.__name__)  # Returns secure_func
print(my_function.__doc__)  # Returns None because it looks for secure_func information
print(another.__name__)  # Returns secure_func
# Must define __init__.py file to designate the file as a python file for older versions of python

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

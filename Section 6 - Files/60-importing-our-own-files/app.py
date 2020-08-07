# Import everything
# import file_operations

# Import specific methods from supporting folder
from utils.file_operations import save_to_file, read_file

save_to_file('Rolf', 'data.txt')
print(read_file('data.txt'))

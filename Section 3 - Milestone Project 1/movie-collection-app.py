movies = []


def new_movie():
  title = input("Please enter the title: ")
  director = input("Please enter the director: ")
  year = input("Please enter the release year: ")
  
  movies.append({
    'title': title,
    'director': director,
    'year': year
  })


def list_movies():
  for movie in movies:
    print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")


def find_movie():
  title = input("Enter the movie title you would like to display: ")
  for movie in movies:
    if movie['title'] == title:
      print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")

def menu():
  selection = ''
  while (selection != 'q'):
    selection = input('Please select an option (a, l, f, q): ')

    if selection == 'a':
      new_movie()
    elif selection == 'l':
      list_movies()
    elif selection == 'f':
      find_movie()

menu()
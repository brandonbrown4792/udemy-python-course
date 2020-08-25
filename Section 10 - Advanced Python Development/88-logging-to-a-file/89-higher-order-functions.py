def greet():
    print("Hello")


def before_and_after(func):
    print("Before...")
    print(func())
    print("After...")


before_and_after(lambda: 5)
before_and_after(greet)


movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"}
]


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)

    return found


find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movies = find_movie(looking_for, lambda movie: movie[find_by])

print(movies or 'No movies found')

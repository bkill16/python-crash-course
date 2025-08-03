print()

movies = ['Star Wars', 'Indiana Jones', 'Jaws']
print(movies)

print()

print(f'My favorite movies is {movies[1]}.')

print()

movies[2] = 'Jurassic Park'
print(movies)

print()

movies.append('Thunderbolts')
movies.append('Superman')
movies.append('Fantastic Four')
print(movies)

print()

movies.insert(4, 'Spider-Man')
print(movies)

print()

del movies[2]
print(movies)

print()

popped_movie = movies.pop()
print(popped_movie)
print(movies)

print()

popped_movie = movies.pop(1)
print(popped_movie)
print(movies)

print()

movies.remove('Superman')
print(movies)

print()

books = ['Harry Potter', 'Dune', 'The Lord of the Rings', 'Percy Jackson', 'Catching Fire']

print(sorted(books))
print(books)
print(sorted(books, reverse=True))
print(books)

print()

books.reverse()
print(books)
books.reverse()
print(books)

print()

books.sort()
print(books)
books.sort(reverse=True)
print(books)

print()
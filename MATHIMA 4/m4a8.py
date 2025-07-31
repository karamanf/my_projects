
try:
    with open("movies.txt", "r", encoding="utf-8") as f:
        my_movies = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    my_movies = []

movie = input("Δώσε μια αγαπημένη ταινία: ")

if movie in my_movies:
    print("Η ταινία υπάρχει ήδη. Δεν αποθηκεύτηκε.")
else:
    my_movies.append(movie)
    my_movies.sort()
    print(my_movies)
    print("Σύνολο ταινιών:", len(my_movies))

   
    with open("movies.txt", "w", encoding="utf-8") as f:
        for title in my_movies:
            f.write(title + "\n")

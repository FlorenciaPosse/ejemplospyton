
#Obtener valores introducidos por el usuario

movie_title = input("What is the title of your favorite movie? ")

movie_director = input("Who is the director? ")

release_year = input("What is the release year? ")

movie_genre = input("What genre is it? ")

duration_minutes = input("How many minutes long is it? ")

movie_awards = input("Does it have awards? (yes/no): ").lower() == "yes"

print("The movie title is:", movie_title)

print("The director is:", movie_director)

print("The release year was:", release_year)

print("The genre is:", movie_genre)

print("The movie duration is:", duration_minutes)

print("Has awards:", movie_awards)

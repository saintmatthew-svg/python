from datetime import datetime

movies = {}

def show_options():
    menu = """
        1. Add a movie
        2. Rate the movie
        3. View average rating
        4. Exit
        """
    print(menu)

def add_movie(movie_name):
    if movie_name in movies:
        return f"{movie_name} HAS ALREADY BEEN ADDED."
    else:
        current_time = datetime.now()
        movies[movie_name] = {"ratings": [], "added_on": current_time}
        return f"MOVIE: {movie_name} ADDED SUCCESSFULLY ON {current_time}."

def rate_movie(movie_name, rating):
    if movie_name not in movies:
        return f"{movie_name} NOT FOUND."
    if not (1 <= rating <= 5):
        return "INVALID RATING. PLEASE ENTER A RATING BETWEEN 1 AND 5."
    movies[movie_name]["ratings"].append(rating)
    return f"RATING {rating} ADDED FOR {movie_name}."

def view_average_rating(movie_name):
    if movie_name not in movies:
        return f"{movie_name} NOT FOUND."
    ratings = movies[movie_name]["ratings"]
    if not ratings:
        return f"NO RATINGS AVAILABLE FOR {movie_name}."
    average_rating = sum(ratings) / len(ratings)
    return f"AVERAGE RATING FOR {movie_name} IS {average_rating:.2f}."

def main():
    while True:
        show_options()
        try:
            choice = int(input("SELECT AN OPTION>>>> "))
            if choice == 1:
                movie_name = input("ENTER MOVIE NAME: ")
                print(add_movie(movie_name))
            elif choice == 2:
                movie_name = input("ENTER MOVIE NAME TO RATE: ")
                rating = int(input("ENTER RATING (1-5): "))
                print(rate_movie(movie_name, rating))
            elif choice == 3:
                movie_name = input("ENTER MOVIE NAME TO VIEW AVERAGE RATING: ")
                print(view_average_rating(movie_name))
            elif choice == 4:
                print("<<<<<<EXITING THE CONSOLE>>>>>>>")
                break
            else:
                print("INVALID INPUT. PLEASE SELECT A VALID OPTION.")
        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A NUMBER.")

if __name__ == "__main__":
    main()
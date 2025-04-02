import unittest
import MovieRatingSystem 

class TestMovieRatingSystem(unittest.TestCase):
    def setUp(self):
        global movies
        movies = {}

    def test_add_movie(self):
        movie_name = "Inception"
        actual = MovieRatingSystem.add_movie(movie_name)
        expected = "MOVIE: Inception ADDED SUCCESSFULLY ON 25/03/10."
        self.assertEqual(actual, expected)
        
    def test_that_movie_rate_works(self):
        movie_name = "Inception"
        rating = 3
        actual = MovieRatingSystem.rate_movie(movie_name, rating)
        expected = "RATING 3 ADDED FOR Inception."
        self.assertEqual(actual, expected)
        
    def test_that_movie_rate_rate_from_one_to_five(self):
        movie_name = "Inception"
        rating = 0 or 6
        actual = MovieRatingSystem.rate_movie(movie_name, rating)
        expected = 'INVALID RATING. PLEASE ENTER A RATING BETWEEN 1 AND 5.'
        self.assertEqual(actual, expected)
        
    def test_that_average_rating_rates_existing_movie_only(self):
        movie_name = "Inception"
        actual = MovieRatingSystem.view_average_rating(movie_name)
        self.assertEqual(actual, 'NO RATINGS AVAILABLE FOR Inception.')

if __name__ == "__main__":
    unittest.main()
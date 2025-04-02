import unittest
import MovieRatingSystem 
class TestMovieRatingSystem(unittest.TestCase):
    def setUp(self):
        global movies
        movies = {}

    def test_add_movie(self):
        movie_name = "Inception"
        actual = MovieRatingSystem.add_movie(movie_name)
        expected = f"MOVIE: {movie_name} ADDED SUCCESSFULLY ON"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
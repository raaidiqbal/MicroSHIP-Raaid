import subprocess
import unittest
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adaptable parent directory so we can import the utils file. solution that works on any os thanks to not hardcoding a path
sys.path.append(parent_dir) # adding the parent directory to the system path

from ProductionCode.utils import * # now we can easily import utils!

class TestClass(unittest.TestCase):
    def test_get_score_cowboy_bebop(self):
         """This tests whether get_score correctly returns the score when an anime that is in the dataset is inputted."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--title", "Cowboy Bebop"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), "8.78")
         expectedCode.terminate()

    def test_get_score_incorrect_title(self):
         """This tests the edge case for get_score when an invalid title is inputted. An empty string should be returned."""
         expectedCode = subprocess.Popen(["python3", "ProductionCode/utils.py", "--title", "Space Jam"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), "")
         expectedCode.terminate()
         
    def test_get_score_cowboy_bebop_lowercase(self):
            """This tests the edge case where a correct anime title is input into get_score, but the capitalization is incorrect."""
            expectedCode = subprocess.Popen(["python3", "ProductionCode/utils.py", "--title", "cowboy bepop"], 
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
            output, err = expectedCode.communicate()
            self.assertEqual(output.strip(), "")
            expectedCode.terminate()

    def test_test_filter_by_one_genre_valid(self):
         """This tests whether filter_by_genres returns the correct animes when filtering by one valid genre."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Action"],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertIn('1, 5, 6, 7, 15, 18', output.strip())
         expectedCode.terminate()

    def test_filter_by_genre_invalid_genre(self):
         """This tests the edge case for filter_by_genres where a single invalid genre is inputted. This should return an empty list."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "FakeGenre"],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()

    def test_filter_by_genres_invalid_partial(self):
         """This tests the edge case for filter_by_genre where one valid genre and one invalid genre is inputted. This should return an empty list."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Action", "FakeGenre"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()
         
    def test_filter_by_genres_many_genres(self):
         """This tests whether filter_by_genres returns the correct anime when multiple genres are inputted."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Action", "Mystery", "Drama", "Police"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertIn('7, 3254, 34430, 35798, 38770, 39764', output.strip())
         expectedCode.terminate()
         
    def test_filter_by_genres_no_input(self):
         """This tests the edge case for filter_by_genres when there is no input. An error should occur and nothing will be returned in output."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", ""],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertIn('', output.strip())
         expectedCode.terminate()
         
    def test_filter_by_genres_no_combination(self):
         """This tests the edge case for filter_by_genres when multiple valid genres are inputted, but there is no anime that fits all of the genres."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "Supernatural", "Comedy", "Action", "Hentai", "Police"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertEqual(output.strip(), '[]')
         expectedCode.terminate()
         
    def test_filter_by_genre_case_sensitive(self):
         """This tests the edge case for when a valid genre is inputted with improper capitalization. The animes that fit this genre will still be returned because filter_by_genres is not case sensitive."""
         expectedCode = subprocess.Popen(["python3", "command_line.py", "--genres", "AcTIon"],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
         output, err = expectedCode.communicate()
         self.assertIn('1, 5, 6, 7, 15, 18', output.strip())
         expectedCode.terminate()

if __name__ == "__main__":
     unittest.main()
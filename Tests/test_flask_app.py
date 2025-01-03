
import sys 
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adaptable parent directory so we can import the utils file. solution that works on any os thanks to not hardcoding a path
sys.path.append(parent_dir) # adding the parent directory to the system path

import unittest
from flask_app import *   
from ProductionCode.datasource import *
sql = DataSource()

class TestHomepage(unittest.TestCase):
    def test_route(self):
        ''' Tests the standard case for the homepage and this is also an integration test that makes sure
        that flask is working.'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Next Episode', response.data)     

    def test_route_no_title(self):
        ''' Tests the edge case of user not writing a title at all '''
        self.app = app.test_client()
        response = self.app.get('/title?title=', follow_redirects=True)
        self.assertIn(b'Page not found', response.data)

    def test_valid_title(self):
        ''' Tests for a valid title - should include the same title as the input one '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_invalid_capitalization_title(self):
        ''' Tests the edge case of a valid title typed with incorrect capitlization - 
        should show normal page for title as capitalization is automatically handled
        '''
        self.app = app.test_client()
        response = self.app.get('/title?title=trigun', follow_redirects=True)
        self.assertIn(b'Trigun', response.data)

    def test_valid_score(self):
        ''' Tests for a valid title that is one word - should include a valid score '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Trigun', follow_redirects=True)
        self.assertIn(b'Score', response.data)
        self.assertIn(b'<td class="data">8.24</td>', response.data)

    def test_valid_multiple_word_title(self):
        ''' This tests  for a valid title that is multiple words.'''
        self.app = app.test_client()
        response = self.app.get('/title?title=Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Score', response.data)
        self.assertIn(b'<td class="data">8.78</td>', response.data)

    def test_valid_genre(self):
        ''' Tests the get_genre function with a valid one word title  '''
        self.app = app.test_client()
        response = self.app.get('/title?title=Monster', follow_redirects=True)
        self.assertIn(b'Drama, Horror, Mystery, Police, Psychological, Seinen, Thriller', response.data)

    def test_valid_genre_multiple_words(self):
        ''' This tests get_genre for a valid title that is multiple words.'''
        self.app = app.test_client()
        response = self.app.get('/title?title=Cowboy Bebop', follow_redirects=True)
        self.assertIn(b'Action, Adventure, Comedy, Drama, Sci-Fi, Space', response.data)

    def test_one_genre(self):
        ''' Tests the filter_by_genre function with one valid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/search?title=&genre=Comedy").data
        self.assertIn(b'<h1>Search Results for  genres: "Comedy"', response)
        self.assertIn(b'Rec', response)
        self.assertIn(b'Pop', response)
        self.assertIn(b'MM!', response)
        self.assertIn(b'Mado', response)
        self.assertIn(b'Heya', response)

    def test_multiple_genre(self):
        ''' Tests the filter_by_genre function with more than one valid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/search?title=&genre=Comedy&genre=Drama").data
        self.assertIn(b'<h1>Search Results for  genres: "Comedy, Drama"', response)
        self.assertIn(b'Nana', response)
        self.assertIn(b'Beck', response)
        self.assertIn(b'Free!', response)
        self.assertIn(b'Trigun', response)
        self.assertIn(b'Photon', response)

    def test_no_genre(self):
        ''' Tests the filter_by_genre function with no inputted genres
        '''
        self.app = app.test_client()
        response = self.app.get("/search?title=&genre=").data
        self.assertIn(b'Page not found.', response)
    
    def test_nonexistant_genre(self):
        ''' Tests the filter_by_genre function with one invalid genre
        '''
        self.app = app.test_client()
        response = self.app.get("/search?title=&genre=schools").data
        self.assertIn(b'Page not found.', response)
        
    def test_valid_and_invalid_genre(self):
        ''' Tests the filter_by_genre function with a valid genre and an invalid genre, which should
        return a 404 error.'''
        self.app = app.test_client()
        response = self.app.get("/search?title=&genre=Seinen&genre=nonsense").data
        self.assertIn(b'Page not found.', response)
        
    def test_about_page(self):
        '''Tests if the about page is working properly.''' 
        self.app = app.test_client()
        response = self.app.get("/about").data
        self.assertIn(b"About Next Episode", response)
        
    def test_guide_page(self):
        '''Tests if the guide page is working properly.'''
        self.app = app.test_client()
        response = self.app.get("/guide").data
        self.assertIn(b"Column Descriptions", response)
        
    def test_top_25_rankings(self):
        '''Tests if the top 25 rankings are correctly displayed.'''
        self.app = app.test_client()
        response = self.app.get("/rankings").data
        self.assertIn(b"Gintama.: Shirogane no Tamashii-hen", response)
        self.assertIn(b"Kizumonogatari III: Reiketsu-hen", response)
        self.assertIn(b"Sen to Chihiro no Kamikakushi", response)
        self.assertIn(b"Mob Psycho 100 II", response)
        self.assertIn(b"Gintama.: Shirogane no Tamashii-hen - Kouhan-sen", response)
        
    def test_top_50_rankings(self):
        '''Tests if the top 50 rankings are correctly displayed.'''
        self.app = app.test_client()
        response = self.app.get("/rankings?limit=50").data
        self.assertIn(b"Hajime no Ippo: New Challenger", response)
        self.assertIn(b"Howl no Ugoku Shiro", response)
        self.assertIn(b"Natsume Yuujinchou Shi", response)
        self.assertIn(b"Ashita no Joe 2", response)
        self.assertIn(b"Seishun Buta Yarou wa Yumemiru Shoujo no Yume wo Minai", response)
        
    def test_top_75_rankings(self):
        '''Tests if the top 75 rankings are correctly displayed.'''
        self.app = app.test_client()
        response = self.app.get("/rankings?limit=75").data
        self.assertIn(b"Shingeki no Kyojin Season 3", response)
        self.assertIn(b"Kimi no Suizou wo Tabetai", response)
        self.assertIn(b"Fate/Zero 2nd Season", response)
        self.assertIn(b"Fate/stay night Movie: Heaven&#39;s Feel - II. Lost Butterfly", response)
        self.assertIn(b"Natsume Yuujinchou Go", response)
        
    def test_top_100_rankings(self):
        '''Tests if the top 100 rankings are correctly displayed.'''
        self.app = app.test_client()
        response = self.app.get("/rankings?limit=100").data
        self.assertIn(b"JoJo no Kimyou na Bouken Part 4: Diamond wa Kudakenai", response)
        self.assertIn(b"Kono Subarashii Sekai ni Shukufuku wo!: Kurenai Densetsu", response)
        self.assertIn(b"Chihayafuru 3", response)
        self.assertIn(b"Gintama Movie 1: Shinyaku Benizakura-hen", response)
        self.assertIn(b"Uchuu Kyoudai", response)
        
    def test_top_200_rankings(self):
        '''Tests if the top 200 rankings are correctly displayed.'''
        self.app = app.test_client()
        response = self.app.get("/rankings?limit=200").data
        self.assertIn(b"NHK ni Youkoso!", response)
        self.assertIn(b"Hunter x Hunter: Original Video Animation", response)
        self.assertIn(b"Fate/stay night: Unlimited Blade Works 2nd Season", response)
        self.assertIn(b"Natsume Yuujinchou Go Specials", response)
        self.assertIn(b"Made in Abyss Movie 2: Hourou Suru Tasogare", response)
        
    def test_top_26_rankings(self):
        '''Tests if the top 26 rankings are correctly displayed, which can only be accessed through
        the URL, and not our GUI.'''
        self.app = app.test_client()
        response = self.app.get("/rankings?limit=26").data
        self.assertIn(b"Shouwa Genroku Rakugo Shinjuu: Sukeroku Futatabi-hen", response)
        self.assertIn(b"Gintama.: Shirogane no Tamashii-hen", response)
        self.assertIn(b"Kizumonogatari III: Reiketsu-hen", response)
        self.assertIn(b"Sen to Chihiro no Kamikakushi", response)
        self.assertIn(b"Mob Psycho 100 II", response)

        
if __name__ == "__main__":  
    unittest.main()
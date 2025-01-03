import psycopg2
import ProductionCode.psqlConfig as config

class DataSource:
    def __init__(self):
        ''' Constructor that initiates connection to database '''
        self.connection = self.connect()

    def connect(self):
        ''' Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object '''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def get_all_anime(self):
        ''' Outputs the entire dataset - currently only includes two columns: title and score '''
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey)")
        records = cursor.fetchall()
        return records
    
    def get_all_titles(self):    
        ''' Retrieves and returns a list of all anime titles from the table '''
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT name FROM anime_table")
            titles = [record[0] for record in cursor.fetchall()]
            return titles
        except Exception as e:
            print("Something went wrong when executing the query in get_all_titles: ", e)
            return None

    def get_data_from_title(self, type):
        ''' Gets data of Anime title input by user '''
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey) WHERE lower(name) = %s;"
            cursor.execute(query, (type.lower(),))
            return cursor.fetchall()[0]

        except Exception as e:
            print ("Something went wrong when executing the query in get_data_from_title: ", e)
            print(type)
            return None

    def fuzzy_match_name(self, title, genres, blacklist):
        ''' Allows site to search beyond exact matches '''
        cursor = self.connection.cursor()
        query = "SELECT * FROM (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey) WHERE lower(name) LIKE %s " 
        
        if len(genres) > 0:
            for gen in genres:
                query += f"and lower(genres) like '%%{str(gen).lower()}%%' "
                
        if len(blacklist) > 0:
            for b in blacklist:
                query += f"and not (lower(genres) like '%%{str(b).lower()}%%') "
        
        query += "order by levenshtein(name, %s) asc;"
        print(query)
        cursor.execute(query, ('%%'+title.lower()+'%%', title.lower(),))
        return cursor.fetchall()
        
    def filter_by_genres(self, g):
        ''' Filters the table by a specific genre or multiple genres and displays them '''
        try:
            cursor = self.connection.cursor()
            
            try:
                query = f"select * from (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey) where lower(genres) like '%{str(g[0]).lower()}%'"
                for gen in g[1:]:
                    query += f"and lower(genres) like '%{str(gen).lower()}%'"
                query += ";"
            except IndexError:
                query = "select * from (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey);"
            
            cursor.execute(query)
            return cursor.fetchall()
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
    def get_random_anime(self):
        ''' Returns one random anime entry from the table '''
        try: 
            cursor = self.connection.cursor()
            
            try: 
                query = f"SELECT * FROM (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey) ORDER BY RANDOM() LIMIT 1;"
                cursor.execute(query)
                return cursor.fetchall()
        
            except Exception as e:
                print ("Something went wrong when executing the query: ", e)
                return None
        
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def get_top_ranked_anime(self, limit):
        ''' Retrieves the top ranked anime based on score '''
        try:
            cursor = self.connection.cursor()
            query = f"""
            SELECT * FROM (((anime_table natural join ratingkey) natural join typekey) natural join sourcekey)
            WHERE score IS NOT NULL
            ORDER BY score DESC
            LIMIT %s;
            """
            cursor.execute(query, (limit,))
            return cursor.fetchall()
        except Exception as e:
            print("Something went wrong when executing the query in get_top_ranked_anime: ", e)
            return None
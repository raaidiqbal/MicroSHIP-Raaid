import csv

dataset = open('Data/command_line_testing_subset.csv', newline='')

dataset_reader = csv.reader(dataset)
dataset_read = [f for f in dataset_reader]

def get_score(title):
    """ This function returns the score as found in the database based on the name of a show."""
    for row in dataset_read: # looping through rows in the dataset
        if row[1] == title: # if title name in the dataset matches the input
            return row[2] # return!
   
def get_genre(title):
    """ This function returns the genre as found in the database based on the name of a show """
    for row in dataset_read:
        if row[1] == title:
            return row[3]

def filter_by_genres(genres : list):
    """ This function returns a list of anime ids that match all specified genres."""
    return_rows = [] # collections of rows to return
    for ix, row in enumerate(dataset_read[1:]):
        genres_match = [0] * len(genres) # bitmap for matched genres
        for i, genre in enumerate(genres):
            if genre.lower() in row[3].lower():
                genres_match[i] = 1 # if match, set to 1
        
        if sum(genres_match) == len(genres_match): # if all genres are matched
            return_rows.append(ix) # this bit of the code has been changed to return the indices of the items instead of their ids
            
    return return_rows
"""
@author: Arnav Garg
@date: 08/20/2018

How To Run
-----------
> Help menu
$ python main.py --help

> Code run
$ python main.py -b sample_book_json.txt -w sample_genre_keyword_value.csv

> Run Unit Tests
$ python unit-tests.py -v
"""

import re
import ast
import copy
import argparse
import sys


class Genre():
    """Class to store the genre names. Used by various
       other classes to make the code more maintainable.
    """
    action = 'action'
    mystery = 'mystery'
    biography = 'biography'
    sci_fi = 'sci-fi'
    literary_fiction = 'literary fiction'


class BookDetails:
    """Stores all the details for each book. 

    Attributes:
        title (str): Title of the book
        description (str): Description of the book
        genre_points(dict): Mapping of genre to its subsequent details. 

    """

    def __init__(self, title, description):
        self.title = title
        self.description = description
        genre_details = {
            'unique_words': 0,
            'total_points': 0,
            'total_words': 0,
            'score': 0
        }
        self.genre_points = {
            Genre.action: copy.deepcopy(genre_details),
            Genre.mystery: copy.deepcopy(genre_details),
            Genre.biography: copy.deepcopy(genre_details),
            Genre.sci_fi: copy.deepcopy(genre_details),
            Genre.literary_fiction: copy.deepcopy(genre_details)
        }
    
    def compute_possible_genre(self):
        """ Compute the score of the genre for a particular book based on the
            unique_words, total_points, total_words. 
        """
        for genre, details in self.genre_points.items():
            if details['unique_words'] > 0:
                details['score'] = (details['total_words']) * (details['total_points']/details['unique_words'])
        self.genre_points = dict(reversed(sorted(self.genre_points.items(), key=lambda x: x[1]['score'])))
        return [(genre, details['score']) for genre, details in self.genre_points.items() if details['score'] > 0]


class GenrePoints:
    """Stores all the details for each word. 

        Attributes:
        genre2points(dict): Mapping of genre to its subsequent details. 

    """
    def __init__(self):
        self.genre2points = {
            Genre.action: 0,
            Genre.mystery: 0,
            Genre.biography: 0,
            Genre.sci_fi: 0,
            Genre.literary_fiction: 0
    }

    def update(self, genre, points):
        """Update the points for a particular genre for a word. 
        """
        self.genre2points[genre] = points

    def get_genres(self):
        """ Returning all the genres with points more than 0. 
        """
        return [(key, value) for key, value in self.genre2points.items() if value > 0]


def update_book_genre_score(book, word2points) -> None:
    """Goes over each unique word and checks if that word exists in
       books description (how many counts), if it does, it adds the corresponding
       genres associated with the word and updates the BookDetails.

    Args:
        book: BookDetails object for that a book.
        word2points: Mapping of a unique word to its GenrePoints object.

    Returns:
        None

    """
    for word in word2points:
        value = sum(1 for _ in re.finditer(r'%s' % re.escape(word), book.description))
        if value > 0:
            # Get all the genres associated with that word.
            associated_genres = word2points[word].get_genres()
            # Updating the book object for each genre.
            for (genre, points) in associated_genres: 
                book.genre_points[genre]['unique_words'] += 1
                book.genre_points[genre]['total_points'] += points
                book.genre_points[genre]['total_words'] += value


def update_keyword(word2points, keyword, genre, points) -> None:
    """Updaing the word2points dict which has a mapping of word 
       to GenrePoints objects. This function checks in the genre
       has already been added or not. If the mapping exists, then
       it updates the object else created one. 

    Args:
        word2points: mapping of words to GenrePoints
        keyword: Unique word. 
        genre: The genre associated with that word. 
        points: The points for that genre and word group. 

    Returns:
        None

    """
    if keyword in word2points:
        word2points[keyword].update(genre, points)
    else:
        genre_points = GenrePoints()
        genre_points.update(genre, points)
        word2points[keyword] = genre_points


def get_word_mapping(genre_list_filename) -> dict:
    """Read the CSV file and get a mapping of word to GenrePoints objects. 

    Args:
        genre_list_filename: The filename of the CSV file containing the
                             word/point information.

    Returns:
        Returns a dict with word to GenrePoint mapping. 

    """
    word2points = dict()
    with open(genre_list_filename, 'r') as f:
        for line_num, line in enumerate(f):
            # Ignoring line_num 0 as that's the heading. 
            if line_num:
                line = line.split(', ')
                genre, keyword, points = line
                points = int(points)
                update_keyword(word2points, keyword, genre, points)
    return word2points


def get_list_of_books(json_filename) -> list:
    """Read the txt file and get the list of books in BookDetails Object.

    Args:
        json_filename: filename of the text file..

    Returns:
        list of books in BookDetails Object.

    """
    json_data = ''
    list_of_books = []
    with open(json_filename, 'r') as f:
        json_data = f.read()
    json_data = ast.literal_eval(json_data)     # Converting the string into list of dict object. 
    for book_details in json_data:
        title = book_details["title"]
        description = book_details["description"]
        book = BookDetails(title, description)
        list_of_books.append(book)
    return list_of_books


if __name__ == '__main__':
    # Parsing the command line arguements.
    parser = argparse.ArgumentParser(description='Arnav - BookBub Challenge')
    parser.add_argument('--books', 
                        '-b', 
                        help='filename of the txt file containing data on the books. (Title and Description)',
                        required=True)
    parser.add_argument('--words', 
                        '-w', 
                        help='filename of the csv file containing data on the genre, words and points',
                        required=True)
    args = parser.parse_args()
    json_filename = args.books
    genre_list_filename = args.words

    # Reading the json_file and getting the list of all the books back.
    list_of_books = get_list_of_books(json_filename)

    # Reading the Genre-Keyword File and getting a mapping of words to details
    word2points = get_word_mapping(genre_list_filename)

    # Sorting the list based on the title.
    # Would be needing when I display information.
    list_of_books = sorted(list_of_books, key=lambda x: x.title)

    # Now iterating over each book to compute the possible genres.
    for book in list_of_books:
        update_book_genre_score(book, word2points)
        possible_genres = book.compute_possible_genre()
        # Printing the solution for each book. 
        print(book.title)
        for i, (genre, score) in enumerate(possible_genres):
            if i > 2:   # Not print more than 3.
                break
            print("{}, {:.0f}".format(genre, score))
        print()






    

from main import get_list_of_books, get_word_mapping
import unittest

json_filename = 'sample_book_json.txt'
csv_file = 'sample_genre_keyword_value.csv'

class TestCode(unittest.TestCase):

    def test_get_list_of_books(self):
        self.assertEqual(len(get_list_of_books(json_filename)), 2)

    def test_get_word_mapping(self):
        self.assertEqual(len(get_word_mapping(csv_file)), 13)

if __name__ == '__main__':
    unittest.main()


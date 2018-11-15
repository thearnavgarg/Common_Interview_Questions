Name: Arnav Garg
Email: arnavgarg@cs.ucla.edu


Requirements
------------
1. Python Version: 3.7.0
2. Two files in the in same directory:
    a. sample_book_json.txt
    b. sample_genre_keyword_value.csv


How To Run
-----------
> Help menu
$ python main.py --help

> Code run
$ python main.py -b sample_book_json.txt -w sample_genre_keyword_value.csv

> Run Unit Test
$ python unit-tests.py -v


Further Questions
-----------------
> Any interesting trade-offs or edge cases you ran into?
1. I assumed that each book will have only one description.
(i.e. each book will appear only once in the list of books given.)

2. Due to the time constraint, I didn't get a chance to write more unit testcases. 

3. The genres mentioned in the testcase are the only ones we need to categorize in.  
   However, we can add more in the Genre class if needed.


> Approximately how long you spent (this is not timed, but it’s helpful for us)
2 hours 35 mins ==> main.py
10 mins => unit tests
10 mins => documentation
Total time = ~3 hrs


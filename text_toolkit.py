import os
import re

def word_frequency(text_or_path):
    """
    Count how frequently each word appears in the text.
    Can accept a string or a file path to a text file.
    """
    unique_words = {}
    if not isinstance(text_or_path, str):
        raise TypeError ("Only 'str' data with text or filepath allowed")
    
    def counting_word_frequency(data:str)->None:
        ''' Function counts the unique words in the given text data
        '''
        nonlocal unique_words
        # Remove all special characters (keeping only letters, numbers, and spaces)
        cleaned_string = re.sub(r'[^A-Za-z0-9\s]', '', data)
        # convert string data to lower case (to avoid confict between capital and 
        # non-capital words)
        cleaned_string = cleaned_string.lower()

        # For each word in the text
        for data in cleaned_string.split():
            if data in unique_words.keys():
                unique_words[data] += 1
            else:
                unique_words[data] = 1
    
    # Function supports only two types of strings
    #   1. A valid file path - If exists it reads and processes it
    #   2. A text data - It processes directly
    if os.path.isfile(text_or_path):
        # Open the file, read each line and send for processing
        with open(text_or_path, 'r') as file:
            for row in file:
                counting_word_frequency(row)

    else:
       # Text data, send the raw text for processing
       counting_word_frequency(text_or_path)

    return unique_words

def unique_words(text_or_path):
    """
    Extract unique words from the text.
    """
    pass

def word_cooccurrence_matrix(text_or_path, window=2):
    """
    Create a word co-occurrence matrix with a given window size.
    """
    pass

def text_generator(text_or_path):
    """
    A generator that yields one line of text at a time.
    """
    pass


'''
Create a Text Analytics Toolkit
Overview: Create a Python module called text_toolkit that provides a set of text analysis tools. 
This module will include functionalities such as:

Counting word frequencies,
Extracting unique words,
Finding word co-occurrences,
Generating word sequences,
Handling files via context managers,
Handling large text datasets efficiently using generators and iterables.
The final module should also be version-controlled using Git.
 

Assignment Breakdown:

Module Creation: Create a Python module called text_toolkit.py containing several 
functions for text processing and analysis.

The module should contain the following tools:
Word frequency counter: Count how often each word appears in a given text file.
Unique word extractor: Extract all unique words in the text.
Word co-occurrence matrix: Create a matrix showing how frequently words appear next to each other in the text.
Text generator: A generator function that yields one line of the text at a time to process large files efficiently.
Functionality Requirements:

The module should support large text files by using generators to handle memory efficiently.
Functions should accept both file paths and string inputs.
Use context managers to ensure proper file handling.
Encourage the use of scopes, closures, and functional parameters where applicable.
The module should allow for reuse and easy integration into larger AI projects (e.g., for NLP tasks).
Create a README.md file that explains how to use each function in the module, including sample usage and examples.
Once done, run session14_test.py using Actions, and upload a screenshot of your action's result on your README.md file. Share the link to your README.md file along with other code
'''
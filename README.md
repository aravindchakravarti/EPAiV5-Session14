# Submission Details
Name: Aravind D. Chakravarti

Email: aravinddcsadguru@gmail.com

# Code Details

`text_toolkit.py` is a Python module that provides various text processing functions. These functions can handle both plain text strings and file paths to text files. The module includes functions for counting word frequencies, extracting unique words, generating word co-occurrence matrices, and yielding lines of text.

## Functions

### `word_frequency(text_or_path, filter_func=None)`

Counts the frequency of each word in the given text, which can be provided as either a string or a file path.

**Parameters:**
- `text_or_path` (str): The input data, which can be either a string of text or a file path to a text file.
- `filter_func` (callable, optional): A function used to filter the words before counting their frequency. If not provided, all words are counted. The filter function should take a string (word) as input and return `True` to include the word in the count or `False` to exclude it.

**Returns:**
- `dict`: A dictionary where the keys are unique words and the values are their corresponding frequency counts.

**Raises:**
- `TypeError`: If `text_or_path` is not a string.

**Example usage:**
```python
word_frequency("This is a test text. This test is only a test.", lambda word: len(word) > 2)
```


### `unique_words(text_or_path)`

Extracts unique words from a given text or file path.

**Parameters:**
- `text_or_path` (str): Input can either be a string containing text or a file path to a text file.

**Returns:**
- `set`: A set of unique words in lowercase from the input text.

**Raises:**
- `TypeError`: If the input is not a string.
- `IOError`: If the file path provided is invalid or cannot be read.

**Example usage:**
```python
unique_words("This is a test text. This test is only a test.")
```


### `word_cooccurrence_matrix(text_or_path, window=2)`

Returns the word co-occurrence matrix from a given text or file path.

**Parameters:**
- `text_or_path` (str): Input can either be a string containing text or a file path to a text file.
- `window` (int): The window size for fetching adjacent words.

**Returns:**
- `list`: A list containing tuples of word co-occurrence pairs.

**Raises:**
- `TypeError`: If the input is not a string.
- `TypeError`: If `window` is not an integer.

**Example usage:**
```python
word_cooccurrence_matrix("This is a test text. This test is only a test.", window=2)
```



### `text_generator(text_or_path)`

A generator function that yields one line of text at a time, either from a file or a string.

**Parameters:**
- `text_or_path` (str): The input data, which can be either a file path or a string.

**Yields:**
- `str`: One line of text at a time, either from the file or the cleaned string.

**Raises:**
- `TypeError`: If the input is not a string or file path.
- `IOError`: If there is an error opening or reading from the file.

**Example usage:**
```python
text_generator("This is a test text. This test is only a test.")
```
# Expand the README file to explain the code and how to run it. Here is an example of what is expected:
import text_toolkit as tt

# Example usage:
freq = tt.word_frequency('example.txt')
print(freq)

unique = tt.unique_words('example.txt')
print(unique)

cooccurrence_matrix = tt.word_cooccurrence_matrix('example.txt')
print(cooccurrence_matrix)

# Example of using the text generator
for line in tt.text_generator('example.txt'):
    print(line)

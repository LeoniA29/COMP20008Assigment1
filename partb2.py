# Part B Task 2
# Importing Libraries
import re
import os
import sys

# define a function for this preprocessing
def preprocess_file(file):
    """Gets the text from a file.
    Returns
    -------
    
        the text after pre-processing
      """
    with open(file, 'r') as fd:
         line = fd.read()

         # filter out non-alphabetic characters using Regular Expression
         alpha_process = re.sub(r'[^a-zA-Z"\t""\n""\s"]', ' ', line)

            
         # filter out all tabs, newlines, and spaces into one whitespace
         space_process = re.sub(r'^\n+|\t+|\s+|\s\s+', ' ', alpha_process)
            
         # make all uppercase characters lowercase
         lower_process = space_process.lower()
            
    return lower_process

file = sys.argv[1]
print(preprocess_file(file))
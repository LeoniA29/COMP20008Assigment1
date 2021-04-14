## Part B Task 4
# Importing Libraries
import re
import sys
import pandas as pd
import nltk
import os
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()

# preprocessing function from partb2
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

# read csv data from partb1
df_b1 = pd.read_csv('partb1.csv')
df_b1.drop('Unnamed: 0', inplace=True, axis=1)

# extract key words from commandline
# use porter stemmer for more advanced search
keywords = sys.argv[1:]
keywords = [ps.stem(w) for w in keywords]
print(keywords)

# the file_string needs to be processed and tokenized 
# loop through each file in cricket folder and find matches for the keywords
for fname, ID in zip(df_b1['filename'], df_b1['documentID']):
    file_string = preprocess_file("cricket/"+fname)
    
    file_tokenize = nltk.word_tokenize(file_string)
    
    if (all(w in file_tokenize for w in keywords)):
        results = True
    else:
        results = False
        
    if results == True:
        print(ID)
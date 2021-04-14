## Part B Task 1
# Importing Libraries
import re
import pandas as pd
import os
import glob

def read_file(file):
    """Gets the text from a file.
    Returns
    -------
    str
        the Document ID of the cricket file
      """
    with open(file, 'rt') as fd:
         file_string = fd.read()
         #display(file_string)
         # filter out Document ID using Regular Expression
         x = re.search(r"[a-zA-Z]{4}\-\d{3}[a-zA-Z]?", file_string)
         #display(x.group())
    return x.group()

# Create a series of text files for Dataframe
all_files = os.listdir("cricket/")
all_files = sorted(all_files) # sort the txt files
txt_files = filter(lambda x: x[-4:] == '.txt', all_files) # filter out files that are not txt

filename = pd.Series(txt_files)


# Use glob to add the path name in front of the text files
# Used for iterating in the read_file function
myFilesPaths = glob.glob(r'cricket/*.txt')


# run read_file function and create Document ID series for datafram
output_DocID = map(read_file, sorted(myFilesPaths))
DocID = list(output_DocID)
DocID = pd.Series(DocID)


# create DataFrame and save as csv file
df_b1 = df = pd.DataFrame({"filename": filename, "documentID": DocID})

df_b1.to_csv("partb1.csv") 
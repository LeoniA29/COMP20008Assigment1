## Part B Task 5
# Importing Libraries
import re
import sys
import pandas as pd
import nltk
import os
import math
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Function taken from: Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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
#print(keywords)

# initializing strings for TF-IDF processing
docID = []
valid_docs = []

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
        docID.append(ID)
        #print(docID)
        valid_docs.append(file_string)
             
#print(valid_docs)        
# settings that you use for count vectorizer will go here 
tfidf_vectorizer=TfidfVectorizer(use_idf=True) 
 
# send all valid documents with a query match 
tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(valid_docs)
#print(tfidf_vectorizer_vectors)
# get the first vector out (for the first document)

first_vector_tfidfvectorizer= tfidf_vectorizer_vectors[0]
 
#place tf-idf values in a pandas data frame 
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(),
                  index=tfidf_vectorizer.get_feature_names(),columns=["tfidf"]) 

df.sort_values(by=["tfidf"],ascending=False)

#print(df)

# make keywords vector for cosine similarity
keywords_vector = tfidf_vectorizer.transform(keywords)

cosine_score = []

for doc_vector in tfidf_vectorizer_vectors:
    # conduct cosine similarity
    cosine_score.append(cosine_similarity(keywords_vector, doc_vector, dense_output=True))
    
#display(cosine_score)
# round the cosine scores to 4th decimal place
#cosine_score = [round(score, 4) for score in cosine_score]

df_final = pd.DataFrame({"documentID": docID, "score": cosine_score})  
df_final.sort_values(by=["score"],ascending=False)
print(df_final)

#i'm sorry i'm not sure how to get out of that cosine_score numpy array to round to 4th decimal place
# import beautifulsoap package to get the data from url
from bs4 import BeautifulSoup
import urllib.request
#import nltk package
import nltk
# import stemmer and lemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import trigrams
from nltk import ne_chunk
'''Get the text from the python programming language url'''
# Read the web url into a variable
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# use urllib to open the url
res = urllib.request.urlopen(url)
plain_text = res
# Use beautiful soup to get the content of webpage
soup = BeautifulSoup(plain_text, "html.parser")
# get the text from the website
data = soup.get_text("\n")
#print(data)
# open the out.txt in write mode and write the website data to out file
with open("out.txt",'w') as f:
    f.write(str(data.encode("utf-8")))
# tokenize words
tokenize_words = nltk.word_tokenize(data)

print("Tokenized words")
print("----------------------------------------------------------------------------------------------------------------")
print(tokenize_words)
print("-----------------------------------------------------------------------------------------------------------------")
print("POS Tagging")
print("----------------------------------------------------------------------------------------------------------------")
# apply parts of speech to words
parts_of_speech=nltk.pos_tag(tokenize_words)
print(parts_of_speech)
print("-----------------------------------------------------------------------------------------------------------------")
print("Trigrams")
print("------------------------------------------------------------------------------------------------------------------")
# import trigrams to divide the data into triplets
print(list(trigrams(tokenize_words)))
print("------------------------------------------------------------------------------------------------------------------")
print("Named entity recognition")
print("------------------------------------------------------------------------------------------------------------------")
# apply named entity recognition to the tagged words
print(ne_chunk(parts_of_speech))
print("-------------------------------------------------------------------------------------------------------------------")

# open the out.txt file
with open("out.txt",'r') as f:
    # split into lines
    lines=f.read().splitlines()
    for l in lines:
        # split words in a line
        words=l.split()
        # apply the stemmer to the words
        pstem=PorterStemmer()
        # apply the lemmatization to the words
        word_lemmatizer=WordNetLemmatizer()
        for i in words:
            print("Stemmed words")
            print("-------------")
            print(pstem.stem(i))
            print("-------------")
            print("Lemmatized words")
            print("--------------")
            print(word_lemmatizer.lemmatize(i))
            print("--------------")








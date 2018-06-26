from bs4 import BeautifulSoup
import urllib.request
import nltk
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

data = soup.get_text("\n")
#print(data)
with open("out.txt",'w') as f:
    f.write(str(data.encode("utf-8")))
tokenize_words = nltk.word_tokenize(data)
'''
print("Tokenized words")
print("----------------------------------------------------------------------------------------------------------------")
print(tokenize_words)
print("-----------------------------------------------------------------------------------------------------------------")
print("POS Tagging")
print("----------------------------------------------------------------------------------------------------------------")
parts_of_speech=nltk.pos_tag(tokenize_words)
print(parts_of_speech)
print("-----------------------------------------------------------------------------------------------------------------")
print("Trigrams")
print("------------------------------------------------------------------------------------------------------------------")
print(list(trigrams(tokenize_words)))
print("------------------------------------------------------------------------------------------------------------------")
print("Named entity recognition")
print("------------------------------------------------------------------------------------------------------------------")
print(ne_chunk(parts_of_speech))
print("-------------------------------------------------------------------------------------------------------------------")

'''
with open("out.txt",'r') as f:
    lines=f.read().splitlines()
    for l in lines:
        words=l.split()
        pstem=PorterStemmer()
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








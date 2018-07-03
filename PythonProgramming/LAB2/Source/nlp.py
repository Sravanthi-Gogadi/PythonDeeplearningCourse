from nltk.stem import WordNetLemmatizer
from nltk.util import bigrams
from collections import Counter
import nltk.data


f= open('sample.txt', 'r')
data=f.read() #reading the data from a file
words = nltk.word_tokenize(data) #splitting into words
wordLemmatizer = WordNetLemmatizer() #creating an object for WordNetLemmatizer
for i in words:
    print("Lemmatized word for {} is: {} ".format(i,wordLemmatizer.lemmatize(i))) #Applying lemmatization for each word
sentences=nltk.sent_tokenize(data) #splitting into sentences
bi_grams= bigrams(words) #getting the bigrams
count_grams=[]
counts = Counter(bi_grams) #counting the occurence of bigrams
most_common_bigrams=counts.most_common(5) #gettng the most common 5 bigrams and counts
most_common_list = [i[0] for i in most_common_bigrams] #extracting just the bigrams
print("-----------------------------------------------------------------------------------------------------------------")
print("The most common bigrams are:")
print(most_common_list)
print("-----------------------------------------------------------------------------------------------------------------")
summary = ''
for s in sentences:

    for each in most_common_list:
        if each[0]+' '+each[1] in s and s not in summary: #if the bigram in sentence and not repeated
            summary = summary+s

print("The summary is:\n")
print(summary)
print("-----------------------------------------------------------------------------------------------------------------")












import nltk
import string
from heapq import nlargest
nltk.download('stopwords')
nltk.download('punkt')

def summarization(data):
    text = data
    if text.count(". ") > 20:
        length = int(round(text.count(". ")/10, 0))
    else:
        length = 1
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    processed_text =[word for word in nopunc.split() if word.lower() not in nltk.corpus.stopwords.words('english')]      
    word_freq = {}
    for word in processed_text:
        if word not in word_freq:
         word_freq[word] = 1
    else:
        word_freq[word] = word_freq[word] + 1
    max_freq = max(word_freq.values())
    print(word_freq)
    print(max_freq)
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/max_freq)
    sent_list = nltk.sent_tokenize(text)
    sent_score = {}

    
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] = sent_score[sent] + word_freq[word]     
                
    summary_sents = nlargest(length, sent_score, key = sent_score.get)
    summary = ' '.join(summary_sents)
    return summary        
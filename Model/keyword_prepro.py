from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import copy
import re

stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def my_lemmatizer(word_and_tag):
    word = word_and_tag[0]
    tag = word_and_tag[1]
    if tag.startswith('J'):
        return lemmatizer.lemmatize(word,wordnet.ADJ)
    elif tag.startswith('V'):
        return lemmatizer.lemmatize(word,wordnet.VERB)
    elif tag.startswith('N'):
        return lemmatizer.lemmatize(word,wordnet.NOUN)
    elif tag.startswith('R'):
        return lemmatizer.lemmatize(word,wordnet.ADV)
    else:
        return word


def preprocess(input_string, additional_stopwords = None, mode = None):
    local_stopwords = copy.copy(stopwords)
    if additional_stopwords != None:
        local_stopwords.extend(additional_stopwords)
    lower = input_string.lower()
    lower = word_tokenize(lower)
    mid = []
    for word in lower:
        if not word in local_stopwords:
            mid.append(word)
    mid = ' '.join(mid)
    mid = re.sub('_',' ', mid)
    mid = re.sub(r'[^\w\s]',' ', mid)
    mid = re.sub('\d', ' ', mid)
    mid = re.sub('\s+',' ', mid )
    mid = word_tokenize(mid)
    mid = pos_tag(mid)
    if mode == None:
        pos_tagged = mid
    else:
        pos_tagged = []
        for item in mid:
            if item[1].startswith(mode):
                pos_tagged.append(item)

    lemmatized = list(map(my_lemmatizer,pos_tagged))
    content = []
    for word in lemmatized:
        if not word in local_stopwords:
            content.append(word)
    return content

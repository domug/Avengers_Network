import os
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from keyword_prepro import *





DATA_PATH = './data/wiki'
document_list = []
collected_characters = os.listdir(DATA_PATH)

# 캐릭터별 위키설명을 하나의 리스트에 저장
for file in os.listdir(DATA_PATH):
    with open(os.path.join(DATA_PATH, file), 'r', encoding='utf-8') as f:
        document = f.read()
    document_list.append(document)



# 텍스트 전처리
documents_filtered = []
for doc in document_list:
    document_filtered =''
    for word in preprocess(doc):
        document_filtered = document_filtered+' '+word
    documents_filtered.append(document_filtered)


# TFIDF로 텍스트 벡터화
vectorizer = TfidfVectorizer(
    min_df=1,
    ngram_range = (1,2),
    lowercase = True,
    tokenizer = lambda x: x.split())

input_matrix = vectorizer.fit_transform(documents_filtered)

id2vocab = {vectorizer.vocabulary_[token]:token
           for token in vectorizer.vocabulary_.keys()}



# 저장된 위키문서와 캐릭터명을 통일
def name_matching(character):
    character = character.lower()
    matched = None
    for names in collected_characters:
        if len(re.findall(character, names.lower())) != 0:
            matched = names
    return matched


# 특정 캐릭터와 관련된 키워드(TFIDF similarity) 추출
def tfidf_keywords(character, n):

    character = name_matching(character)
    print(character)

    if character is not None:
        index = collected_characters.index(character)
        print(index)
        curr_doc, result = input_matrix[index], []
        for idx, el in zip(curr_doc.indices, curr_doc.data):
            result.append((id2vocab[idx], el))
        keyword = sorted(result, key=lambda x: x[1], reverse=True)[:n]

        for i, ele in enumerate(keyword):
            print("{}. {}".format(i, ele))

    else:
        print("선택하신 캐릭터에 대한 위키 정보가 없습니다.")
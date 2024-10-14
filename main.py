import string
from collections import defaultdict

def searchForWordsInSentences():
    results = []
    n = int(input("Podaj liczbę zdań: "))
    
    word_to_docs = defaultdict(list)
    
    for i in range(n):
        sentence = input(f"Podaj zdanie nr {i + 1}: ")
        words = sentence.split()
        word_count = defaultdict(int)

        for word in words:
            clean = clean_word(word)
            if clean:
                word_count[clean] += 1

        for word, count in word_count.items():
            word_to_docs[word].append((i, count))

    m = int(input("Podaj liczbę szukanych słów: "))
    
    for j in range(m):
        query = input(f"Podaj słowo nr {j + 1}: ")
        clean_query = clean_word(query)

        if clean_query in word_to_docs:
            result = sorted(word_to_docs[clean_query], key=lambda x: (-x[1], x[0]))
            results.append([doc[0] for doc in result])
        else:
            results.append([])
    
    for result in results:
        print(result)

def clean_word(word):
    return word.strip(string.punctuation).lower()

searchForWordsInSentences()

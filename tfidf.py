import math

class TFIDF:
    stopwords = {'и', 'в', 'на', 'с', 'по', 'для', 'от', 'из', 'о', 'к', 'за', 'не'}

    def __init__(self, documents):
        self.documents = documents
        self.doc_count = len(documents)

    def get_tf(self, word, doc_number):
        words = self.documents[doc_number].split()
        word_count = words.count(word)
        return word_count / len(words)

    def get_idf(self, word):
        doc_count_with_word = sum(1 for doc in self.documents if word in doc.split())
        return math.log(self.doc_count / (doc_count_with_word + 1))

    def get_tf_idf(self, word, doc_number, ignore_stopwords=True):
        if ignore_stopwords and word in TFIDF.stopwords:
            return 0
        tf = self.get_tf(word, doc_number)
        idf = self.get_idf(word)
        return tf * idf

if __name__ == "__main__":
    documents = [
        "Кошка сидит на окне",
        "Собака лает на прохожих",
        "Птицы поют утром",
        "На столе стоит ваза с цветами",
        "Машина едет по дороге",
        "Дети играют на площадке"
    ]
  
    tfidf = TFIDF(documents)

    word = 'на'
    doc_number = 0

    print(f"TF: {tfidf.get_tf(word, doc_number)}")
    print(f"IDF: {tfidf.get_idf(word)}")
    print(f"TF-IDF: {tfidf.get_tf_idf(word, doc_number)}")

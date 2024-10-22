class WordCounter:
    def __init__(self, words):
        self.words = words

    def count_words(self):
        for word in conting_words:
            print(f"{word}:{words.count(word)}")

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
conting_words = set(words)
W = WordCounter(words)
print(W.count_words())

    
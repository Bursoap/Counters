import re
from collections import defaultdict


class CountWords:
    def __init__(self):
        text = input("Enter your text here: ")
        self.words_list = re.sub(r'[.,;/:!?]?[0-9]?', '', text.lower()).strip().split()
        limit = 0
        while not limit:
            try:
                limit = int(input("Enter top words limit: "))
            except ValueError:
                print("Input limit should be a number")
        self.count_top_words(limit)

    def count_top_words(self, limit):
        count_dict = defaultdict(int)
        if self.words_list:
            for word in self.words_list:
                count_dict[word] += 1
            result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:limit]
            for word, quantity in result:
                print(f"Char {word} in sequence repeated {quantity} times")
            return result
        else:
            print("There is no words in your text")


if __name__ == "__main__":
    run = CountWords()

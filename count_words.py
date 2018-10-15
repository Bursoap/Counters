from collections import defaultdict


class CountWords:
    def __init__(self):
        text = input("Enter your text here: ")
        self.words_list = text.lower().split(' ')
        limit = 0
        while not limit:
            try:
                limit = int(input("Enter top words limit: "))
            except ValueError:
                print("Input limit should be a number")
        self.count_top_words(limit)

    def count_top_words(self, limit):
        count_dict = defaultdict(int)
        for word in self.words_list:
            count_dict[word] += 1
        result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:limit]
        for word, quantity in result:
            print(f"Char {word} in sequence repeated {quantity} times")
        return result


if __name__ == "__main__":
    run = CountWords()
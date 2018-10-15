from collections import defaultdict


class CharsCounter:
    def __init__(self):
        self.seq = input("Enter your string here: ")
        limit = 0
        while not limit:
            try:
                limit = int(input("Enter top chars limit: "))
            except ValueError:
                print("Input limit should be a number")
        self.count_top_chars(limit)

    def count_top_chars(self, limit):
        count_dict = defaultdict(int)
        for char in self.seq:
            count_dict[char] += 1
        result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:limit]
        for char, quantity in result:
            print(f"Char {char} in sequence repeated {quantity} times")
        return result

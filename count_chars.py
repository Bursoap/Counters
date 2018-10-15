class CharsCounter:
    def __init__(self, sequence):
        if isinstance(sequence, str):
            self.seq = sequence
        else:
            raise ValueError("sequence type should be string")
        self.count_chars()

    def count_chars(self):
        count_dict = {}
        for char in self.seq:
            val = count_dict.get(char, 0) + 1
            count_dict[char] = val
        result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:3]
        for char, quantity in result:
            print(f"Char {char} in sequence repeated {quantity} times")
        return result

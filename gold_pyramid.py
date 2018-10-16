numerals = [[0],
          [0, 0],
        [0, 0, 1],
       [1, 1, 7, 2],
      [1, 5, 0, 0, 0]]


class Pyramid:
    def __init__(self, pyramid, method='down'):
        self.pyramid = pyramid
        self.row_level = -2
        print(self.get_best_sum(method=method))

    def get_best_sum(self, method):
        if method == 'up':
            return self.get_up_sum()
        elif method == 'down':
            down_row_data = [(num, [idx]) for idx, num in enumerate(self.pyramid[-1])]
            return self.get_down_sum(down_row_data)

    def get_up_sum(self):
        pass

    def get_down_sum(self, down_row_data):
        result = []
        for idx, num in enumerate(self.pyramid[self.row_level]):
            first_down_sum = down_row_data[idx][0]
            second_down_sum = down_row_data[idx+1][0]
            first_down_indexes = down_row_data[idx][1]
            second_down_indexes = down_row_data[idx+1][1]
            if first_down_sum > second_down_sum:
                new_sum = first_down_sum + num
                indexes = first_down_indexes + [idx]
            else:
                new_sum = second_down_sum + num
                indexes = second_down_indexes + [idx]
            result.append((new_sum, indexes))
        if len(result) == 1:
            return result[0]
        else:
            self.row_level -= 1
            return self.get_down_sum(result)


if __name__ == '__main__':
    x = Pyramid(numerals, method='up')

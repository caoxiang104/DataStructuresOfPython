from Chapter4_Arrays_and_Linked_Structures.exercise4_3.arrays import Array


class Matrix(object):
    def __init__(self, row, col, fill_value=None):
        self._data = Array(row)
        for i in range(row):
            self._data[i] = Array(col, fill_value)

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result

    def __add__(self, other):
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                other[i][j] = other[i][j] + self._data[i][j]
        return other


def main():
    row = 3
    col = 3
    matrix = Matrix(row, col)
    for i in range(row):
        for j in range(col):
            matrix[i][j] = i * row + j
    print(matrix)
    matrix2 = matrix
    print(matrix + matrix2)


if __name__ == '__main__':
    main()
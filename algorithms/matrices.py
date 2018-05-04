# general logic of a matrix

# n = 3
# m = 4
# a = [0] * n
# for i in range(n):
#     a[i] = [0] * m
# print(a)


# Write an algorithm such that if an element in am MxN matrix is 0, its entire row and column are set to 0

class MyMatrix:
    """A class that takes some matrix as an argument"""
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

    def __str__(self):
        """Representation of a matrix"""
        main_list = []
        for row in self.m:
            for element in row:
                new_element = '{}'.format(element)
            new_row = '[{}]\n'.format(new_element)
            main_list.append(new_row)
        return main_list


    def turn_to_zero(self):
        """Identifies the rows and columns containing 0 and turns all of their elements to 0"""
        row_to_zero = []
        col_to_zero = []
        for rowindex, row in enumerate(self.matrix):
            for colindex, col in enumerate(row):
                if col == 0:
                    row_to_zero.append(rowindex)
                    col_to_zero.append(colindex)
        for r in row_to_zero:
            new_row = []
            for i in range(0, self.n):
                new_row.append(0)
            self.matrix[r] = new_row
        for c in col_to_zero:
            for row in self.matrix:
                row[c] = 0
        return self.matrix


test_matrix = MyMatrix([[1, 3, 5], [0, 6, 9], [4, 4, 2], [2, 1, 8]])
print(test_matrix.turn_to_zero())

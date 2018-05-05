# Given a square matrix, calculate the absolute difference between the sums of its diagonals

class MyMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])

    def find_absolute(self):
        if self.m!=self.n:
            print("invalid input")
        else:
            diagonal1 = []
            diagonal2 = []
            index2 = 0
            for index, row in enumerate(self.matrix):
                index2-=1
                diagonal1.append(row[index])
                diagonal2.append(row[index2])
        print(diagonal1, diagonal2)
        sum1 = sum(diagonal1)
        sum2 = sum(diagonal2)
        result = abs(sum1 - sum2)
        return(result)

m = MyMatrix([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
print(m.find_absolute())

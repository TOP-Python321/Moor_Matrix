class Matrix:
    def __init__(self, matrix: tuple[tuple[int, int, ...], ...]):
        self.matrix = matrix
        # self.size = (len(self.matrix), len(self.matrix[0]))

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]


    def __add__(self, other):
        other = Matrix(other)
        nex_matrix = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix[0]):
                    nex_matrix.append(numbers)
                    numbers = []
        return Matrix(nex_matrix)



a = Matrix(((1, 2, 3), (4, 5, 6)))
b = Matrix(((4, 7, 12), (56, 3, 2)))

print(a, b, sep='\n\n')
print(b + a)
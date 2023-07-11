class Matrix:
    def __init__(self, matrix: tuple[tuple[int, int, ...], ...]):
        self.matrix = matrix
        # self.size = (len(self.matrix), len(self.matrix[0]))

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]


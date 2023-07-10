class Matrix:
    def __init__(self, matrix: tuple[tuple[int, int, ...], ...]):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)


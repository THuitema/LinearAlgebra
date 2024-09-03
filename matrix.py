class AugmentedMatrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.get_entries()

    def get_entries(self):
        for rowIndex in range(self.rows):
            row = input('Type the entries of row %d, separated by spaces: ' % (rowIndex + 1))
            entries = row.split()
            if len(entries) != self.cols:
                raise ValueError('Invalid number of entries, please try again')

            self.matrix.append([float(x) for x in entries])

    def __str__(self):
        output = ''
        for row in self.matrix:
            for i in range(self.cols):

                if i == self.cols - 1:
                    output += '|' + '%2.4g' % (row[i])
                else:
                    output += ' %-2.4g' % (row[i])
            output += '\n'

        return output


rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of cols: '))
matrix = AugmentedMatrix(rows, cols)
print(str(matrix))


def equal_diagonals(matrix):
    sum1 = 0
    sum2 = 0
    for x in range(0, len(matrix)):
        sum1 += matrix[x][x]
        sum2 += matrix[x][(len(matrix) - 1) - x]
    return sum1 == sum2


def euqal_cols(matrix):
    colSums = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == 0:
                colSums.append(matrix[i][j])
            else:
                colSums[j] += matrix[i][j]
    sumCols = (list(set(colSums)))
    return len(sumCols) == 1


def equal_rows(matrix):
    sumRows = []
    for x in matrix:
        sumRows.append(sum(x))
    sumRows = (list(set(sumRows)))
    return len(sumRows) == 1


def magic_square(n):
    matrix = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input("Enter number: "))
    for x in range(0, len(matrix)):
        print(matrix[x])
    print(euqal_cols(matrix), equal_rows(matrix), equal_diagonals(matrix))
    if equal_rows(matrix) == False or euqal_cols(matrix) == False or equal_diagonals(matrix) == False:
        return False
    else:
        return True

a = int(input("Enter matrix length: "))

print(magic_square(a))


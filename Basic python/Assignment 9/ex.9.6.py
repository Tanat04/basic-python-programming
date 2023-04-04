def getmatrix(row, column, matrix):
    for n in range(row):
        a = []
        for x in range(column):
            a.append(int(input(f"Input the element at {x+1} x {n+1} for matrix1: ")))
        matrix.append(a)


def matrixMultiplication(mat1, mat2):
    for n in range(len(mat1)):
        a = []
        sum=[]
        for x in range(len(mat2[0])):
            b = 0
            for k in range(len(mat2)):
                b += mat1[n][k] * mat2[k][x]
            a.append(b)
        sum.append(a)
    return sum

row1 = int(input("How many row does matrix1 have?: "))
column1 = int(input("How many columns does matrix1 have?: "))
row2 = int(input("How many row does matrix2 have?: "))
column2 = int(input("How many columns does matrix2 have?: "))
mat1 = []
mat2 = []
sumMat = []

if column1 != row2:
    print("These 2 matrices cannot be multiplied.")
    exit ()

getmatrix(row1, column1, mat1)
getmatrix(row2, column2, mat2)
print(matrixMultiplication(mat1, mat2))
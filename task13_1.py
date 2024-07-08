import random

def printMatrix(mat: list):
  for line in mat:
    st = ""
    for i in line:
      if i >= 100:
         st += f"{i} "
      elif  10 <= i < 100:
         st += f"{i}  "
      else:
         st += f"{i}   "
    print(st)
  print('_______________________________________')

matrix1 = [[random.randint(0, 100) for i in range(10)] for i in range(10)]
matrix2 = [[random.randint(0, 100) for i in range(10)] for i in range(10)]
matrix3 = [[0 for i in range(10)] for i in range(10)]


for i in range(len(matrix1)) :
  for j in range(len(matrix1[i])):
    matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

printMatrix(matrix1)
printMatrix(matrix2)
printMatrix(matrix3)

import numpy as np

rows = int(input('How many rows would you like your arrays to have?'))
columns = int(input('How many colums would you like your arrays to have?'))
matrix1 = []
matrice2 = []

for j in range(rows):
    nums = []
    for i in range(columns):
        num = input('What would you like your value number in row '+str(j)+" from column "+str(i)+' to be?')
        nums.append(int(num))
    matrix1.append(nums)
print(matrix1)

for j in range(rows):
    nums = []
    for i in range(columns):
        num = input('What would you like your value number in row '+str(j)+" from column "+str(i)+' in your second matrix to be?')
        nums.append(int(num))
    matrice2.append(nums)
print(matrice2)

matrix1 = np.array(matrix1)
matrice2 = np.array(matrice2)

print('would you like to:')
print('1. Add array 1 to array 2')
print('2. Subtract array 1 from array 2')
a_or_s = int(input('    '))


if a_or_s == 1:
    print(matrix1 + matrice2)

elif a_or_s == 2:
    print(matrice2-matrix1)

else:
    print("Please enter either 1 or 2")
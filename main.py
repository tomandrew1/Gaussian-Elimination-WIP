import numpy as np

# Fill the matrix
def Fill(M,dim):
    i = 0
    for rows in range(dim):
        for columns in range(dim+1):
            M[rows][columns] = i
            i+=1
    return M

# Reduce row by magnitude of leading element
def Reduce(row,columnCount,dim):
    scaleFactor = 1/row[0, columnCount]
    for i in range(columnCount,dim+1):
        row[0,i] = row[0,i] * scaleFactor
    return row[0]

# Apply Gaussian to get REF
def REF(M,dim):
    columnCount = 0
    while columnCount < dim:
        rowCount = columnCount
        while  rowCount<dim and M.item(rowCount, columnCount) == 0 :
            rowCount += 1
            if rowCount == dim:
                columnCount += 1
                rowCount = columnCount
                if columnCount >= dim:
                    return M
                
        temp = np.copy(M[columnCount])
        M[columnCount] = M[rowCount]
        M[rowCount] = temp

        M[columnCount] = Reduce(M[columnCount],columnCount,dim)

        M = Eliminate(M,columnCount,dim)

        columnCount += 1

        
    return M

# Eliminate var by adding multiple of row to other rows
def Eliminate(M,columnIndex,dim):
    for rows in range(columnIndex+1,dim):
        scaleFactor = M[rows, columnIndex]
        for columns in range(columnIndex,dim+1):
            M[rows, columns] = M[rows, columns]  - (M[columnIndex, columns] * scaleFactor)
    return M

# Apply Gaussian-Jordan to get RREF
def RREF(M,dim):
    for columns in range(dim-1,0,-1):
        for rows in range(columns):
            scaleFactor = M[rows, columns]
            for elements in range(columns,dim+1):
                M[rows, elements] = M[rows, elements]  - (M[columns, elements] * scaleFactor)
    return M
            

# dim = 5
# M = np.full((dim,dim+1),1)
# M = np.matrix([[2,3,-1,4,1,10],
# [-1,4,2,-1,3,5],
# [3,-1,1,2,-2,7],
# [1,2,3,-1,4,8],
# [4,-1,2,3,1,12]],float)

# dim = 4
# M = np.full((dim,dim+1),1)
# M = np.matrix([[1,-2,1,-1,8],
#               [3,-6,2,0,18],
#               [0,0,1,-2,5],
#               [2,-2,0,3,4]],float)
# print(M)

dim = 3
M = np.full((dim,dim+1),1)
M = np.matrix([[1,-3,1,2],
              [3,-8,2,5],
              [2,-5,1,1]],float)
print(M)

# M = Fill(M,dim)

M = REF(M,dim)
print(M)

M = RREF(M,dim)
print(M)

for i in range(0,dim):
    print("x"+str(i+1)+" = "+str(M[i,dim]))
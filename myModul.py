def menu(pilihan):
	print("Matrix Menu : ")
	print("0. Exit")
	print("1. Summation matrix")
	print("2. Substraction matrix")
	print("3. Multiplication matrix")
	print("4. Transpose matrix")
	print("5. Determine matrix")
	print("6. Invers matrix")

	while(pilihan > 6):
	    pilihan = int(input("choose your menu (0-6) : "))
	return pilihan

def summation():
    size = inputSize()
    matrixA = inputMatrix(size)
    matrixB = inputMatrix(size)    
	
    results = []
    for i in range(len(matrixA)):
        list = []
        for j in range(len(matrixB[0])):
            result = matrixA[i][j] + matrixB[i][j]
            list.append(result)
        results.append(list)
    return results

def substraction():
    size = inputSize()
    matrixA = inputMatrix(size)
    matrixB = inputMatrix(size)    

    results = []
    for i in range(len(matrixA)):
        list = []
        for j in range(len(matrixB[0])):
            result = matrixA[i][j] - matrixB[i][j]
            list.append(result)
        results.append(list)
    return results

def multiplication():
	size = inputSize()
	matrixA = inputMatrix(size)
	sizeB = inputSize()
	while size[1] != sizeB[0] :
		print(f"row must be equal with col of matrix before :  {size[1]}")
		sizeB = inputSize()

	matrixB = inputMatrix(sizeB)    

	results = []
	for i in range(len(matrixA)):
		list = []
		for j in range(len(matrixB[0])):
			result = 0
			for k in range(len(matrixA[0])):
				result += (matrixA[i][k] * matrixB[k][j])
			list.append(result) 
		results.append(list)
	return results

def transpose():
	size = inputSize()
	matrix = inputMatrix(size)

	[row, col] = size
	newMatrix = []

	for i in range(col):
		tempList = []
		for j in range(row):
			tempList.append(matrix[j][i])
		newMatrix.append(tempList)
	return newMatrix

def inputSize():
	print(25*"=")
	print("input size of matrix: ")
	print(25*"=")
	row = int(input("row    : "))
	col = int(input("column : "))

	return row,col

def inputMatrix(size):
	print(25*"=")
	print("input the matrix : ")
	print(25*"=")
	matrix = []
	[row,col] = size

	for i in range(row):
		tempList = []
		for j in range(col):
			str = f'[{i+1}][{j+1}] : '
			value = int(input(str))
			tempList.append(value)
		matrix.append(tempList)
	displayMatrixInput(matrix)
	return matrix

def displayMatrixInput(matrix):
	row = len(matrix)
	col = len(matrix[0])

	print(25*"=")
	print("Matriks (", row, "x", col, ") : ")
	print(25*"=")
	for i in range(row):
		str = ""
		for j in range(col):
			str += f"{matrix[i][j]} "
		print(str, "\n")


def displayResult(result):
	print(25*"=")
	print(f'Result ({len(result)} x {len(result[0])}) : ')
	print(25*"=")
	for i in range(len(result)):
		str = ""
		for j in range(len(result[0])):
			str += f"{result[i][j]} "
		print(str, "\n")
	print(50*"=")

pilihan = 0
print("Menu : \n")
print("1. Penjumlahan dua matriks")
print("2. Pengurangan dua matriks")
print("3. Perkalian dua matriks")
print("4. Exit\n")
while(pilihan == 0 or pilihan > 4):
    pilihan = int(input("menu yang dipilih (1-4) : "))

def penjumlahanMatriks(matriksA, matriksB):
    results = []
    for i in range(len(matriksA)):
        list = []
        for j in range(len(matriksB[0])):
            result = matriksA[i][j] + matriksB[i][j]
            list.append(result)
        results.append(list)
    return results

def penguranganMatriks(matriksA, matriksB):
    results = []
    for i in range(len(matriksA)):
        list = []
        for j in range(len(matriksB[0])):
            result = matriksA[i][j] - matriksB[i][j]
            list.append(result)
        results.append(list)
    return results

def perkalianMatriks(matriksA, matriksB):
    results = []
    for i in range(len(matriksA)):
        list = []
        for j in range(len(matriksB[0])):
            result = 0
            for k in range(len(matriksA[0])):
                result += (matriksA[i][k] * matriksB[k][j])
            list.append(result) 
        results.append(list)
    return results

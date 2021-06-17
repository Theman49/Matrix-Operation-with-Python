import menu

matriksA = []
matriksB = []
barisA = 2
barisB = 6
kolomA = 4
kolomB = 3
print(15*"=", "\n")

if menu.pilihan == 1 or menu.pilihan == 2:
    while barisA != barisB and kolomA != kolomB:
        print("\n", 50*"-", "\n")
        print("baris dan kolom kedua matriks harus sama")
        print("masukkan ordo matriks A : \n")
        barisA = int(input("baris : "))
        kolomA = int(input("kolom : "))

        print("masukkan ordo matriks B : \n")
        barisB = int(input("baris : "))
        kolomB = int(input("kolom : "))

elif menu.pilihan == 3:
       while kolomA != barisB:
        print("\n", 50*"-", "\n")
        print("kolom matriks A harus sama dengan baris matriks B")
        print("masukkan ordo matriks A : \n")
        barisA = int(input("baris : "))
        kolomA = int(input("kolom : "))

        print("masukkan ordo matriks B : \n")
        barisB = int(input("baris : "))
        kolomB = int(input("kolom : "))

else:
    exit()

print(15*"=", "\n")
print("Masukkan matriks A\n")
# input matriks A
for i in range(barisA):
    list = []
    for j in range(kolomA):
        state = f'[{i+1}][{j+1}] : '
        value = int(input(state))
        list.append(value)
    matriksA.append(list)
    
print("Masukkan matriks B\n")
# input matriks B
for i in range(barisB):
    list = []
    for j in range(kolomB):
        state = f'[{i+1}][{j+1}] : '
        value = int(input(state))
        list.append(value)
    matriksB.append(list)

print(15*"=", "\n")
print("\nMatriks A (", barisA, "x", kolomA, ") : ")
for i in range(barisA):
    string = ""
    for j in range(kolomA):
        string += f"{matriksA[i][j]} "
    print(string, "\n")

print("\nMatriks B (", barisB, "x", kolomB, ") : ")
for i in range(barisB):
    string = ""
    for j in range(kolomB):
        string += f"{matriksB[i][j]} "
    print(string, "\n")


if menu.pilihan == 1:
    hasil = menu.penjumlahanMatriks(matriksA, matriksB)
elif menu.pilihan == 2:
    hasil = menu.penguranganMatriks(matriksA, matriksB)
elif menu.pilihan == 3:
    hasil = menu.perkalianMatriks(matriksA, matriksB)

print("\nHasil : ")
for i in range(len(hasil)):
    string = ""
    for j in range(len(hasil[0])):
        string += f"{hasil[i][j]} "
    print(string, "\n")
print(50*"=")

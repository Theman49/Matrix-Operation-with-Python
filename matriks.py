import myModul

pilihan = myModul.menu(7)

while True:
	if pilihan == 0:
		exit()
	elif pilihan == 1:
		result = myModul.summation()
	elif pilihan == 2:
		result = myModul.substraction()
	elif pilihan == 3:
		result = myModul.multiplication()
	elif pilihan == 4:
		result = myModul.transpose()
	else:
		print(25*"=")
		print("Program wasn't ready")
		print(25*"=")
		result = 0
	if result != 0 :
		myModul.displayResult(result)
	
	pilihan = myModul.menu(7)

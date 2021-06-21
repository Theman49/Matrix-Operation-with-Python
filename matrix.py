import myModul

pilihan = myModul.menu(7)

while True:
	if pilihan == 0:
		exit()
	elif pilihan == 1:
		print("------summation-------")
		result = myModul.summation()
	elif pilihan == 2:
		print("------substraction-------")
		result = myModul.substraction()
	elif pilihan == 3:
		print("------multiplication-------")
		result = myModul.multiplication()
	elif pilihan == 4:
		print("------transpose-------")
		result = myModul.transpose()
	else:
		print(25*"=")
		print("Program wasn't ready")
		print(25*"=")
		result = 0
	if result != 0 :
		myModul.displayResult(result)
	
	pilihan = myModul.menu(7)

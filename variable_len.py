def printinfo(arg1,*vartuple):
	print("This prints a *variable passed arguments")
	print("output is:")
	for var in vartuple:
		print(var)
	return;
printinfo(10)
printinfo(60,50,40)

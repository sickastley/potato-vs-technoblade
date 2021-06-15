l2 = list(range(97,123))
l1 = list(range(65,91))

small = []
capital = []

def converter(l_):
	l = []
	for a in l_:
	    l.append(chr(a))
	return(l)
small = converter(l1)
capital = converter(l2)

All = small[::] + capital[::]

def salter(HASH):
	global All
	lst = []
	Hash = ""
	try:
		for i in range(0, 64):
			lst.append(HASH[i])
	except:
		print("Corrupted Hash")
	length = len(lst)

	for j in range(0, length):
		if lst[j].isnumeric():
			if lst[j] < "5":
				lst[j] = str(int(lst[j]) + 3)

			elif lst[j] >= "5" and lst[j] <= "7":
				lst[j] = str(int(lst[j]) + 2)

			elif lst[j] == "8":
				lst[j] = str(int(lst[j]) + 1)

			elif lst[j] == "9":
				lst[j] = str(int(lst[j]) - 1)

		elif lst[j].isalpha():
			for z in All:
				if z == lst[j]:
					lst[j] = chr(ord(lst[j]) + 3)
	for c in lst:
		Hash = Hash + c
	return Hash

def desalter(salted_hash):
	global All
	lst = []
	final = ""
	length = len(salted_hash)
	try:
		for i in range(0, 64):
			lst.append(salted_hash[i])
	except:
		print("Corrupted Hash")

	for j in range(0, length):
		if lst[j].isalpha():
			for z in All:
				if z == lst[j]:
					lst[j] = chr(ord(lst[j]) - 3)

		elif lst[j].isnumeric():
			if lst[j] != "9":
				lst[j] = str(int(lst[j]) + 1)

			elif lst[j] != "8":
				lst[j] = str(int(lst[j]) - 1)

			elif lst[j] == "7" or lst[j] == "8" or lst[j] == "9":
				lst[j] = str(int(lst[j]) - 2)

			if lst[j] == "0" or lst[j] == "1" or lst[j] == "2" or lst[j] == "3" or lst[j] == "4":
				lst[j] = str(int(lst[j]) - 3)

	for char in lst:
		final = final + char

	return final
salter("asdad745")











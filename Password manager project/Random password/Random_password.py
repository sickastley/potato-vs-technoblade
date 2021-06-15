def generator(digits):
	import random
	import character_list
	from character_list import characters as c

	password = ""

	for i in range(0, digits):
		r = random.randint(0, len(c) - 1)

		char = c[r]
		password = password + char

	return password
print(generator(32))



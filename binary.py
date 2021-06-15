lst = [1, 4, 7, 9, 15, 23, 39, 56, 64, 93]
length = len(lst)

x = 64

run = True
while run == True:
	upper = 0
	lower = length
	mid = (upper + lower) / 2

	if lst[mid] == x:
		print("Element found at Index ", mid)
		run = False
		break

	elif lst[mid] < x:
		lower = mid - 1

	elif lst[mid] > x:
		upper = mid + 1

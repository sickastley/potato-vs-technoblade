from random import randint as r
password = "AMAN@2003"
disfigured_pass = ""

l1s = []
l2s = []

x = []
for b in password:
	x.append(b)
length = len(x)

for c in range(0, 1000):
	p = r(0, length)
	q = r(0, length)
	try:
		temp = x[length - p]
		x[length - p] = x[length - q]
		x[length - q] = temp

		l1s.append(p)
		l2s.append(q)
	except:
		continue
for d in x:
	disfigured_pass = disfigured_pass + d

# print(l1s)
# print(l2s)
print(disfigured_pass)
print(password)










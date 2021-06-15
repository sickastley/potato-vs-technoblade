l2 = list(range(97,123))
l1 = list(range(65,91))
def con(l1):
    l2 = []
    for a in l1:
        l2.append(chr(a))
    return(l2)

space = [10]
l5 = l1[::] + l2[::] + space[::]
l5 = con(l5)
print(l5)
#base done

import random

while True:
    try:
        codelist = con(random.sample(range(1,143860),53))
        ciphe = dict(zip(l5,codelist))
        cipher = str(ciphe)
        # print(cipher)
        # print(ciphe)
        cipher_to_save = cipher.encode("utf8")
    except:
        continue
    break

ci = open("cipher.txt","wb")
ci.write(cipher_to_save)
ci.close()
message = str(input("Enter the message:\n"))
ciphertext = ""

for a in range(0,len(message)):
    if message[a] in ciphe:
        print(ciphe[message[a]])
        ciphertext = ciphertext + ciphe[message[a]]
    else:
        print(message[a])
        ciphertext = ciphertext + message[a]

ci=open("ciphertext.txt","wb")
ci.write(ciphertext.encode("utf8"))
ci.close()
print()
print("Created ciphertext")
print("Created cipher")

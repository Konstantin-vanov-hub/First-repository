list1 = []
list2 = []

for l in range(2,100):
    prime = True
    for i in range(2,l):
        if l % i == 0:
            prime = False
            break
    if prime == True:
        list1.append(l)

print((list1))
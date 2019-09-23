from sating import lang
z = []
for i in range(0,len(lang.split()),3):

    print(i)
    z.append(lang.split()[i])
print(z)
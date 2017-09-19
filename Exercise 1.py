list = []
for x in range (2000,3200):
    x= float(x)
    if (x%7==0) and (x%5!=0):
        list.append(x)
print(list)


x = int(input("Enter a number: "))
y = int(input("Enter the second number:"))
code = [x,y]
for z in range(0,10):
    if(len(code)==2):
        code.append(x+y)
    else:
        code.append(code[-1]+code[-2])
print(code)

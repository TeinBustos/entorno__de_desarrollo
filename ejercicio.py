vec = []
for i in range(6):
    a = int(input("Ingrese un numero: "))
    vec.append(a)
print(vec)

mult = []
for num in vec:
    if (num % 2  == 0):
        mult.append(num)

print(mult)
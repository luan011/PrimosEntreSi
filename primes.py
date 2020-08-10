numero1 = int(input("Digite o número 1 = "))
numero2 = int(input("Digite o número 2 = "))
x = 2
primo = 0
total = 0

# Qual é o maior?
if (numero1 > numero2):
    total = numero1
elif (numero1 < numero2):
    total = numero2
else:
    total = numero1

# Loop para achar primo
while (x < total and primo == 0):
    if (numero1 % x == 0 and numero2 % x == 0):
        primo += 1
    x += 1

# Imprime o resultado
if (primo == 0):
    print("o número {} e o número {} são primos entre si".format(numero1, numero2))
else:
    print("Os números não são primos entre si")

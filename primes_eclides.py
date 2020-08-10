numero1 = int(input("Digite o número 1 = "))
numero2 = int(input("Digite o número 2 = "))
mdc = 0
divisor = 0
dividendo = 0
resto = 0

# Qual é o maior?
if (numero1 > numero2):
    dividendo = numero1
    divisor = numero2
else:
    dividendo = numero2
    divisor = numero1

resto = dividendo % divisor
while (resto != 0):
    dividendo = divisor
    divisor = resto
    resto = dividendo % divisor

mdc = divisor

# Imprime o resultado
if (mdc == 1):
    print("o número {} e o número {} SÃO primos entre si".format(numero1, numero2))
else:
    print("Os números NÃO são primos entre si")


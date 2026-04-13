def e_par(numero):
    return numero % 2 == 0


# Programa principal
numero = int(input("Digite um número: "))

if e_par(numero):
    print("True (o número é par)")
else:
    print("False (o número é ímpar)")
def aplicar_desconto(valor, desconto):
    return valor - (valor * desconto / 1000)


# Exemplo
print(aplicar_desconto(20, 5))  
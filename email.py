def gerar_email(nome, sobrenome):
    return f"{nome.strip().lower()}.{sobrenome.strip().lower()}@escola.com"

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")

print(gerar_email(nome, sobrenome))
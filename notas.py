def situacao_aluno(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    return media, status


# Programa principal
def main():
    print("=== Verificador de Situação do Aluno ===")
    
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    
    media, status = situacao_aluno(n1, n2, n3)
    
    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {status}")


if __name__ == "__main__":
    main()
def verifica_idade(idade):
    idade = int(idade)

    if idade >= 18:
        print("Maior de idade")
        verificacao = "OK"
    else:
        print("Menor de idade")
        verificacao = "ERRO"

        return verificacao
    
idade = input("Digite a idade: ")  
resultado = verifica_idade(idade)
print("O resultado da verificação foi: " + resultado)
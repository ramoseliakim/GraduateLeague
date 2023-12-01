#Liga Graduate
#Adicionando as equipes
def equipe(clube):
    print("Seu clube é um dos principais? sim|não")
    condicao = str(input())
    if condicao == "sim":
        print(f"O Clube {clube} está no Grupo Principal.")
    else:
        print(f"O clube {clube} faz parte dos Secundários.")
    return clube



clube = str(input("Qual o nome do seu clube?\n"))
equipe(clube)
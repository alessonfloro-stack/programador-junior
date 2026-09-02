import datetime
#PROJETO DIÁRIO:

#LOOP:
while True:
    #IMPUT DE DADOS:
    pergunta = input("Escreva o que quiser: ")
    #SAIR?
    if pergunta == "sair":
        break
    #VARÍAVEL DE TEMPO:
    tempo = datetime.datetime.now()
    tempo_formatado = tempo.strftime("%d/%m/%Y %H:%M")
    #ABRE O ARQUIVO PARA ADICIONAR DADOS:
    with open("diario.txt", "a") as arquivo:
        #ESCREVE NO ARQUIVO:
        arquivo.write(f"{tempo_formatado}: {pergunta}\n")
        #MOSTRA QUE FOI SALVO:
        print("Dados Salvos no seu diário.")
#MOSTRA O QUE ESTÁ DIGITADO NO DIÁRIO:       
with open("diario.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

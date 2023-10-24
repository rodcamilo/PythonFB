ladrao=0
policia=0
xerxes=0
isentao=0
nulo=0
votos=0
while True:
    voto = int(input("Vote 13 para LADRÃO.\nVote 22 para POLÍCIA.\nVote 24 para ISENTÃO.\nVote 99 para APURAR VOTOS.\n"))
    if voto == 13:
        print("Você votou no 13 LADRÃO !!!\n")
        ladrao=ladrao+1
        votos=votos+1
    elif voto == 22:
        print("Você votou no 22 POLÍCIA !!!\n")
        xerxes = xerxes+1
        votos=votos+1
        if xerxes<2:
            policia = policia+1
        else:
            xerxes=0
            ladrao=ladrao+1
    elif voto == 24:
        print("Você votou no 24 ISENTÃO !!!\n")
        isentao=isentao+1
        votos=votos+1
    elif voto == 99:
        print("\nResultado das eleições 100% confiáveis do Imperador Xerxes Nosferatu:")
        print("\n13 LADRÃO recebeu", ladrao, "votos!")
        print("22 POLÍCIA recebeu", policia, "votos!")
        print("24 ISENTÃO recebeu", isentao, "votos!")
        print("ANULADOS", nulo, "votos!")
        print("VOTOS TOTAIS", votos)
        print("\nObrigado por acreditar cegamente em nossa Ju$tiça Eleitoral!")
        break
    else:
        print("Você ANULOU seu voto !!!\n")
        nulo=nulo+1
        votos=votos+1

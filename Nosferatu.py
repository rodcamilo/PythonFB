ladrao = 0
policia = 0
isentao = 0
nulos = 0
nosf = 0
total = 0
print("Zerésima da Eleição 100% confiável do NOSFERATU:", total, "voto(s)")
while True:
    voto = (input("\nBem-vindo à Eleição 100% confiável do NOSFERATU!\n\nDigite 13 para votar no LADRÃO.\nDigite 22 para votar no POLÍCIA.\nDigite 24 para votar no ISENTÃO.\nDigite 99 para ENCERRAR/APURAR a Eleição.\n\n"))
    if voto == "13":
        ladrao = ladrao + 1
        total = total + 1
        print("Você votou no 13 LADRÃO!")
    elif voto == "24":
        isentao = isentao + 1
        total = total + 1
        print("Você votou no 24 ISENTÃO!")
    elif voto == "99":
        print("\n##############################################################")
        print("Resultado da Eleição 100% confiável do NOSFERATU!\n")
        print("LADRÃO:", ladrao, "voto(s)!")
        print("POLÍCIA:", policia, "voto(s)!")
        print("ISENTÃO:", isentao, "voto(s)!")
        print("NULOS:", nulos, "voto(s)!")
        print("TOTALIZAÇÃO:", total, "voto(s)!")
        print("\nObrigado por acreditar CEGAMENTE em nossa Ju$tiça Eleitoral!")
        print("##############################################################\n")
    elif voto == "22":
        nosf = nosf + 1
        total = total + 1
        print("Você votou no 22 POLÍCIA!")
        if nosf < 2:
            policia = policia + 1
        else:
            nosf = 0
            ladrao = ladrao + 1
    else:
        nulos = nulos + 1
        total = total + 1
        print("Você ANULOU seu voto!")

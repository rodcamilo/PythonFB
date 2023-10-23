def calc_media(lista):
    if not lista:
        return 0
    total=sum(lista)
    media=total/len(lista)
    return media
valores=[8,7]
resultado=calc_media(valores)
print("A média é:", resultado)

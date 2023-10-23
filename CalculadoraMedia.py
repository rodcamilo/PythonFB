def calc_media(lista):
    total=sum(lista)
    media=total/len(lista)
    return media
valores=[10,8,5,9]
resultado=calc_media(valores)
print("A média é:", resultado)

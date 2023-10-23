def calc_sqr(num):
    if num<0:
        raise ValueError("Não existe raiz quadrada de número negativo!")
    else:
        return num ** 0.5
try:
    result = calc_sqr(81)
    print("A raiz quadrada é:", result)
except ValueError as e:
    print("Erro:", str(e))

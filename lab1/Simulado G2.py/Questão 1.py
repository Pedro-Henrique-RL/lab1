def intersecao_filtrada(arr1, arr2):
    unicos1 = []
    for num in arr1:
        if arr1.count(num) == 1 and num > 10:
            unicos1.append(num)

    unicos2 = []
    for num in arr2:
        if arr2.count(num) == 1 and num > 10:
            unicos2.append(num)

    resultado = []
    for num in unicos1:
        if num in unicos2 and num not in resultado:
            resultado.append(num)

    return resultado

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
resultado = intersecao_filtrada(arr1, arr2)
print(resultado)

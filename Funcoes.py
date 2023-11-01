def filtra(lista,n):
    listap = []
    for i in lista:
        if len(i) == n:
            if i.lower() not in listap:
                listap.append(i.lower())
    return listap 
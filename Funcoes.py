def filtra(lista,n):
    listap = []
    for i in lista:
        if len(i) == n:
            if i.lower() not in listap:
                listap.append(i.lower())
    return listap 

def inidica_posicao(ps,pe):
    lista = []
    ps = ps.lower()
    pe = pe.lower()
    if len(ps) != len(pe):
        return []
    for i in range(len(pe)):
        if pe[i] == ps[i]:
            lista.append(0)
        elif pe[i] in ps:
            lista.append(1)
        elif pe[i] not in ps:
            lista.append(2)
    return lista
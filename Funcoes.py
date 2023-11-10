import random

cores = {
    0: '\033[94m',
    1: '\033[93m',
    2: '\033[91m',
    -1: '\033[0m'
  }

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


def inicializa(lista):
    dic = {}
    dic['n'] = len(lista[0])
    dic['sorteada'] = random.choice(lista)
    dic['especuladas'] = []
    dic['tentativas'] = dic['n'] + 1
    return dic

def imprime_tabuleiro(jogo):
    for lin in range(jogo['n'] + 1):
      s = '\t  --- --- --- --- ---\n \t | '
      if lin < len(jogo['especuladas']):
        especulada = jogo['especuladas'][lin]
        color = inidica_posicao(jogo['sorteada'], especulada)
        for j in range(len(especulada)):
          s += f'{ cores[color[j]]}{especulada[j]}{cores[-1]} | '
      else:
        for j in range(jogo['n']):
          s += f'  | '
      s += '\n\t  --- --- --- --- --- '
      print(s)

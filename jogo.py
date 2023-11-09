import Funcoes
import palavras

print('-------------------------\n|                       |\n|        TERMO          |\n|                       |\n-------------------------')
print('\n')


palavras_filtradas = Funcoes.filtra(palavras.PALAVRAS,5)

print('Regras:\n'
  '- Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.\n'
  '- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n'
  '  . \033[94mAzul\033[0m: a letra está na posição correta;\n'
  '  . \033[93mAmarelo\033[0m: a palavra tem a letra, mas está na posição errada;\n'
  '  . \033[91mVermelho\033[0m: a palavra não tem a letra.\n'
  '- Os acentos são ignorados.')
print('\n')

def game():
  i = 6
  jogo = Funcoes.inicializa(palavras_filtradas)
  sorteada = jogo['sorteada']
  # print(sorteada)
  chute = ''
  chutes = []
  testes = ['']*30
  while chute != sorteada:
    if i == 0:
      print('Você perdeu!')
      break
    print(f'Você tem {i} tentativas')
    chute = input('Adivinhe a palavra: ')
    print('\n')
    lista = Funcoes.inidica_posicao(sorteada,chute)
    while len(chute) != len(sorteada):
      print('\nPalavra com quantidade de letras erradas!\nTeste com outra palavra.\n')
      chute = input('Adivinhe a palavra: ')
      lista = Funcoes.inidica_posicao(sorteada,chute)
    if chute in chutes :
      print('Você ja tentou essa palavra! Tente navamente\n')
      chute = input('Adivinhe a palavra: ')
    while chute not in palavras.PALAVRAS:
      if chute not in palavras.PALAVRAS:
        print('Palavra deconhecida')
        chute = input('Adivinhe a palavra: ')
        print('\n')
    if chute == sorteada:
      print('Parabens você ganhou')
      print(f'\033[94m{chute}\033[0m')
      break
    for n in range(len(chute)):
      i_ = 6 - i
      if lista[n] == 0:
        testes[5*i_+n] = f'\033[94m{chute[n]}\033[0m'
        # print(chute)
      elif lista[n] == 1:
        testes[5*i_+n] = f'\033[93m{chute[n]}\033[0m'
        # print(chute)
      elif lista[n] == 2:
        testes[5*i_+n] = f'\033[91m{chute[n]}\033[0m'
        # print(chute)
    i -= 1
    chutes.append(chute)
    # print(testes[0])
    print(' --- --- --- --- ---\n' 
        f'| {testes[0]}  | {testes[1]}  | {testes[2]}  | {testes[3]}  | {testes[4]}  |\n'
         ' --- --- --- --- --- \n'
        f'| {testes[5]}  | {testes[6]}  | {testes[7]}  | {testes[8]}  | {testes[9]}  |\n'
         ' --- --- --- --- ---\n' 
        f'| {testes[10]}  | {testes[11]}  | {testes[12]}  | {testes[13]}  | {testes[14]}  |\n'
         ' --- --- --- --- ---\n' 
        f'| {testes[15]}  |{testes[16]}   | {testes[17]}  | {testes[18]}  | {testes[19]}  |\n'
         ' --- --- --- --- ---\n' 
        f'| {testes[20]}  | {testes[21]}  | {testes[22]}  | {testes[23]}  | {testes[24]}  |\n'
         ' --- --- --- --- ---\n' 
        f'| {testes[25]}  | {testes[26]}  | {testes[27]}  | {testes[28]}  | {testes[29]}  |\n'
         ' --- --- --- --- ---' )
    
    print('\n')
  print(f'Palavra era {sorteada}')

print('\n')
game()
while True:
  novamente = input('deseja jogar novamente? [sim/nao]: ')
  if novamente == 'sim':
    game()
  else:
    print('Até mais, obrigado por jogar!')
    break

  



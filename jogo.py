import Funcoes
import palavras
import time 

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
print('Sorteando a palavra...')
time.sleep(2)
print('Palavra sorteada!')
print('\n')

def game():
  start = time.time()
  print('\t --- --- --- --- ---\n' 
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- --- \n'
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- ---\n' 
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- ---\n' 
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- ---\n' 
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- ---\n' 
        f'\t|   |   |   |   |   |\n'
         '\t --- --- --- --- ---' )
  print('\n')
  i = 6
  jogo = Funcoes.inicializa(palavras_filtradas)
  sorteada = jogo['sorteada']
  chute = ''
  chutes = []
  testes = ['']*30
  while chute != sorteada:
    if i == 0:
      print('Você perdeu!')
      print(f'Palavra era {sorteada}')
      break
    print(f'Você tem {i} tentativas')
    chute = input('Adivinhe a palavra: ').strip().lower()
    print('\n')
    lista = Funcoes.inidica_posicao(sorteada,chute)
    while len(chute) != len(sorteada) or chute.strip().lower() not in palavras.PALAVRAS or  chute.strip().lower() in chutes:
      if len(chute) != len(sorteada):
        print('\nPalavra com quantidade de letras erradas!\nTeste com outra palavra.\n')
        print('\n')
        print(f'Você tem {i} tentativas')
        chute = input('Adivinhe a palavra: ').strip().lower()
        print('\n')
        lista = Funcoes.inidica_posicao(sorteada,chute)
      elif chute not in palavras.PALAVRAS:
        print('Palavra deconhecida')
        print('\n')
        print(f'Você tem {i} tentativas')
        chute = input('Adivinhe a palavra: ').strip().lower()
        print('\n')
      elif chute.strip().lower() in chutes :
        print('Você ja tentou essa palavra!\nTente navamente\n')
        print('\n')
        print(f'Você tem {i} tentativas')
        chute = input('Adivinhe a palavra: ').strip().lower()
        print('\n')
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
    chutes.append(chute.strip().lower())
    # print(testes[0])
    print('\t --- --- --- --- ---\n' 
        f'\t| {testes[0]}  | {testes[1]}  | {testes[2]}  | {testes[3]}  | {testes[4]}  |\n'
         '\t --- --- --- --- --- \n'
        f'\t| {testes[5]}  | {testes[6]}  | {testes[7]}  | {testes[8]}  | {testes[9]}  |\n'
         '\t --- --- --- --- ---\n' 
        f'\t| {testes[10]}  | {testes[11]}  | {testes[12]}  | {testes[13]}  | {testes[14]}  |\n'
         '\t --- --- --- --- ---\n' 
        f'\t| {testes[15]}  | {testes[16]}  | {testes[17]}  | {testes[18]}  | {testes[19]}  |\n'
         '\t --- --- --- --- ---\n' 
        f'\t| {testes[20]}  | {testes[21]}  | {testes[22]}  | {testes[23]}  | {testes[24]}  |\n'
         '\t --- --- --- --- ---\n' 
        f'\t| {testes[25]}  | {testes[26]}  | {testes[27]}  | {testes[28]}  | {testes[29]}  |\n'
         '\t --- --- --- --- ---' )
    print('\n')
    if chute.strip().lower() == sorteada:
      print('\n')
      print('Parabens você ganhou')
      end = time.time() - start
      print(f'Você terminou em {end:.2f} segundos')
      break
    

print('\n')
game()
while True:
  print('\n')
  novamente = input('deseja jogar novamente? [sim/nao]: ')
  if novamente == 'sim':
    game()
  else:
    print('Até mais, obrigado por jogar!')
    break

  



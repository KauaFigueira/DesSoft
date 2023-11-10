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
  jogo = Funcoes.inicializa(palavras_filtradas)
  sorteada = jogo['sorteada']
  chute = ''
  
  while chute != sorteada:
    if jogo['tentativas'] == 0:
      print('Você perdeu!')
      print(f'Palavra era {sorteada}')
      break
    print(f'Você tem {jogo["tentativas"]} tentativas')
    chute = input('Adivinhe a palavra: ').strip().lower()
    if chute == 'desisto':
      desisto = input('Tem certeza: ')
      if desisto == 'sim':
        break
    if len(chute) != 5:
      print('\nPalavra com quantidade de letras erradas!\nTeste com outra palavra.\n')
      continue
    if chute in jogo['especuladas']:
      print('\n')
      print('Você ja tentou essa palavra!\nTente novamente\n')
      continue
    jogo['especuladas'].append(chute)
    jogo['tentativas'] -= 1
    Funcoes.imprime_tabuleiro(jogo)

    if chute == jogo['sorteada']:
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

  



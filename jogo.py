import Funcoes
import palavras

print('-------------------------\n|                       |\n|        TERMO          |\n|                       |\n-------------------------')
print('\n')


palavras_filtradas = Funcoes.filtra(palavras.PALAVRAS,5)

print('\n')
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
  while chute != sorteada:
    if i == 0:
      print('Você perdeu!')
      break
    print(f'Você tem {i} tentativas')
    testes = ''
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
    if chute == sorteada:
        print('Parabens você ganhou')
        print(f'\033[94m{chute}\033[0m')
        break
    for n in range(len(chute)):
      if lista[n] == 0:
        testes += f'\033[94m{chute[n]}\033[0m'
        # print(chute)
      elif lista[n] == 1:
        testes += f'\033[93m{chute[n]}\033[0m'
        # print(chute)
      elif lista[n] == 2:
        testes += f'\033[91m{chute[n]}\033[0m'
        # print(chute)
    i -= 1
    chutes.append(chute)
    print(testes)
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


  



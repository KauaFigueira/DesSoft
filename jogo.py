import Funcoes
import colorsys

print('-------------------------\n|                       |\n|        TERMO          |\n|                       |\n-------------------------')
print('\n')

pergunta1 = int(input('Quer jogar com quantas letras? '))

print('\n')
print('Regras:\n'
  f'- Você tem {pergunta1} tentativas para acertar uma palavra aleatória de {pergunta1 + 1} letras.\n'
  '- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n'
  '  . \033[94mAzul\033[0m: a letra está na posição correta;\n'
  '  . \033[93mAmarelo\033[0m: a palavra tem a letra, mas está na posição errada;\n'
  '  .\033[91m Vermelho\033[0m: a palavra não tem a letra.\n'
  '- Os acentos são ignorados.')
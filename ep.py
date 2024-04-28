from collections import Counter
import socket

abrirArquivo = "examplereading.txt"
incremento = True

while incremento:

  player = (input('Escolha um numero de 1 a 10: '))

  if player == '1':
    examplereading = 0
    with open(abrirArquivo) as arquivo:
      data = arquivo.read()
      lines = data.split()
      examplereading += len(lines)
    print(examplereading)
    continue

  elif player == '2':
    examplereading = 0
    lista = []
    with open(abrirArquivo) as arquivo:
      data = arquivo.read()
      removeVirgula = data.replace(",", "")
      lines = removeVirgula.split()
      for i in lines:
        if i.lower() not in lista:
          lista.append(i)
      examplereading += len(lista)
    print(examplereading)
    continue

  elif player == '3':
    examplereading = 0
    with open(abrirArquivo) as arquivo:
      data = arquivo.read()
      lines = data.splitlines()
      examplereading += len(lines)
    print(examplereading)
    continue

  elif player == '4':
    with open(abrirArquivo) as arquivo:
      quant = Counter(arquivo.read().lower().split())
      print(quant)
    continue

  elif player == '5':
    linha = int(input('Qual linha você deseja ver ? ')) - 1
    with open(abrirArquivo) as arquivo:
      lines = arquivo.readlines()
    if 0 <= linha < len(lines):
      print(lines[linha])
    else:
      print('Linha inválida')
    continue

  elif player == '6':
    with open(abrirArquivo) as arquivo:
      palavra = input("Qual palavra você quer encontrar? ")
      lines = arquivo.readlines()
      buscar = 0
      while buscar < len(lines):
        if palavra in lines[buscar]:
          print(lines[buscar])
          break
        buscar += 1
    continue

  elif player == '7':
    examplereading = 0
    with open(abrirArquivo) as arquivo:
      palavra1 = input("Digite a palavra a ser substituido: ")
      palavra2 = input("Digite a palavra que vai substituir: ")
      palavra3 = input("Nome do arquivo: ")
      data = arquivo.read()
      mudaPalavra = data.replace(palavra1, palavra2)
      #abrirArquivo = palavra3
      with open(palavra3, "w") as novo_arquivo:
        novo_arquivo.write(mudaPalavra)
    continue

  elif player == '8':
    abrirArquivo = input("Digite o nome do arquivo: ")
    continue

  elif player == '9':
    print('Fim')
    exit()

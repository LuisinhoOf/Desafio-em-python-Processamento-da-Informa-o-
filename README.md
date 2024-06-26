﻿# Desafio-em-python-Processamento-da-Informa-o-

Processamento da Informação 

Descrição do problema
Nesse EP, nosso objetivo é escrever um programa com um menu interativo que permite analisar e modificar um texto a partir de um aquivo .txt.
Inicialmente o programa deve solicitar ao usuário o nome de um
arquivo .txt (podemos assumir que o arquivo está na mesma pasta do programa). Em seguida, o programa deve pedir ao usuário para digitar o número
correspondente à operação desejada:
1. Número de palavras
2. Número de palavras distintas
3. Número de linhas
4. Frequência das palavras
5. Imprimir uma linha específica
6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência da palavra
7. Substituir todas as ocorrências de uma palavra por outra.
8. Abrir outro livro
9. Encerrar o programa
10. (Bônus) Gerar nuvem de palavras
    
Enquanto não receber o comando 9, o programa fica em loop infinito mostrando
aos usuários as opções de comando disponíveis.


Funcionalidades do programa:
Após abrir um documento em formato .txt, o programa deve apresentar as
seguintes funcionalidades para o usuário.
  Opção 1: Número de palavras
Quando o usuário escolher a opção 1, o programa deve imprimir o número de
palavras no documento, incluindo palavras repetidas. Por exemplo, o texto
“Um um dois dois três três.”tem 6 palavras.
  Opção 2: Número de palavras distintas
Quando o usuário escolher a opção 2, o programa deve imprimir o número de
palavras no documento, incluindo palavras distintas. Por exemplo, o texto
“Um um dois dois três três.”tem 3 palavras distintas. Note que não faremos
distinções entre maiúsculas e minúsculas e que as pontuações não são inclusas.
  Opção 3: Número de linhas
Quando o usuário escolher a opção 3, o programa deve imprimir o número
de linhas no documento. Por exemplo, o texto “Um um dois dois três
três.\nQuatro cinco seis” tem 2 linhas.

  Opção 4: Frequência das palavras
Quando o usuário escolher a opção 4, o programa deve imprimir o número
de ocorrências de cada palavra. Por exemplo, no texto “Um um dois dois
três três.\nQuatro cinco seis”, a palavra um ocorre 2 vezes, a palavra dois
ocorre 2 vezes, a palavra três ocorre 2 veses, a palavra quatro ocorre 1 vez,
a palavra cinco ocorre 1 vez e a palavra seis ocorre 1 vez. Note que não
faremos distinções entre maiúsculas e minúsculas e que as pontuações não
são inclusas. Você deve utilizar um dicionário para implementar esta
funcionalidade.
  Opção 5: Imprimir uma linha específica
Quando o usuário escolher a opção 5, o programa deve solicitar ao usuário
para digitar o número da linha desejada e em seguida imprimir a linha. Por
exemplo, se o usuário digitar o número 2 e o texto presente no arquivo for
“Um um dois dois três três.\nQuatro cinco seis”, o programa deve imprimir
“Quatro cinco seis”.
  Opção 6: Buscar uma palavra e imprimir a linha em que
aparece a primeira ocorrência da palavra
Quando o usuário escolher a opção 6, o programa deve solicitar ao usuário
para digitar a palavra desejada e, em seguida, imprimir a linha em que ela
ocorre a primeira vez. Por exemplo, se o usuário digitar o “quatro” e o texto
presente no arquivo for “Um um dois dois três três.\nQuatro cinco seis”, o
programa deve imprimir “Quatro cinco seis”. Note que para fazer a busca, o
programa não irá diferenciar as maiúsculas e minúsculas. No entanto, para
imprimir a linha encontrada, o programa deve reproduzir as maiúsculas e
minúsculas como no texto original.
Dicas: você pode usar a função find disponível para strings para localizar a
posição de uma palavra texto. Você também pode usar as funções upper ou
lower para fazer as buscas ignorando a diferença entre maiúsculas e minúsculas.
  Opção 7: Substituir todas as ocorrências de uma palavra
por outra
Quando o usuário escolher a opção 7, o programa deve ler três strings pelo
teclado: a primeira uma palavra a ser substituída, a segunda a palavra que
irá substituir a palavra anterior e a terceira o nome do arquivo onde serão
salvos os resultados. Por exemplo, se a primeira string digitada for “três” e a
sequnda string digitada for “zero” e o texto presente no arquivo for ”Um um
dois dois três três”, o programa deve gerar o texto ”Um um dois dois zero
zero”e salvar esse texto em um arquivo formato .txt com o nome fornecido
pelo usuário. Diferentemente da opção anterior, aqui o programa deve diferenciar maiúsculas e minúsculas. Você pode utilizar a função replace para
strings para implementar esta funcionalidade.
  Opção 8: Abrir um outro livro
Quando o usuário escolher a opção 8, o programa deve solicitar ao usuário
para digitar o nome de um novo arquivo .txt que será lido pelo programa. Em
seguida o programa deve imprimir de novo o menu com as funcionalidades
disponíveis para serem executadas com o novo livro aberto.
  Opção 9: Encerrar o programa
Quando o usuário escolher a opção 9, o programa deve ser encerrado.

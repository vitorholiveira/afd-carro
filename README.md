# Autômato Finito Determinístico
O sistema implementado é uma simulação de um carro hipotético. É possível ligar, desligar, abaixar o freio de mão, levantar o freio de mão, acelerar, desacelerar, parar, trocar de marcha e trocar de direção.
## Implementação
Foi implementada a função de transição do AFD, a qual recebe um estado e um símbolo do alfabeto (operação) e devolve o próximo estado. Esse código está disponível em "automato.py". Para saber se uma palavra pertence à linguagem, é possível testá-la digitando símbolo por símbolo ou criar um arquivo csv em que os símbolos estão separados por virgulas. As funções das duas formas de leitura de uma palavra está em "leitura.py". A interface para seleção do modo de interação está em "main.py".
## Diagrama de transição
![carrro_automato](https://github.com/vitorholiveira/afd-carro/assets/62735040/51bb31d1-1a62-46d6-8c3a-17372afa460e)
## Significado dos símbolos do alfabeto
- s	: Ligar
- 0	: Desligar
- ^	: Levantar o freio de mão
- v	: Abaixar o freio de mão
- a	: Acelerar
- f	: Desacelerar
- ! : Frear bruscamente (para o carro)
- m	: Embreagem
- 1	: Primeira marcha
- 2	: Segunda marcha
- 3	: Terceira marcha
- 4	: Quarta marcha
- 5	: Quinta marcha
- n	: Neutro
- d	: Dobrar para a direita
- e	: Dobrar para a esquerda
## Tutorial de uso:
  Existem duas formas de executar o programa: pelo executável correspondente ao seu SO na pasta "executaveis" ou rodando o script "main.py". A única diferença é que o programa do script possui imagens para ilustrar as operações. Ambos os códigos começam em um menu inicial em que o usuário pode escolher entro os modos de interação "input" ou "arquivo":
  - Input: O programa pede um símbolo do alfabeto da linguagem, o qual representa uma operação. Para enviar a entrada, é preciso digitar o símbolo no espaço em branco e clicar no botão "Realizar Operação". Quando o estado atual possuir uma transição com esse símbolo, o estado é atualizado e um nova operação é requisitada. Caso contrário a função é indefinida e o programa reijeita a palavra. Para finalizar a leitura, é preciso clicar no botão "Terminar Percurso". Se o estado atual for final a palavra é aceita, caso contrário é rejeitada.
  - Arquivo: O programa pede o nome do arquivo de entrada (com caminhamento correto), o qual deve ser estar no formato csv em que cada campo possui um símbolo do alfabeto da linguagem. Para enviar o arquivo, é preciso digitar no espaço em branco e clicar no botão "Abrir Arquivo". O botão "Proxima Operação" realizará a transição do estado atual com o primeiro símbolo do arquivo que ainda não foi processado. Também é possível realizar o processamento da palavra de uma vez, clicando no botão reconhecer. Nessa opção a transição é feita até ser indefinida ou até os símbolos do arquivo acabarem.

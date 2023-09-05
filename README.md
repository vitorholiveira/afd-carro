# Autômato Finito Determinístico
O sistema implementado é uma simulação de um carro hipotético. É possível ligar, desligar, abaixar o freio de mão, levantar o freio de mão, acelerar, desacelerar, parar, trocar de marcha e trocar de direção.
## Implementação
Foi implementada a função de transição do AFD, a qual recebe um estado e um símbolo do alfabeto (operação) e devolve o próximo estado. Esse código está disponível em "automato.py". Para saber se uma palavra pertence à linguagem, é possível testá-la digitando símbolo por símbolo no terminal ou criar um arquivo csv em que os símbolos estão separados por virgulas. As funções das duas formas de leitura de uma palavra está em "leitura.py". A interface para seleção do modo de interação está em "main.py".
## Diagrama de transição
![carrro1 jff](https://github.com/vitorholiveira/afd-carro/assets/62735040/82ab3b89-63a1-4d14-a514-5898e78fcde4)
## Significado dos símbolos do alfabeto
- s	: Liga
- 0	: Desliga
- ^	: Levanta o freio de mão
- v	: Abaixa o freio de mão
- a	: Acelera
- f	: Desacelera
- ! : Frea bruscamente (para o carro)
- m	: Embreagem
- 1	: Primeira marcha
- 2	: Segunda marcha
- 3	: Terceira marcha
- 4	: Quarta marcha
- 5	: Quinta marcha
- n	: Neutro
- d	: Girar 90° para a direita
- e	: Girar 90° para a esquerda
## Tutorial de uso:
  Ao executar "main.py", deve-se digitar "1" para selecionar o modo de interação pelo terminal ou "2" para o reconhecedor automático por meio de um arquivo csv. Nos dois modos, o estado inicial é o "i0" e, quando o programa realizar a função de transição, é escrito no terminal a operação realizada pelo motorista acompanhado da própria função.
  - Terminal: O programa pede um símbolo do alfabeto da linguagem, o qual representa uma operação. Quando estado atual possui uma transição com esse símbolo, ele é atualizado e um nova operação é requisitada. Caso contrário a função é indefinida e o programa reijeita a palavra. Para finalizar a leitura, é preciso digitar "fim" ao invés de um símbolo do alfabeto. Se o estado atual for final a palavra é aceita, caso contrário é rejeitada.
  - Arquivo: O programa pede o nome do arquivo de entrada, o qual deve ser estar no formato csv em que cada campo possui um símbolo do alfabeto da linguagem. Para cada caractere, a função de transição é realizada com o estado atual. Se ela for definida, o estado é atualizado, caso contrário, o programa interromperá a computação e a palavra será rejeitada. Ao terminar a leitura do arquivo, se o estado atual for final a palavra é aceita, caso contrário rejeitada.
  
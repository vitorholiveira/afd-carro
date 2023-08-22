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
- d	: Gira 90° para a direita
- e	: Gira 90° para a esquerda


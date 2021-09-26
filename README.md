# Problema do Produtor Consumidor
 
 
**Universidade Veiga de Almeida**  
*Disciplina de Arquitetura e Funcionamento de Sistemas Operacionais*  

Integrantes do grupo:  
André Luiz Braga Vasco de Paula | 20201103664  
Kevin William M. Maia | 20161101736  
Filipe da Silva Machado Silva | 20121104748  
Sérgio Vinícius Mamed | 20201102420  
Ryan de Mello Paladino | 20162102609

## Descrição do problema
- Dois processos compartilham um *buffer* de tamanho fixo
- O Produtor insere informação no *buffer*
- O Consumidor remove informação do *buffer*

## Problemas possíveis
- Produtor insere informação em posição que ainda não foi consumida
- Consumidor remove de posição que já foi consumida

## Algoritmo com espera ocupada
Podemos imaginar uma *solução simples*, onde os processos dentro de um loop **while** ficam aguardando a posição esvaziar ou encher, sem ter comunicação direta com o outro processo.
Vantagens:
- Código simples e intuitivo;

Desvantagens:
- A operação de aguardar pode não ser imediata;

## Utilização de Semáforos
- Semáforos são *contadores especiais* para recursos compartilhados;
- Eles liberam ou interrompem a execução de processos baseados em operações de controle;

## Execução do código
![2021-09-26-11-06-40_Trim](https://user-images.githubusercontent.com/31835560/134811403-6855b840-d0a1-4702-a792-cdfcef841a11.gif)


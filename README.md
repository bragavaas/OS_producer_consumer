﻿# Problema do Produtor Consumidor
 
 
**Universidade Veiga de Almeida**

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

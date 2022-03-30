# Variações do Sugarscape

Por Leonardo Alves Riether - 190032413

## Como Executar
Primeiro, deve-se instalar o framework
[mesa](https://mesa.readthedocs.io/en/latest/) e demais dependências
necessárias com o comando `python3 -m pip install -r requirements.txt`. É
recomendado utilizar um [_virtual environment_](https://docs.python.org/3/library/venv.html), para evitar poluir
o escopo global do Python.

Após isso, basta abrir o terminal no diretório da simulação e executar `mesa runserver`.
De modo equivalente, é possível rodar `python3 run.py`.

A interface de simulação apresenta o Sugarscape, com uma cana-de-açúcar por célula e
várias formigas distribuídas aleatoriamente pelo grid. A cor da cana indica a quantidade
de açúcar presente na célula. No canto esquerdo, podem ser encontrados dois sliders:
- **Ant Reproduce Probability**: seleciona a probabilidade de uma formiga se reproduzir em
  uma certa etapa, dado que ela possui uma quantidade mínima de açúcar armazenada.
- **Growback Factor**: quantidade de crescimento por etapa de cada cana-de-açúcar.

Para rodar a simulação em modo batch, é possível executar o arquivo `batch.py`.
Esse modo grava os dados coletados em arquivos no diretório `csv/`.

## Sugarscape Original

A simulação escolhida como base para fazer as modificações foi a
[sugarscape](https://github.com/projectmesa/mesa/tree/main/examples/sugarscape_cg). Esse
programa simula uma sociedade de formigas que vivem em um campo (grid) de cana-de-açúcar.
As formigas precisam se alimentar da cana para sobreviver, enquanto a cana possui uma taxa
fixa de crescimento, originalmente igual a 1, mas cada posição do grid possui um
determinado máximo de cana que não pode ultrapassar.

Além disso, cada formiga possui um campo de visão limitado, só podendo ver diretamente
acima, abaixo ou para os dois lados, em um determinado raio. A cada etapa do programa, as
formigas utilizam esse campo de visão para se mover ao lugar do grid que possui mais cana
dentro desse campo, para tentar maximizar suas chances de sobreviver.

O programa é baseado no modelo "Netlogo Sugarscape 2 Constant Growback", introduzido por
Epstein e Axtell.

> Li, J. and Wilensky, U. (2009). NetLogo Sugarscape 2 Constant Growback model.
http://ccl.northwestern.edu/netlogo/models/Sugarscape2ConstantGrowback.  Center for
Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

> The ant sprite is taken from https://openclipart.org/detail/229519/ant-silhouette, with
CC0 1.0 license.

## Mudanças Propostas

São propostas as seguintes variações no Sugarscape: 

+ As formigas podem se reproduzir, caso possuam um nível mínimo de açúcar armazenado. Em
  cada etapa, há uma probabilidade de cada formiga se reproduzir, controlada por um
  _slider_ na visualização do navegador.
+ Adicionar a taxa de crescimento da cana-de-açúcar como uma variável do modelo,
  juntamente com um _slider_ que a controle no navegador.
    
Quando as formigas não se reproduzem, a população se estabiliza rapidamente. Por outro
lado, quando a taxa de reprodução é muito alta, é esperado que ou a cana-de-açúcar não
cresça o suficiente para manter o alto número de formigas, ou que a população se
estabilize de um número relativamente alto, por conta da maior dinamicidade do sistema com
taxas mais altas. Com isso, é possível formular a hipótese causal de que, para valores não
muito pequenos, nem muito grandes, a população oscilará por mais tempo e com mais
amplitude antes de chegar à estabilidade.

## Mudanças no Código

As principais mudanças foram as seguintes:
- Introdução das variáveis `self.reproduce_prob` e `self.growback_factor` no modelo
(`SugarscapeCg`). Essas variáveis controlam, respectivamente, a probabilidade de que uma
formiga se reproduza em uma dada etapa da simulação e a quantidade de crescimento por
etapa de cada cana-de-açúcar.
- Criação de dois sliders em `src/server.py`, por meio da variável `params`, que controlam
os fatores `reproduce_prob` e `growback_factor` citados anteriormente.
- Implementação de um método `reproduce` na classe dos agentes/formigas (`SsAgent`), que
pode gerar, com certa probabilidade, uma formiga filha, na mesma posição que a formiga
pai, caso o pai tenha mais que `1.5` unidades de açúcar. Caso seja feita a criação de um
novo agente, o pai dá metade do seu açúcar para o filho, para que não seja criado açúcar a
partir desse processo.
- Envio do `growback_factor` aos agentes da classe `Sugar`, em `src/agents.py`, além de
seu uso no método `step`.
- Criação da classe `MovingStats` no arquivo `src/moving_stats.py`, que mensura uma média
  móvel de 50 passos da população e calcula uma medida de oscilação `osc`, que é uma
  espécie de média geométrica entre o tempo que a população fica acima da média e abaixo
  dela. Essas medidas são utilizadas para comparar diferentes simulações e testar a
  hipótese causal.
- Correção de um bug na criação de SsAgents do Sugarscape, em `src/model.py`, que gerava o
mesmo `unique_id` para formigas distintas, o que levava algumas formigas a serem
sobrescritas no escalonador e ficarem paradas até o final da simulação. A correção pode
ser vista [neste commit](https://github.com/LeoRiether/SugarscapeVariations/commit/71991c4f30fb71dc4d3b4bb3fad103535743dbda#diff-f9626810656f0fce88d60f204a11125e00df081ded6cc2bff95922ea8e177b62L19-R24) 

## Variáveis Armazenadas nos Arquivos CSV
Os arquivos CSV gerados durante as simulações são gravados no diretório `csv/`. Existem
dois tipos de arquivos, os de variáveis de agentes e os do modelo, que possuem os prefixos
`agent_` e `model_`, respectivamente. Algumas colunas estão presentes em ambos os tipos.
São elas

- **RunId:** identificador da execução
- **iteration:** são feitas várias simulações com os mesmos parâmetros, para diminuir o
erro envolvido na análise. A variável `iteration` identifica uma iteração com um certo
conjunto de parâmetros.
- **Step:** etapa da simulação
- **reproduce_prob:** probabilidade de reprodução de uma dada formiga
- **growback_factor:** quantidade de crescimento por etapa das canas-de-açúcar

Os arquivos `agent_` posuem, além dessas colunas, a coluna
- **SsAgent:** tamanho da população de formigas vivas no sugarscape na última etapa da
  simulação

Os arquivos `model_` adicionam as seguintes colunas:
- **Average**: média da população de formigas nos últimos 50 passos da simulação
- **Oscillation**: medida de oscilação da população de formigas ao longo da simulação
  inteira, definida na classe `MovingStats`, no arquivo `src/moving_stats.py`.


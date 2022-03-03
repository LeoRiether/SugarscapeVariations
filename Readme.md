# Variações do Sugarscape

Por Leonardo Alves Riether - 190032413

## Como Executar
Primeiro, deve-se instalar o framework
[mesa](https://mesa.readthedocs.io/en/latest/) e demais dependências necessárias
com o comando `python3 -m pip install -r requirements.txt`. É recomendado utilizar um
[_virtual environment_](https://docs.python.org/3/library/venv.html), para
evitar poluir o escopo global do Python.

Após isso, basta abrir o terminal no diretório da simulação e executar `mesa runserver`.
De modo equivalente, é possível rodar `python3 run.py`.

## Sugarscape Original
TODO: explicar `mesa/examples/sugarscape_cg`

This is Epstein & Axtell's Sugarscape Constant Growback model, with a detailed
description in the chapter 2 of Growing Artificial Societies: Social Science from the Bottom Up

A simple ecological model, consisting of two agent types: ants, and sugar
patches.

The ants wander around according to Epstein's rule M:
- Look out as far as vision pennies in the four principal lattice directions and identify the unoccupied site(s) having the most sugar. The order in which each agent search es the four directions is random.
- If the greatest sugar value appears on multiple sites then select the nearest one. That is, if the largest sugar within an agent s vision is four, but the value occurs twice, once at a lattice position two units away and again at a site three units away, the former is chosen. If it appears at multiple sites the same distance away, the first site encountered is selected (the site search order being random).
- Move to this site. Notice that there is no distinction between how far an agent can move and how far it can see. So, if vision equals 5, the agent can move up to 5 lattice positions north , south, east, or west.
- Collect all the sugar at this new position.

The sugar patches grow at a constant rate of 1 until it reaches maximum capacity. If ant metabolizes to the point it has zero or negative sugar, it dies.


The model is tests and demonstrates several Mesa concepts and features:
 - MultiGrid
 - Multiple agent types (ants, sugar patches)
 - Overlay arbitrary text (wolf's energy) on agent's shapes while drawing on CanvasGrid
 - Dynamically removing agents from the grid and schedule when they die

## Files

* ``sugarscape/agents.py``: Defines the SsAgent, and Sugar agent classes.
* ``sugarscape/schedule.py``: This is exactly based on wolf_sheep/schedule.py.
* ``sugarscape/model.py``: Defines the Sugarscape Constant Growback model itself
* ``sugarscape/server.py``: Sets up the interactive visualization server
* ``run.py``: Launches a model visualization server.

## Further Reading

This model is based on the Netlogo Sugarscape 2 Constant Growback:

Li, J. and Wilensky, U. (2009). NetLogo Sugarscape 2 Constant Growback model.
http://ccl.northwestern.edu/netlogo/models/Sugarscape2ConstantGrowback.
Center for Connected Learning and Computer-Based Modeling,
Northwestern University, Evanston, IL.

The ant sprite is taken from https://openclipart.org/detail/229519/ant-silhouette, with CC0 1.0 license.

## Mudanças Propostas


Especificação da Tarefa (copiada do LaTeX da disciplina)
--------------------------------------------------------

Nessa tarefa você vai:

-   criar um novo laboratório de simulação;

-   iniciar a realização de seus primeiros experimentos de simulação.

.

A tarefa é individual, e de forma operacional consiste em codificar,
descrever e executar uma simulação em Python, usando o framework Mesa, a
partir de mudanças no código de qualquer um dos exemplos disponíveis no
conjunto de exemplos disponível na distribuição padrão do *framework*
Mesa, com exceção do exemplo BoltzmannWealthModel.

A codificação e descrição equivalem a criar um laboratório de simulação
experimental.

A execução da simulação corresponde à realização de experimentos de
simulação.

### O código: Criação do Laboratório

#### Características do Laboratório

O código da simulação apresentada deve atender às seguintes
características, em relação ao código original:

-   Deve apresentar uma variação no comportamento do modelo e no
    comportamento dos agentes. As duas variações podem ser mínimas, mas
    precisam ser justificadas, baseadas em alguma hipótese causal que
    você deve declarar, sobre o seu entendimento do modelo que está
    sendo simulado;

-   Deve permitir que pelo menos um parâmetro ou variável de controle
    adicional possa ser manipulável na interface do usuário, na parte
    interativa do modelo. A sua hipótese causal deve estar relacionada
    com essa variável manipulável;

-   Deve apresentar, na interface de interação com a simulação, algum
    gráfico mostrando a variação de dados de efeito, necessariamente
    relacionados com a sua hipótese causal. Podem ser os mesmos dados já
    existentes na simulação original, ou novos dados que você acha
    importante serem apresentados;

-   Deve coletar e gravar dados gerados durante cada execução da
    simulação, em dois arquivos no formato CSV, usando as ferramentas
    próprias do framework, apresentadas na URL
    <https://mesa.readthedocs.io/en/stable/tutorials/intro_tutorial.html#collecting-data>.
    Um dos arquivos contém os dados de variáveis no nível do modelo, e
    outro de variáveis no nível do agente, por exemplo:

    -   `model_data_iter_10_steps_10_2021-11-05 17:32:12.906885.csv`

    -   `agent_data_iter_10_steps_10_2021-11-05 17:32:12.906885.csv`

#### A entrega do Laboratório

Para depositar o código fonte do simulador, atenda aos seguintes
aspectos de organização:

-   O seu código deve estar em um repositório em sua conta individual no
    git, usando um nome `<project-name>`, para o modelo criado,
    possivelmente uma pequena variação em relação ao nome do diretório
    onde se encontra a simulação usada como base. Por exemplo, o nome do
    seu `<project-name>` pode ser `boltzmann_wealth_model_greedy`, com
    uma url
    [https://github.com/&lt;githubusername&gt;/&lt;project-name&gt;](https://github.com/<githubusername>/<project-name>);

-   No raiz do seu repositório, o arquivo `Readme.md` deve conter:

    -   Apresentação do novo modelo, em sua relação ao modelo original;

    -   Descrição da hipótese causal que você deseja comprovar;

    -   Justificativa para as mudanças que você fez, em relação ao
        código original;

    -   Orientação sobre como usar o simulador; e

    -   Descrição das variáveis armazenadas no arquivo CSV;

    -   Quaisquer outras informações que você julgue importante;

-   O resto do repositório deve conter o seu código.

Ao concluir o seu código crie uma subtree dentro do diretório a seguir,
no repositório central da disciplina:

`experiments/<githubusername>/labs/`

Dentro do diretório labs deve haver um ponteiro para o repositório onde
você desenvolveu o seu simulador. Use o comando abaixo para criar esse
ponteiro:

    git subtree add --prefix experiments/<githubusername>/labs/<project-name> 
        https://github.com/<githubusername>/<project-name>|mesa master --squash

Não se esqueça de enviar suas mudanças para o repositório central com
`git pull`.

Para mais detalhes sobre o que faz o comando `git subtree` veja as urls
<https://stackoverflow.com/questions/36554810/how-to-link-folder-from-a-git-repo-to-another-repo>
e <https://blog.developer.atlassian.com/the-power-of-git-subtree/>

Dados de Simulação: Os experimentos iniciais
--------------------------------------------

Além de depositar os código fonte, você precisa depositar pelo menos
três pares de arquivos CSV (*Comma Separated Values*), que apresentem
resultados de três simulações (experimentos), com distintos valores para
as variáveis de controle apresentadas na interface do usuário,
especialmente as variáveis que você introduziu no modelo.

Os nomes de cada arquivo CSV devem permitir fácil identificação dos
parâmetros e valores usados na execução da simulação, por exemplo, os
quatro arquivos a seguir listados indicariam os dados da execução de
duas simulações (experimentos), uma delas com o valor da variável
**greedy** True, outro com o valor False:

-   `agent_data_greedy_True`

-   `model_data_greedy_True`

-   `agent_data_greedy_False`

-   `model_data_greedy_False`

Os arquivos devem estar armazenados no diretório **experiments /
&lt;githubusername&gt; / Experimento-&lt;nome-do-experimento&gt; /
&lt;data-experimento&gt; /**, onde:

-   `<nome-do-experimento>` é um nome que você escolheu para o
    experimento, baseado na sua hipótese causal. Perceba que o nome do
    experimento deve obedecer às regras de nomeação de arquivos, já
    indicadas das orientações iniciais deste documento;

-   `<data-experimento>` é a data em que você executou o experimento, no
    formato AAAAMMDD;

.

Use o Overleaf (ou o git) para depositar nos diretórios os arquivos
gerados durante os experimentos (execução da simulação).

Opcionalmente, recomenda-se que os nomes individuais dos arquivos
contenham a data e hora de término da simulação.

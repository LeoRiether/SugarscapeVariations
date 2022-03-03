# Variações do Sugarscape

Por Leonardo Alves Riether - 190032413

## Como Executar Primeiro, deve-se instalar o framework
[mesa](https://mesa.readthedocs.io/en/latest/) e demais dependências necessárias com o
comando `python3 -m pip install -r requirements.txt`. É recomendado utilizar um [_virtual environment_](https://docs.python.org/3/library/venv.html), para evitar poluir o escopo
global do Python.

Após isso, basta abrir o terminal no diretório da simulação e executar `mesa runserver`.
De modo equivalente, é possível rodar `python3 run.py`.

## Sugarscape Original TODO: explicar `mesa/examples/sugarscape_cg`

A simulação escolhida como base para fazer as modificações foi a
[sugarscape](https://github.com/projectmesa/mesa/tree/main/examples/sugarscape_cg). Esse
programa simula uma sociedade de formigas que vivem em um campo (grid) de cana de açúcar.
As formigas precisam se alimentar da cana para sobreviver, enquanto a cana possui uma taxa
fixa de crescimento, originalmente igual a 1, mas cada posição do grid possui um
determinado máximo de cana que pode possuir.

Além disso, cada formiga possui um campo de visão limitado, só podendo ver diretamente
acima, abaixo ou para os dois lados, em um determinado raio. A cada etapa do programa, as
formigas utilizam esse campo de visão para se mover ao lugar do grid que possui mais cana
dentro desse campo, para tentar maximizar suas chances de sobreviver.

O programa é baseado no modelo "Netlogo Sugarscape 2 Constant Growback", introduzido por
Epstein e Axtell.

Li, J. and Wilensky, U. (2009). NetLogo Sugarscape 2 Constant Growback model.
http://ccl.northwestern.edu/netlogo/models/Sugarscape2ConstantGrowback.  Center for
Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

The ant sprite is taken from https://openclipart.org/detail/229519/ant-silhouette, with
CC0 1.0 license.

## Mudanças Propostas

São propostas as seguintes variações no Sugarscape: 

+ As formigas podem se reproduzir, caso possuam um nível mínimo de açúcar armazenado. Em
cada etapa, há uma probabilidade de cada formiga se reproduzir, controlada por um _slider_
na visualização do navegador.
    - **Efeito esperado**: enquanto no Sugarscape original a população de formigas tendia
    à estabilidade, com a introdução dessa mudança é esperado que a população oscile para
    sempre, dada uma taxa de reprodução suficientemente grande.
+ Adicionar a taxa de crescimento da cana de açúcar como uma variável do modelo,
juntamente com um _slider_ que a controle no navegador.
    - **Efeito esperado**: quanto maior a taxa de crescimento, maior será a população
    média das formigas durante as últimas etapas da simulação (ignoramos as primeiras
    etapas, porque a população não é estável o suficiente nessa parte).

------------------------------------------------------------------------------------------

## Especificação da Tarefa (copiada do LaTeX da disciplina)

Nessa tarefa você vai:

-   criar um novo laboratório de simulação;

-   iniciar a realização de seus primeiros experimentos de simulação.

.

A tarefa é individual, e de forma operacional consiste em codificar, descrever e executar
uma simulação em Python, usando o framework Mesa, a partir de mudanças no código de
qualquer um dos exemplos disponíveis no conjunto de exemplos disponível na distribuição
padrão do *framework* Mesa, com exceção do exemplo BoltzmannWealthModel.

A codificação e descrição equivalem a criar um laboratório de simulação experimental.

A execução da simulação corresponde à realização de experimentos de simulação.

### O código: Criação do Laboratório

#### Características do Laboratório

O código da simulação apresentada deve atender às seguintes características, em relação ao
código original:

-   Deve apresentar uma variação no comportamento do modelo e no
    comportamento dos agentes. As duas variações podem ser mínimas, mas precisam ser
    justificadas, baseadas em alguma hipótese causal que você deve declarar, sobre o seu
    entendimento do modelo que está sendo simulado;

-   Deve permitir que pelo menos um parâmetro ou variável de controle
    adicional possa ser manipulável na interface do usuário, na parte interativa do
    modelo. A sua hipótese causal deve estar relacionada com essa variável manipulável;

-   Deve apresentar, na interface de interação com a simulação, algum
    gráfico mostrando a variação de dados de efeito, necessariamente relacionados com a
    sua hipótese causal. Podem ser os mesmos dados já existentes na simulação original, ou
    novos dados que você acha importante serem apresentados;

-   Deve coletar e gravar dados gerados durante cada execução da
    simulação, em dois arquivos no formato CSV, usando as ferramentas próprias do
    framework, apresentadas na URL
    <https://mesa.readthedocs.io/en/stable/tutorials/intro_tutorial.html#collecting-data>.
    Um dos arquivos contém os dados de variáveis no nível do modelo, e outro de variáveis
    no nível do agente, por exemplo:

    -   `model_data_iter_10_steps_10_2021-11-05 17:32:12.906885.csv`

    -   `agent_data_iter_10_steps_10_2021-11-05 17:32:12.906885.csv`

#### A entrega do Laboratório

Para depositar o código fonte do simulador, atenda aos seguintes aspectos de organização:

-   O seu código deve estar em um repositório em sua conta individual no
    git, usando um nome `<project-name>`, para o modelo criado, possivelmente uma pequena
    variação em relação ao nome do diretório onde se encontra a simulação usada como base.
    Por exemplo, o nome do seu `<project-name>` pode ser `boltzmann_wealth_model_greedy`,
    com uma url
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

Ao concluir o seu código crie uma subtree dentro do diretório a seguir, no repositório
central da disciplina:

`experiments/<githubusername>/labs/`

Dentro do diretório labs deve haver um ponteiro para o repositório onde você desenvolveu o
seu simulador. Use o comando abaixo para criar esse ponteiro:

    git subtree add --prefix experiments/<githubusername>/labs/<project-name>
    https://github.com/<githubusername>/<project-name>|mesa master --squash

Não se esqueça de enviar suas mudanças para o repositório central com `git pull`.

Para mais detalhes sobre o que faz o comando `git subtree` veja as urls
<https://stackoverflow.com/questions/36554810/how-to-link-folder-from-a-git-repo-to-another-repo>
e <https://blog.developer.atlassian.com/the-power-of-git-subtree/>

Dados de Simulação: Os experimentos iniciais --------------------------------------------

Além de depositar os código fonte, você precisa depositar pelo menos três pares de
arquivos CSV (*Comma Separated Values*), que apresentem resultados de três simulações
(experimentos), com distintos valores para as variáveis de controle apresentadas na
interface do usuário, especialmente as variáveis que você introduziu no modelo.

Os nomes de cada arquivo CSV devem permitir fácil identificação dos parâmetros e valores
usados na execução da simulação, por exemplo, os quatro arquivos a seguir listados
indicariam os dados da execução de duas simulações (experimentos), uma delas com o valor
da variável **greedy** True, outro com o valor False:

-   `agent_data_greedy_True`

-   `model_data_greedy_True`

-   `agent_data_greedy_False`

-   `model_data_greedy_False`

Os arquivos devem estar armazenados no diretório **experiments / &lt;githubusername&gt; /
Experimento-&lt;nome-do-experimento&gt; / &lt;data-experimento&gt; /**, onde:

-   `<nome-do-experimento>` é um nome que você escolheu para o
    experimento, baseado na sua hipótese causal. Perceba que o nome do experimento deve
    obedecer às regras de nomeação de arquivos, já indicadas das orientações iniciais
    deste documento;

-   `<data-experimento>` é a data em que você executou o experimento, no
    formato AAAAMMDD;

.

Use o Overleaf (ou o git) para depositar nos diretórios os arquivos gerados durante os
experimentos (execução da simulação).

Opcionalmente, recomenda-se que os nomes individuais dos arquivos contenham a data e hora
de término da simulação.

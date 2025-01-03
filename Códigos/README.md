 # README

## Introdução

O código dos laboratórios foi adaptado do repositório https://github.com/qx0731/Sharing_ISL_python.

## Baixando os dados

Em primeiro lugar, crie uma pasta no seu computador para guardar os arquivos do curso. Ao longo desse documento vamos usar, como exemplo, `~/cursos/ml2023/labs`. Aqui, o til "~" quer dizer a sua pasta-base como usuário. No caso de Windows, é  `C:\Users\<CurrentUserName>`, e, no caso de macOS e Linux, é `/Users/<CurrentUserName>`.

Baixe todos os dados (os arquivos que terminam em ".csv") e coloque-os na pasta `~/cursos/ml2023/labs/data`

## Baixe Anaconda

Vamos usar Python. Precisaremos instalar uma série de pacotes no sistema para poder rodar modelos de machine learning sem precisar escrever código do zero. Isso frequentemente leva a inconsistências no sistema, caso você já esteja usando Python em outros projetos. Por isso, é altamente recomendado que você tenha como isolar o ambiente onde vamos instalar esses pacotes dos outros ambientes de Python que você já tem no seu computador (em algum sentido, isso é como criar um novo usuário no computador). 

Nesse curso vamos usar Anaconda para criar um ambiente de Python separado. Se você não tiver Anaconda, instale-o seguindo as instruções aqui: https://docs.anaconda.com/anaconda/install/index.html.

## Criando e usando novos ambientes no Anaconda

Depois de instalar Anaconda, vamos criar um novo ambiente para o curso. No seu terminal, rode

```shell
conda create --name ml2023 python=3.10
```

Para ativar o nosso ambiente, precisaremos rodar, no terminal,

```shell
conda activate ml2023
```

Para desativar, e voltar ao seu ambiente usual, basta rodar

```shell
conda deactivate
```

## Instalando pacotes no Anaconda

Agora, precisamos instalar os pacotes que queremos usar nesse ambiente

```
conda install -c conda-forge ipykernel numpy matplotlib pandas statsmodels scikit-learn scipy seaborn notebook lifelines
```

Se depois precisarmos instalar mais pacotes, e.g., `keras` e `tensorflow`, basta rodar

```
conda install -c conda-forge keras tensorflow
```

## Rodando Jupyter

Agora, podemos abrir o Jupyter, que é o ambiente onde rodaremos o nosso código por permitir que vejamos imediatamente o resultado do nosso código. Para isso, usando o terminal, primeiro navegue para a pasta `labs`:

```shell
cd ~/cursos/ml2023/labs
```

Acima, "cd" significa "change directory", e troca a pasta para a indicada (como se nós usássemos o Windows Explorer ou Finder para entrar na pasta). Depois, rode o Jupyter:

```shell
jupyter notebook
```

Uma página deve abrir no seu navegador com o ambiente Jupyter.
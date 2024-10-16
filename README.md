# Avaliação - AnaliseDadosBrasileirao

O projeto **AnaliseDadosBrasileirao** tem como objetivo fornecer uma aplicação interativa em Python que permita a visualização e análise de estatísticas detalhadas dos jogos do Campeonato Brasileiro Série A desde 2003. Usando dados armazenados em um arquivo CSV, a aplicação permite que os usuários explorem diferentes estatísticas por meio de abas como **Tabela**, **Cubo** e **Dashboard**.

## Sobre a Base de Dados

A base de dados utilizada está localizada no arquivo **data/base.csv** e contém informações detalhadas sobre os jogos do Campeonato Brasileiro Série A. Os dados abrangem aspectos como times, rodadas, estádios, placares, entre outras informações essenciais para a análise do desempenho das equipes ao longo dos anos.

## Classificação das Colunas conforme modelo multidimensional (4W1H)

- **Quem (Who):** Refere-se aos sujeitos envolvidos nos jogos. Colunas: **Time Mandante**, **Time Visitante**, **Árbitro**.
- **O quê (What):** Refere-se ao objeto ou conteúdo dos jogos. Colunas: **Gols Marcados**, **Placar Final**, **Número de Faltas**.
- **Onde (Where):** Refere-se à localização geográfica dos jogos. Colunas: **Estádio**, **Cidade**.
- **Quando (When):** Refere-se ao tempo em que os jogos ocorreram. Colunas: **Ano**, **Rodada**, **Data da Partida**.
- **Como (How):** Refere-se ao método de quantificação dos eventos. Colunas: **Posse de Bola**, **Finalizações**, **Escanteios**, **Cartões Amarelos**, **Cartões Vermelhos**.

## Implementação de Cubo de Dados

A aplicação **AnaliseDadosBrasileirao** permite ao usuário criar e manipular cubos de dados com base nas informações dos jogos. O cubo oferece a opção de selecionar dimensões como **Time**, **Estádio** e **Rodada**, e medidas como **Gols Marcados** ou **Posse de Bola**. A agregação desses valores pode ser feita através de funções como soma, média, contagem, entre outras, fornecendo uma visão multidimensional dos dados.

## Visualização

A aplicação oferece diversos tipos de visualizações de dados, permitindo que os usuários escolham entre várias dimensões e medidas para gerar gráficos:
- **Gráfico de Linhas e Barras:** Para mostrar o desempenho dos times ao longo das rodadas e anos.
- **Histograma:** Para visualizar a distribuição de estatísticas como número de gols por partida.
- **Gráfico de Dispersão:** Para correlacionar diferentes medidas, como posse de bola e número de gols.
- **Gráfico de Pizza:** Para mostrar a distribuição de vitórias, empates e derrotas dos times ao longo das temporadas.

## Rotinas com base na análise de dados

Aqui estão algumas rotinas sugeridas para análise dos dados dos jogos do Campeonato Brasileiro Série A:

### 1. Análise Descritiva

- **Rotina 1: Estatísticas Básicas por Time e Estádio**
  - **Objetivo:** Obter estatísticas descritivas, como média de gols marcados e posse de bola, segmentadas por time e estádio.
  - **Passos:**
    - Selecionar as colunas: "Time Mandante", "Estádio" como dimensões e "Gols Marcados", "Posse de Bola" como medidas.
    - Calcular as estatísticas descritivas, como média, mediana e desvio padrão.

- **Rotina 2: Distribuição de Gols e Faltas**
  - **Objetivo:** Analisar a distribuição de gols marcados e faltas ao longo dos anos e rodadas.
  - **Passos:**
    - Selecionar as colunas: "Ano", "Rodada" e "Gols Marcados" ou "Faltas Cometidas".
    - Gerar histogramas para visualizar a distribuição dessas estatísticas.

### 2. Análise Diagnóstica

- **Rotina 1: Tendências de Desempenho por Time**
  - **Objetivo:** Identificar como o desempenho dos times variou ao longo das temporadas, observando estatísticas como gols marcados e posse de bola.
  - **Passos:**
    - Selecionar colunas: "Ano", "Time Mandante" e "Gols Marcados".
    - Criar gráficos de linha para visualizar a variação de desempenho dos times ao longo dos anos.

- **Rotina 2: Análise de Desvios por Rodada**
  - **Objetivo:** Examinar como os desempenhos dos times variam de acordo com a rodada e identificar padrões de jogo.
  - **Passos:**
    - Selecionar colunas: "Rodada", "Time Mandante" e "Gols Marcados".
    - Calcular desvios padrão para entender a variabilidade do desempenho por rodada.

---

Este documento descreve as principais rotinas de análise que podem ser realizadas no **AnaliseDadosBrasileirao**. A aplicação foi desenvolvida para ser uma ferramenta interativa, permitindo explorar diferentes dimensões e medidas dos jogos do Campeonato Brasileiro Série A.


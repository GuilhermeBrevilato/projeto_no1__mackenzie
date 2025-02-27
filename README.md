# Inteligência para Rastreamento de Veículos: Análise Mercadológica
## Descrição do Projeto
Este projeto tem como objetivo analisar a viabilidade mercadológica de uma solução inovadora de rastreamento veicular baseada em IoT (Internet das Coisas) e inteligência artificial. A proposta busca aumentar a segurança no trânsito, reduzir custos operacionais e minimizar o impacto ambiental dos veículos automotores.

O foco principal é responder às seguintes questões:
* Existe demanda para o produto?
* Quem é o público-alvo?
* Quais são as tendências do mercado?
* Como a solução se diferencia da concorrência?

A análise será conduzida com base em dados de acidentes de trânsito, informações sobre o mercado automotivo e tendências tecnológicas, utilizando técnicas de ciência de dados.

## Estrutura do Repositório

A organização dos arquivos no repositório segue a seguinte estrutura:

```
├── data/                     # Dados brutos e tratados
│   ├── raw/                  # Dados brutos originais
│   ├── processed/            # Dados tratados e prontos para análise
├── notebooks/                # Notebooks Jupyter com análises exploratórias e inferenciais
├── reports/                  # Relatórios e apresentações gerados
│   ├── figures/              # Gráficos e visualizações geradas
├── src/                      # Scripts utilizados no projeto
│   ├── data_preparation.py   # Código para limpeza e preparação dos dados
│   ├── eda.py                # Código para análise exploratória de dados
├── README.md                 # Arquivo explicativo do projeto (este documento)
├── requirements.txt          # Dependências necessárias para replicar o projeto
└── LICENSE                   # Licença do projeto
```

## Objetivos
O estudo visa:
1. Determinar a viabilidade mercadológica da solução.
2. Identificar o público-alvo e suas necessidades.
3. Avaliar as tendências tecnológicas que podem impactar a aceitação do produto.
4. Analisar os custos econômicos relacionados aos acidentes de trânsito e como a solução pode mitigá-los.

## Datasets Utilizados

**Fontes de Dados**
* Dados sobre acidentes de trânsito no Brasil:
  * SENATRAN - RENAEST
  * ANAMT - Estatísticas sobre acidentes
* Informações sobre tendências tecnológicas:
  * Telit Cinterion
  * Histórico da Telit Cinterion

**Metadados**
* Período de coleta: Dados mais recentes disponíveis até fevereiro de 2025.
* Limitações:
  * Alguns dados podem estar incompletos ou desatualizados.
  * Dados públicos sujeitos a limitações de granularidade.
* Organização:
  * Dados brutos estão na pasta data/raw/.
  * Dados tratados estão na pasta data/processed/.

## Tecnologias Utilizadas
O projeto faz uso das seguintes ferramentas:
* Linguagem: Python (versão >= 3.8)
* Bibliotecas principais:
  * Pandas (manipulação de dados)
  * Matplotlib e Seaborn (visualização)
  * Scikit-learn (análise estatística e aprendizado de máquina)
  * Jupyter Notebook (documentação e análise interativa)

Para instalar as dependências, execute:

```
pip install -r requirements.txt
```

## Como Reproduzir o Projeto
1. Clone este repositório:
```
git clone https://github.com/seu-repositorio/rastreamento-veicular.git
```
2. Navegue até a pasta do projeto:
```
cd rastreamento-veicular
```
Instale as dependências listadas no arquivo requirements.txt:
```
pip install -r requirements.txt
```
Execute os notebooks na pasta notebooks/ para reproduzir as análises.

## Cronograma do Projeto
| Atividade |	Data de Conclusão |	Responsável |
|-----------|-------------------|-------------|
| Coleta e organização dos dados |   |   |
| Limpeza e preparação dos dados |   |   |
| Análise exploratória |   |   |
| Relatório final |   |   |

## Equipe
Este projeto foi desenvolvido como parte da disciplina "Projeto Aplicado I" do curso "Tecnologia em Banco de Dados: Análise, Mineração e Engenharia de Dados" da Universidade Presbiteriana Mackenzie.

**Integrantes:**
* Felipe Neres Silva Bezerra
* Guilherme da Silva Brevilato
* Ricardo de Oliveira Vieira Franco

**Docente Orientador:**
* Prof. Dr. Fábio Silva Lopes

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
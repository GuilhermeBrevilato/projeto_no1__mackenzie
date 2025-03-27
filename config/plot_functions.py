import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns


def num_const(num):
    if num > 1000000000000:
        return f'{num/1000000000000:.1f} tri.'
    if num > 1000000000:
        return f'{num/1000000000:.1f} bi.'
    if num > 1000000:
        return f'{num/1000000:.1f} mi.'
    if num > 1000:
        return f'{num/1000:.1f} mil'
    return f'{num:.0f}'


def histograma(df,coluna,títulos):
    # Configura o tamanho da figura
    plt.figure(figsize=(10, 6))
    
    # Gera o histograma com Seaborn
    sns.histplot(data=df, x=coluna, bins=20, kde=True)
    
    # Adiciona título e rótulos de eixo
    plt.title(títulos)
    plt.xlabel('')
    plt.ylabel('')
    
    # Exibe o gráfico
    plt.grid(True)
    plt.show()


def grafico_linhas(x, y, nome_x, nome_y, titulo=''):
    # Criar figura e eixos
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plotar os dados com Seaborn
    sns.lineplot(x=x, y=y, ax=ax, marker='.', linestyle='-', color='blue')
    
    # Limitar os ticks nos eixos usando MaxNLocator
    ax.xaxis.set_major_locator(MaxNLocator(nbins=15))  # Limitar ticks no eixo X
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Limitar ticks no eixo Y
    
    # Configurar título e rótulos dos eixos
    ax.set_title(titulo)
    ax.set_xlabel(nome_x)
    ax.set_ylabel(nome_y)
    
    # Adicionar grade ao gráfico
    ax.grid(True)
    
    # Mostrar o gráfico
    plt.show()


def correlação_heatmap(df):
    # Calculando a matriz de correlação
    correlation_matrix = df.corr()

    # Criando o heatmap com azul no zero e vermelho no ±1
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', linewidths=0.5)
    plt.title('Heatmap da Matriz de Correlação (Azul no Zero)')
    plt.show()


def barras_absolutas(série,top_n=15):

    # Calcular a frequência relativa
    frequencia_absoluta = série.value_counts()
    
    # Limitar aos top N valores
    if len(frequencia_absoluta) > top_n:
        frequencia_absoluta = frequencia_absoluta.head(top_n)

    if série.nunique() > 8:
        largura = 14
    else:
        largura = 8

    # Plotar o gráfico de barras
    plt.figure(figsize=(largura, 6))

    # Adicionar os valores acima das barras
    for index, value in enumerate(frequencia_absoluta):
        plt.text(index, value*1.007, num_const(value), ha='center', fontsize=10)

    frequencia_absoluta.plot(kind='bar', color='skyblue')
    plt.title(f'Frequência Absoluta de {série.name}')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()


def barras_percentuais(série,top_n=15):

    # Calcular a frequência relativa
    frequencia_relativa = série.value_counts(normalize=True) * 100
    
    # Limitar aos top N valores
    if len(frequencia_relativa) > top_n:
        frequencia_relativa = frequencia_relativa.head(top_n)

    if série.nunique() > 8:
        largura = 14
    else:
        largura = 8

    # Plotar o gráfico de barras
    plt.figure(figsize=(largura, 6))

    # Adicionar os valores acima das barras
    for index, value in enumerate(frequencia_relativa):
        plt.text(index, value*1.007, f'{value:.2f} %', ha='center', fontsize=10)

    frequencia_relativa.plot(kind='bar', color='skyblue')
    plt.title(f'Frequência Relativa de {série.name}')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()


def barras_agregadas(df, Grupo, Categ, top_n=(4,4)):

    # Contar as ocorrências de cada espécie e ordenar do mais frequente para o menos frequente
    group_counts = df[Grupo].value_counts()
    categ_counts = df[Categ].value_counts()

    # Selecionar as 3 espécies mais frequentes
    top_group = group_counts.nlargest(top_n[0]).index.tolist()

    # Selecionar o sexo mais frequente
    top_categ = categ_counts.nlargest(top_n[1]).index.tolist()

    plt.figure(figsize=(20, 8))

    # Criar o gráfico de barras agrupadas por espécie e sexo, mostrando a contagem
    g = sns.catplot(
        data=df, kind="count",
        x=Grupo, hue=Categ,
        order=top_group,
        hue_order=top_categ,
        palette='viridis', alpha=.6, height=6
    )
    
    #sns.move_legend(g, "upper right", bbox_to_anchor=(1, 1))
    sns.move_legend(g, loc='upper right', bbox_to_anchor=(0.7, 0.9))

    # Verticalização dos rótulos do eixo X
    plt.xticks(rotation=90)

    g.despine(left=True)
    g.set_axis_labels(Grupo, '')
    g.legend.set_title(Categ)

    fig = plt.gcf()  # get current figure
    fig.set_size_inches(20, 8)

    plt.show()


def valor_por_categorias(df,Categoria,Valor,medida='Soma',top_n=10):
    if medida == 'Soma':
        estimator = np.sum
    if medida == 'Média':
        estimator = np.mean
    if medida == 'Máximo':
        estimator = np.max

        # Agregar os dados
    df_agg = df.groupby(Categoria)[Valor].agg(estimator).reset_index()
    df_agg = df_agg.sort_values(Valor, ascending=False)

    # Limitar o número de categorias se top_n for especificado
    if top_n is not None:
        df_agg = df_agg.head(top_n)

    # Criar o gráfico de barras com médias por categoria
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=df_agg, x=Categoria, y=Valor, errorbar=None, palette='cubehelix')

    plt.xticks(rotation=90)

    # Configurar rótulos e título
    ax.set_title(f'{medida} de {Valor} por {Categoria}')
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Adicionar os valores das barras nos topos das barras
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.5,num_const(p.get_height()), ha='center', fontsize=10)
        #ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.5,num_const(p.get_height()) f'{p.get_height():.2f}', ha='center', fontsize=10)

    # Adicionar uma linha horizontal no valor zero para representar o eixo X
    ax.axhline(0, color='black', linewidth=1)  # Linha preta no valor 0

    # Mostrar o gráfico
    plt.tight_layout()
    plt.show()

def contingência(df,coluna1,coluna2):

    # Criar a tabela de contingência (frequência absoluta)
    contingencia = pd.crosstab(df[coluna1], df[coluna2])

    # Normalizar para obter percentuais
    #contingencia_percentual = contingencia.div(contingencia.sum(axis=1), axis=0) * 100
    contingencia_percentual = contingencia.div(len(df)) * 100

    # Criar o heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(contingencia_percentual, annot=True, cmap='coolwarm', vmin=0, vmax=100, fmt='.2f')
    plt.title(f'Tabela Cruzada - {coluna1} X {coluna2}')
    plt.xlabel(coluna2)
    plt.ylabel(coluna1)
    plt.show()

def scatterplots(df,x,y):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x , y=y)

    # Configurar título e rótulos
    plt.title('')
    plt.xlabel(x)
    plt.ylabel(y)

    plt.grid(True)
    plt.show()
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Ler os dados do arquivo Excel
tabela = pd.read_excel("planilha.xlsx")
# Exibir a tabela
display(tabela)



# In[3]:


import pandas as pd
import plotly.express as px
from IPython.display import display

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Loop para criar gráficos de pizza para cada linha
for i, row in df.iterrows():
    semestre = row['Semestre']
    
    # Calcular valores restantes com base na totalidade de ingressantes
    total_ingressantes = row['Ingressantes']
    valores_restantes = row[['Integralizações', 'Cancelamentos', 'Ativos']].tolist()
    
    fig = px.pie(
        values=valores_restantes,
        names=['Integralizações', 'Cancelamentos', 'Ativos'],
        title=f'Semestre {semestre}',
        width=400,  # Largura da figura
        height=400  # Altura da figura
    )
    fig.update_traces(marker=dict(colors=px.colors.qualitative.Set3))  # Definir cores diferentes
    display(fig)


# In[6]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Agrupar os dados da coluna "Ingressantes" por semestre
agregado = df.groupby('Semestre')['Ingressantes'].sum().reset_index()

# Criar o gráfico de barras
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=agregado['Semestre'],
        y=agregado['Ingressantes'],
        text=agregado['Ingressantes'],
        textposition='outside',  # Posição do texto (fora da barra)
        marker_color='blue',  # Cor das barras
    )
)

fig.update_layout(
    title='Ingressantes por Semestre',
    xaxis_title='Semestre',
    yaxis_title='Ingressantes',
    showlegend=False,  # Ocultar a legenda
)

# Exibir o gráfico
fig.show()


# In[7]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Agrupar os dados da coluna "Integralizações" por semestre
agregado = df.groupby('Semestre')['Integralizações'].sum().reset_index()

# Criar o gráfico de barras
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=agregado['Semestre'],
        y=agregado['Integralizações'],
        text=agregado['Integralizações'],
        textposition='outside',  # Posição do texto (fora da barra)
        marker_color='green',  # Cor das barras
    )
)

fig.update_layout(
    title='Integralizações por Semestre',
    xaxis_title='Semestre',
    yaxis_title='Integralizações',
    showlegend=False  # Ocultar a legenda
)

# Exibir o gráfico
fig.show()


# In[16]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Agrupar os dados da coluna "Trancamentos" por semestre
agregado = df.groupby('Semestre')['Trancamentos'].sum().reset_index()

# Criar o gráfico de barras
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=agregado['Semestre'],
        y=agregado['Trancamentos'],
        text=agregado['Trancamentos'],
        textposition='outside',  # Posição do texto (fora da barra)
        marker_color='blue',  # Cor das barras
    )
)

fig.update_layout(
    title='Trancamentos por Semestre',
    xaxis_title='Semestre',
    yaxis_title='Trancamentos',
)

# Exibir o gráfico
fig.show()


# In[13]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Agrupar os dados da coluna "Cancelamentos" por semestre
agregado = df.groupby('Semestre')['Cancelamentos'].sum().reset_index()

# Criar o gráfico de barras
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=agregado['Semestre'],
        y=agregado['Cancelamentos'],
        text=agregado['Cancelamentos'],
        textposition='outside',  # Posição do texto (fora da barra)
        marker_color='red',  # Cor das barras
    )
)

fig.update_layout(
    title='Cancelamentos por Semestre',
    xaxis_title='Semestre',
    yaxis_title='Cancelamentos',
)

# Exibir o gráfico
fig.show()


# In[10]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Agrupar os dados da coluna "Ativos" por semestre
agregado = df.groupby('Semestre')['Ativos'].sum().reset_index()

# Criar o gráfico de barras
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=agregado['Semestre'],
        y=agregado['Ativos'],
        text=agregado['Ativos'],
        textposition='outside',  # Posição do texto (fora da barra)
        marker_color='green',  # Cor das barras
    )
)

fig.update_layout(
    title='Estudantes Ativos por Semestre',
    xaxis_title='Semestre',
    yaxis_title='Estudantes Ativos',
)

# Exibir o gráfico
fig.show()


# In[11]:


import pandas as pd
import plotly.graph_objs as go

# Ler os dados do arquivo Excel
df = pd.read_excel('planilha.xlsx')

# Filtrar os dados até o semestre de 2020.2
df = df[df['Semestre'].astype(str).apply(lambda x: int(x.split('.')[0]) <= 2020 and int(x.split('.')[1]) <= 2)]

# Converter a coluna "Semestre" para o tipo de dados string
df['Semestre'] = df['Semestre'].astype(str)

# Calcular a taxa de sucesso (Integralizações / Ingressantes) e multiplicar por 100 para obter a porcentagem
df['Taxa de Sucesso'] = (df['Integralizações'] / df['Ingressantes']) * 100

# Extrair o ano dos semestres
df['Ano'] = df['Semestre'].apply(lambda x: int(x.split('.')[0]))

# Calcular a média geral da taxa de sucesso por ano
media_geral_por_ano = df.groupby('Ano')['Taxa de Sucesso'].mean().mean()

# Agrupar a taxa de sucesso por ano
taxa_sucesso_por_ano = df.groupby('Ano')['Taxa de Sucesso'].mean().reset_index()

# Calcular a média móvel para as taxas de sucesso
taxa_sucesso_por_ano['Media'] = taxa_sucesso_por_ano['Taxa de Sucesso'].rolling(window=2, min_periods=1).mean()

# Taxa de sucesso da UFRN
taxa_ufrn = [49.19, 59.94, 51.15, 65.57, 58.29, 51.68, 52.77, 50.28]
anos_ufrn = list(range(2013, 2021))

# Média móvel da taxa de sucesso da UFRN
media_ufrn = pd.Series(taxa_ufrn).rolling(window=2, min_periods=1).mean().tolist()

# Criar o gráfico de linhas com as marcações (sem texto) e as linhas médias
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=taxa_sucesso_por_ano['Ano'],
        y=taxa_sucesso_por_ano['Taxa de Sucesso'],
        mode='lines+markers',
        marker=dict(size=10),
        textposition='top center',
        name='Taxa de Sucesso Eng. Biomédica'
    )
)

fig.add_trace(
    go.Scatter(
        x=taxa_sucesso_por_ano['Ano'],
        y=taxa_sucesso_por_ano['Media'],
        mode='lines',
        line=dict(color='red', width=2),
        name='Média Eng. Biomédica'
    )
)

fig.add_trace(
    go.Scatter(
        x=anos_ufrn,
        y=media_ufrn,
        mode='lines',
        line=dict(color='black', width=2),
        name='Média UFRN'
    )
)

# Adicionar rótulo de texto para a média geral na reta
fig.add_annotation(
    x=taxa_sucesso_por_ano['Ano'].iloc[-1],
    y=media_geral_por_ano,
    text=f'Média Geral: {media_geral_por_ano:.2f}%',
    showarrow=True,
    arrowhead=4,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor='red',
    ax=0,
    ay=-40
)

fig.update_layout(
    title='Taxa de Sucesso por Ano',
    xaxis_title='Ano',
    yaxis_title='Taxa de Sucesso Média (%)'
)

# Exibir o gráfico
fig.show()


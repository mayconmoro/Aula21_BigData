# Novo Projeto
# Apresentar uma análise mais detalhada sobre os casos de estelionato registrados no estado do Rio de Janeiro
# Identificar quais meses e anos (coluna: mês_ano) apresentam as menores e maiores quantidades de estelionatos, comparando esses períodos com o total geral de registros
# Apresentar como os casos estão distribuidos ao longo do tempo, verificando se existe algum padrão nas ocorrências, bem como identificar os períodos com menores e maiores índices
#além de expor meses/anos, que apresentem quantidades muito acima do comportamento dos demais períodos analisados.

# Ambiente virtual

# bibliotecas necessárias
import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Limpeza do terminal
os.system('cls')

# Adquirindo os dados para análise
try:
    print('\nAdquirindo os dados... ')

    # definição da variavel para os dados da URL: https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
    endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_seguranca_publica = pd.read_csv(endereco_dados, sep= ';', encoding= 'iso-8859-1')
    
    # Visualização dos dados obtidos
    #print(df_seguranca_publica)

except Exception as e:
    print(f'Erro ao adquirir os dados: {e}')

try:
    print('\nDelimitando os dados adquiridos... ')

    df_estelionato = df_seguranca_publica[['mes_ano', 'estelionato']]

    # Visualização dos dados delimitados
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao delimitar os dados: {e}')

try:
    print('\nAgrupando e totalizandos os dados... ')

    df_estelionato = df_estelionato.groupby('mes_ano', as_index=False)['estelionato'].sum()

    # Visualizando o agrupamento e total
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao agrupar e totalizar os dados: {e}')

try:
    print('\nOrganizando as informações... ')

    df_estelionato = df_estelionato.sort_values(by='estelionato', ascending=False)

    # Visualizando a organização
    #print(df_estelionato)

except Exception as e:
    print(f'Erro ao organizar as informações: {e}')

try:
    print('\nCalculando as quantidades de estelionato... ')

    # Utilizando o Numpy
    array_estelionato = np.array(df_estelionato['estelionato'])
    
    # Visualização do array
    #print(array_estelionato)

    # Verificando os meses que houveram mais, menos e o total de estelionatos
    total_estelionato = sum(array_estelionato)
    menor_mes_estelionato = min(array_estelionato)
    maior_mes_estelionato = max(array_estelionato)
    df_menor_mes_estelionato = df_estelionato[df_estelionato['estelionato'] == menor_mes_estelionato]
    df_maior_mes_estelionato = df_estelionato[df_estelionato['estelionato'] == maior_mes_estelionato]

    # Visualização dos calculos
    # print(total_estelionato)
    # print(menor_mes_estelionato)
    # print(maior_mes_estelionato)
    # print(df_menor_mes_estelionato) 
    # print(df_maior_mes_estelionato)    

except Exception as e:
    print(f'Erro ao calcular as métricas: {e}')

try:
    print('\nCalculando as Medidas de tendência Central... ')

    media_estelionato = np.mean(array_estelionato)
    mediana_estelionato = np.median(array_estelionato)
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato * 100)

    # Visualização dos calculos
    # print(media_estelionato)
    # print(mediana_estelionato)
    # print(distancia_media_mediana)

except Exception as e:
    print(f'Erro ao calcular as medidas: {e}')

try:
    print('\nCalculando as distribuições... ')

    quartil_inferior = np.quantile(array_estelionato, 0.25)
    quartil_superior = np.quantile(array_estelionato, 0.75)
    IQR = quartil_superior - quartil_inferior
    limite_inferior = quartil_inferior - (1.5 * IQR)
    limite_superior = quartil_superior + (1.5 * IQR) 
    amplitude = quartil_superior - quartil_inferior
    
except Exception as e:
    print(f'Erro ao calcular a distribuição: {e}')

try:
    print('\nEncontrando os períodos com Maiores e Menores índices de estelionato...')

    df_menor_qtd_estelionato = df_estelionato[df_estelionato['estelionato'] < quartil_inferior]
    df_maior_qtd_estelionato = df_estelionato[df_estelionato['estelionato'] > quartil_superior]
    df_extremo_inferior = df_estelionato[df_estelionato['estelionato'] < limite_inferior]
    if len(df_extremo_inferior) == 0:
        print('Não existem valores extremos inferiores')

    else:
        print(df_extremo_inferior.sort_values(by= 'estelionato', ascending=True))
        
    df_extremo_superior = df_estelionato[df_estelionato['estelionato'] > limite_superior]
    df_extremo_superior = df_extremo_superior(index=False)
    
    # Visualizaçãod dos periodos
    # print(df_menor_qtd_estelionato)
    # print(df_maior_qtd_estelionato)
    # print(df_extremo_inferior)
    # print(df_extremo_superior)
    
except Exception as e:
    print(f'Erro ao encontrar as informações: {e}')

# Resumo das informações solicitadas
print(200*"=")
print('Relatório de Casos de Estelionato no Estado do Rio de Janeiro - 2003 a 2026(atual):')
print(200*"=")

print(f'Foram observados um total de {total_estelionato} casos durante o período analisado')
print(f'O Período com menor índice de estelionatos teve, {menor_mes_estelionato} casos e refere-se ao mês {df_menor_mes_estelionato['mes_ano'].values[0]}')
print(f'O Período com maior índice de estelionatos teve, {maior_mes_estelionato} casos e refere-se ao mês {df_maior_mes_estelionato['mes_ano'].values[0]}')
print(200*"=")
print(f'Os registros de estelionato apresentam elevada variabilidade ao longo do período analisado.')
print(f'A diferença entre média {media_estelionato:.2f} e mediana {mediana_estelionato:.2f} sugere que determinados meses concentraram quantidades significativamente superiores de ocorrências, influenciando a média geral.')
print(200*"=")
print('\nMeses com valores anormais: ')
print(f'\nForam identificados períodos com comportamento atípico (outliers), indicando meses que merecem investigação específica para compreender fatores que contribuíram para o aumento dos registros.')
print(200 * '=')
print(f'Observam-se oscilações relevantes entre os meses, indicando que a ocorrência de estelionatos sofre influência de fatores temporais que merecem investigação adicional.')
print(df_extremo_superior)

try:
    print('\nVisualização dos dados...')
    #plt.figure(figsize=(18,8))
    plt.subplots(2, 2, figsize=(18, 10))

    # POSIÇÃO 1 => BOXPLOT
    plt.subplot(2, 2, 1)
    plt.boxplot(array_estelionato, vert=False, showmeans=True) #showfliers=False = remove os outliers, não é uma boa prática ou se utilizar, demonstrar em um grafico auxiliar
    plt.title('Boxplot da Distribuição')
    
    # POSIÇÃO 2 => MEDIDAS
    plt.subplot(2, 2, 2)
    plt.text(0.1, 0.9, f'Média: {media_estelionato:.2f}')    
    plt.text(0.1, 0.8, f'Distância: {distancia_media_mediana:.2f}')        
    plt.text(0.1, 0.7, f'Limite Inferior: {limite_inferior:.2f}')
    plt.text(0.1, 0.6, f'Menor mês: {menor_mes_estelionato:.2f}')  
    plt.text(0.1, 0.5, f'Quartil Inferior: {quartil_inferior:.2f}')
    plt.text(0.1, 0.4, f'Mediana: {mediana_estelionato:.2f}')
    plt.text(0.1, 0.3, f'Quartil Superior: {quartil_superior:.2f}')
    plt.text(0.1, 0.2, f'Limite Superior: {limite_superior:.2f}')
    plt.text(0.1, 0.1, f'Maior mês: {maior_mes_estelionato:.2f}')
    plt.text(0.1, 0.0, f'Amplitude: {amplitude:.2f}')


   # POSIÇÃO 3 - DEMONSTRAÇÃO DOS OUTLIERS SUPERIORES
    plt.subplot(2, 2, 3)
    df_extremo_superior = (        
        df_extremo_superior
        .head(10)
        .sort_values(by= 'estelionato', ascending=False)
        )    

    plt.bar(
        df_extremo_superior['mes_ano'], #.str.slice(0, 10),  str slice limita os caracteres
        df_extremo_superior['estelionato']
    )

    deslocamento = max(df_extremo_superior['estelionato']) * 0.01

     # Rotulo dos dados:
    for i, valor in enumerate(df_extremo_superior['estelionato']):
        plt.text(        
        i, # posição X
        valor + deslocamento, # psição Y 
        f'{valor:,}',
        ha= 'center'
        )

    plt.xticks(rotation=45, ha='right') # Rotaciona o texto eixo x
    plt.title('Meses e Anos com Outliers Superiores')


    # POSIÇÃO 4 - DEMONSTRAÇÃO DOS OUTLIERS INFERIORES OU DADOS MENORES
    plt.subplot(2, 2, 4)
    
    if len(df_extremo_inferior) > 0:
        df_extremo_inferior = (
            df_extremo_inferior       
            .sort_values(by= 'estelionato', ascending=True)
        )

        plt.barh(
            df_extremo_inferior['mes_ano'],
            df_extremo_inferior['estelionato']
        )     

        plt.title ('Meses e Anos c/Outliers Inferiores')

    else:
        df_menor_qtd_estelionato = (
            df_menor_qtd_estelionato
            .head(10)
            .sort_values(by='estelionato', ascending=False)    
        )   

        plt.barh(
            df_menor_qtd_estelionato['mes_ano'],
            df_menor_qtd_estelionato['estelionato']
        )

        deslocamento = max(df_menor_qtd_estelionato['estelionato']) * 0.03

           # Rotulo dos dados:
        for i, valor in enumerate(df_menor_qtd_estelionato['estelionato']):
            plt.text(
            valor + deslocamento, # posição X 
            i, # posição Y
            f'{valor:,}',
            ha= 'center'
            )

            plt.title('Meses e Anos com Menor Índice de Estelionato')

    plt.show()

except Exception as e:
    print(f'Erro ao plotar o gráfico: {e}')
    exit()

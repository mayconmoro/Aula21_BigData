# Novo Projeto
# Entender a necessidade do solicitante. (cidade e caso de roubos de veículos desde 2003 até 2026(atual))
# Onde consigo os dados para o trabalho?
    # fonte de informação e do arquivo estudado: 
    # https://www.ispdados.rj.gov.br/estatistica.html
    # https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv
# Criar o ambiente virtual e ativar
# Instalar as bibliotecas necessárias

#--------------------------------------------------------------------------------------------------------------#
# Bibliotecas
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# Limpeza do terminal
os.system('cls')

# Obtenção dos dados dos estudos e Preparação dos dados
try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep= ';', encoding= 'iso-8859-1')
    
    # conferencia dos dados obtidos
    #print(df_ocorrencias.head())

    # delimitando as variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    
    # Checando o dataframe delimitado
    #print(df_roubo_veiculo.head(50))

    # Agrupando e Totalizando os roubos por municipios
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum( ) # as_index=False para retornar com os números de indices

    # Organizando por ordem decrescente
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)

    # Checando o agrupamento por cidade
    #print(df_roubo_veiculo.head(25))

except Exception as e:
    print(f'Erro ao obter dados {e}')

# Obtendo as medidas
try:
    print('Calculando as medidas... ')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo']) # array é uma estrutura do numpy com ganho computacional

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100) # abs é para obtermos o valor absoluto

    # Verificando as medidas estatísticas
    print('\nMedidas de Tendência Central ')
    print(50*"=")
    print(f'Média: {media_roubo_veiculo:.2f}')
    print(f'Mediana: {mediana_roubo_veiculo:.2f}')
    print(f'Distância: {distancia:.2f}%')
    # quando for de 0 a 10% = tendencia a serem dados simetricos (dados menos dispersos)  - dados considerados homogeneos 
    # quando for de 10 a 25% = tendencia a ter uma assimetria moderada (a distribuição pode estar sendo influenciada por valores extremos gerando dispersão) 
    # quando for acima de 25% = tendencia de assimetria forte - dados heterogeneos
    
except Exception as e:
    print(f'Erro ao processar as medidas: {e}')

#Obtendo a distribuição
try:
    array_roubo_veiculo    
    quartil_inferior = np.quantile(array_roubo_veiculo, 0.25)    
    quartil_superior = np.quantile(array_roubo_veiculo, 0.75)

    # Verificando os quartis
    print('\nQuartis ')
    print(50*"=")
    print(f'Quartil inferior: {quartil_inferior:.2f}') # representa os 25% menores com até 47.25 roubos
    print(f'Mediana: {mediana_roubo_veiculo:.2f}')
    print(f'Quartil superior: {quartil_superior:.2f}') # representando 75% das cidades do estado tiveram menos que 1016.75

    # Encontrando os municípios com menos roubos
    df_roubo_veiculo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < quartil_inferior]

    # Encontrando os municípios com menos roubos
    df_roubo_veiculo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > quartil_superior] 

    # print('\nMunicípios com menos casos de roubos: ')
    # print(50 * '=')
    # print(df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True))

    # print('\nMunicípios com maiores casos de roubos: ')
    # print(50 * '=')
    # print(df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False)) # ja esta ordenado na sintaxe acima na linha 40

except Exception as e:
    print(f'Erro ao obter a distribuição: {e}')

    # Obtendo as Medidas de Posição 
try:
    # Amplitude total => amplitude = (máximo - mínimo) 
    # Resultado: mais próximo do mínimo, baixa dispersão (dados mais homogeneos)
    # Resultado: Zero, quer dizer que todos os dados são iguais
    # Resultado: mais próximo do máximo, alta variabilidade ou dispersão

    maximo = np.max(array_roubo_veiculo)
    minimo = np.min(array_roubo_veiculo)
    amplitude = maximo - minimo    

    print('\nMedidas de Posição ')
        
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude}') 

except Exception as e:
    print(f'Erro ao calcular medidas de posição: {e}')

    # Calculando os outliers, medidas de dispersão
try:
    # IQR (INTERVALO INTERQUARTIL) => é a amplitude dos 50% dos dados mais centrais
    # IQR = q4 - q1
    # Ele ignora os valores extremos. Max e Min estão fora do IQR
    # Não sofre interferência dos valores extremos
    # Quanto mais próximo do Q1, mais homogeneos são os dados 
    # Quanto mais próximo do Q3, mais heterogeneos são os dados 

    iqr = quartil_superior - quartil_inferior

    # Limite Inferior
    # É uma medida que vai identificar os outliers, os valores abaixo do que o limite inferior
    limite_inferior = quartil_inferior - (1.5 * iqr)

    # Limite Superior
    # É uma medida que vai identificar os outliers, os valores maiores do que o limite superior
    limite_superior = quartil_superior + (1.5 * iqr)

    print('\nMedidas de Dispersão ')
    print(50*"=")
    print(f'IQR: {iqr}')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Limite Superior: {limite_superior}') 

except Exception as e:
    print(f'Erro ao calcular as medidas de dispersão: {e}')

    #Calculando os Outliers
try:
    # Outliers Superiores
    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]    

    # Outliers Inferiores
    df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]

    # Exibindo os Outliers
    print('\nMunicípios com Outliers Inferiores: ')
    print(50 * '=')
    if len(df_roubo_veiculo_outliers_inferiores) == 0:
        print('Não existem Outliers inferiores')
    else:
        print(df_roubo_veiculo_outliers_inferiores.sort_values(by= 'roubo_veiculo', ascending=True))

    print('\nMunicípios com Outliers Superiores: ')
    print(50 * '=')
    print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))
    
except Exception as e:
    print(f'Erro ao calcular os Outliers: {e}')


# try:
#     # Visualizando os dados
#     plt.figure(figsize=(16, 8)) # configuração da janela do gráfico
#     df_roubo_veiculo_maiores = df_roubo_veiculo_maiores.sort_values(by='roubo_veiculo', ascending=False).head(10)
#     # Plotando o Gráfico Colunas
#     plt.bar(df_roubo_veiculo_maiores['munic'], df_roubo_veiculo_maiores['roubo_veiculo']) # acionar o gráfico
#     plt.title('Municípios com Maiores Roubos de Veículos') # Titulo do gráfico
#     plt.show() # para mostrar o gráfico
# except Exception as e:
#     print(f'Erro ao plotar o gráfico: {e}')

# Visualizando o Boxplot
try:
    print('\nVisualizando os dados...')
    plt.subplots(2, 2, figsize=(18, 10))

    # POSIÇÃO 1: BOXPLOT
    plt.subplot(2, 2, 1) # 2 linhas e 2 colunas para a área 1
    plt.boxplot(array_roubo_veiculo, vert=False, showmeans=True)
    plt.title('Boxplot dos Índices de Roubo de Veículo')

    # POSIÇÃO 2: MEDIDAS
    plt.subplot(2, 2, 2)
    plt.text(0.1, 0.9, f'Média: {media_roubo_veiculo:.2f}')  
    plt.text(0.1, 0.8, f'Distância: {distancia:.2f}%')  
    plt.text(0.1, 0.7, f'Limite Inferior: {limite_inferior:.2f}')
    plt.text(0.1, 0.6, f'Mínimo: {minimo:.2f}')
    plt.text(0.1, 0.5, f'Quartil Inferior: {quartil_inferior:.2f}')    
    plt.text(0.1, 0.4, f'Mediana: {mediana_roubo_veiculo:.2f}')
    plt.text(0.1, 0.3, f'Quartil Superior: {quartil_superior:.2f}')
    plt.text(0.1, 0.2, f'Limite Superior: {limite_superior:.2f}')    
    plt.text(0.1, 0.1, f'Máximo: {maximo:.2f}')    
    plt.text(0.1, 0.0, f'Amplitude: {amplitude:.2f}')

    plt.axis('off')
    plt.title('Resumo Estatístico')

    # POSIÇÃO 3 - DEMONSTRAÇÃO DOS OUTLIERS SUPERIORES
    plt.subplot(2, 2, 3)
    df_roubo_veiculo_outliers_superiores = (        
        df_roubo_veiculo_outliers_superiores
        .head(10)
        .sort_values(by= 'roubo_veiculo', ascending=False)
        )    

    plt.bar(
        df_roubo_veiculo_outliers_superiores['munic'], #.str.slice(0, 10),  str slice limita os caracteres
        df_roubo_veiculo_outliers_superiores['roubo_veiculo']
    )

    deslocamento = max(df_roubo_veiculo_outliers_superiores['roubo_veiculo']) * 0.01

     # Rotulo dos dados:
    for i, valor in enumerate(df_roubo_veiculo_outliers_superiores['roubo_veiculo']):
        plt.text(        
        i, # posição X
        valor + deslocamento, # psição Y 
        f'{valor:,}',
        ha= 'center'
        )

    plt.xticks(rotation=45, ha='right') # Rotaciona o texto eixo x
    plt.title('Municípios com Outliers Superiores')


    # POSIÇÃO 4 - DEMONSTRAÇÃO DOS OUTLIERS INFERIORES OU DADOS MENORES
    plt.subplot(2, 2, 4)
    
    if len(df_roubo_veiculo_outliers_inferiores) > 0:
        df_roubo_veiculo_outliers_inferiores = (
            df_roubo_veiculo_outliers_inferiores            
            .sort_values(by= 'roubo_veiculo', ascending=True)
        )

        plt.barh(
            df_roubo_veiculo_outliers_inferiores['munic'],
            df_roubo_veiculo_outliers_inferiores['roubo_veiculo']
        )     

        plt.title ('Municipios c/Outliers Inferiores')

    else:
        df_roubo_veiculo_menores = (
            df_roubo_veiculo_menores
            .head(10)
            .sort_values(by='roubo_veiculo', ascending=False)    
        )   

        plt.barh(
            df_roubo_veiculo_menores['munic'],
            df_roubo_veiculo_menores['roubo_veiculo']
        )

        deslocamento = max(df_roubo_veiculo_menores['roubo_veiculo']) * 0.03

           # Rotulo dos dados:
        for i, valor in enumerate(df_roubo_veiculo_menores['roubo_veiculo']):
            plt.text(
                valor + deslocamento, # psição X 
                i, # posição Y
                f'{valor:,}',
                ha= 'center'
            )

            plt.title('Municipios com Menores Índices de Roubo')

    plt.show()

except Exception as e:
    print(f'Erro ao plotar o gráfico: {e}')
    
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('life expectancy.csv')
df_filtro=df[['Country Name','Life Expectancy World Bank','Health Expenditure %']].sort_values(by='Life Expectancy World Bank',ascending=False).dropna()

df_life_expec=df_filtro.groupby('Country Name')[['Life Expectancy World Bank']].mean().sort_values(by='Life Expectancy World Bank',ascending=False)
plt.plot(df_life_expec.head(5))
plt.plot(df_life_expec.head(5),'red')
plt.xlabel('PAIS')
plt.ylabel('exp')

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #ESQUERDA #INFERIOR, LARGURA ALTURA
axes2 = fig.add_axes([0.39,0.5,0.47,0.3]) #ESQUERDA #INFERIOR, LARGURA ALTURA

axes.plot(df_life_expec.head(5),'blue')
axes.set_title('Gráfico')
axes.set_xlabel('Pais')
axes.set_ylabel('exp')

axes2.plot(df_life_expec.tail(3),'red')

#SUPLOTS
fig,ax=plt.subplots()
ax.plot(df_life_expec.head(5),'b--')
ax.set_title('Indíce de exp.vida por pais')

#PLOTANDO OS DOIS MAIORES E 2 MENORES
fig,ax=plt.subplots(nrows=1,ncols=2, figsize=(30,10))
for axis in ax:
    if axis == ax[0]:  
        axis.plot(df_life_expec.head(10),'blue')
        axis.set_title('Melhores paises')
    else:
        axis.plot(df_life_expec.tail(10),'r--')
        axis.set_title('Piores Paises')
    plt.tight_layout()
    

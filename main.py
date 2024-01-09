import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('pokemon.csv')

df_legendary=df[df['Legendary']==True].sort_values(ascending=False,by='Attack')

y=df_legendary['Attack']
x=df_legendary['Name']

df_legendary_def=df[df['Legendary']==True].sort_values(ascending=False,by='Defense')
y_def=df_legendary_def['Defense']
x_def=df_legendary_def['Name']

plt.plot(x,y)
plt.plot(color='red')
plt.xlabel('Ataque')
plt.ylabel('Nome')
plt.title(f'Top {len(df_legendary)} Pokemons lendários com mais ataque')

#SUBPLOT

plt.subplot(1,2,1)
plt.plot(x,y, 'r--')
plt.subplot(2,2,2)
plt.plot(x,y, 'g--')



fig= plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8]) # esquerda, #inferior, largura, altura
axes.plot(x,y,'blue')

axes2=fig.add_axes([0.5,0.65,0.3,0.2])
axes2.plot(x.tail(3),y.tail(3),'red')
axes2.set_title('- Ataque')

axes3=fig.add_axes([0.5,0.30,0.3,0.2])
axes3.plot(x_def,y_def,'green')
axes3.set_title('Defesa')


#SUBPLOTS

#PLOTANDO OS 3 MAIORES ATAQUES/DEF E OS 3 PIORES TAMBÉM
fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(15,5))

ax[0][0].plot(x.head(3),y.head(3),'r-*')
ax[0][0].set_title('Maiores ataques')
ax[0][1].plot(x_def.head(3),y_def.head(3),'blue')
ax[0][1].set_title('Maiores defesas')

ax[1][0].plot(x.tail(3),y.tail(3),'r-*')
ax[1][0].set_title('Menores ataques')
ax[1][1].plot(x_def.tail(3),y_def.tail(3),'blue')
ax[1][1].set_title('Menores defesas')

[axis.tick_params(axis='x',labelsize=14) for axis in ax.flat]

plt.tight_layout()



    

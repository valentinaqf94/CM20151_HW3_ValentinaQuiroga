
# coding: utf-8

## Punto 3c 

# In[12]:

get_ipython().magic(u'pylab inline')


# In[54]:

x = input() #esto lee el archivo, lo convierte el filas que leer
reader = open('Sainte-Beuve.txt','r')
i = 0
conta = 0
for fila in reader:
    if (i <= int(x)):
       b = cuenta_vocales(fila)
       conta += b #guarda el conteo de las vocales que ya hay
       i+=1
    else:
       break     
print conta
reader.close()        #cierro el archivo


# In[53]:

def cuenta_vocales(a): #funcion que me cuenta las vocales
    vocales = ['\xa1', '\xa9', '\xad', '\xb3', '\xba', 'a', 'e', 'i', 'o', 'u','\x81', '\x89', '\x8d', '\x93', '\x9a', 'A', 'E', 'I', 'O', 'U'] #da todas las posibles combinaciones de las vocales
    numero_vocales = 0
    for j in range(len(a)):
        numero_vocales += vocales.count(a[j])
      
    return numero_vocales        


# In[41]:




# In[ ]:




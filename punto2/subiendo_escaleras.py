
# coding: utf-8

## Subiendo escaleras

# In[34]:

#get_ipython().magic(u'pylab inline')

import numpy as np
import matplotlib as mtp

# In[88]:

def subir_escalera(): #esta es la funcion que representa las formas de subir una escalera de n escalones
    a = 1
    b = 1
    while True:         
        yield a           #yield es un return para generadores
        a, b = b, a + b  


# In[89]:

def cal_formas(n):
    for index, subiendo in enumerate(subir_escalera()): #funcion que, tras darle el numero de escalones que se quiere subir, le da las formas de hacerlo
         #print('{i:3}: {f:3}'.format(i=index, f=subiendo))
         if index == n:
             break
    return subiendo


### Para 15 escalones existen 987 formas de subir

# In[90]:

print "Para 15 escalones" + str( cal_formas(15))


### Para 13 escalones existen 377 formas de subir

# In[91]:

print "para 13 escalones" + str( cal_formas(13))


### Vamos a ver la escalera con modulo 

# In[91]:




# In[92]:

A=[4,4,5,5,1] #ejemplo guia
B=[3,2,4,3,1]
L=1000
E=[]
def escalera(A,B):
    for d in (range(len(A))): #itero en el tamanio de A, me retorna la lista compuesta del producto de ambas cosas
        DATO=cal_formas(A[d]%(((B[d]))*2))
        E.append(DATO)
    return E
            
print escalera(A,B)
        


    
    


# In[93]:

A=[1,2,3,4,5] #ejemplo aparte
B=[1,2,3,4,5]
L=1000
E=[]
def escalera(A,B):
    for d in (range(len(A))): #itero en el tamanio de A, me retorna la lista compuesta del producto de ambas cosas
        DATO=cal_formas(A[d]%(((B[d]))*2))
        E.append(DATO)
    return E
            
print escalera(A,B)
        


# In[93]:




# In[93]:




# In[ ]:




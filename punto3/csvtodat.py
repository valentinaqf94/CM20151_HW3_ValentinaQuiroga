
# coding: utf-8

## Punto 3b, importar archivos y editarlos

# In[108]:
import numpy as np
import matplotlib as mlp
import csv
#get_ipython().magic(u'pylab inlii

# In[109]:


reader = csv.reader(open('Notas.csv','rU')) #el archivo se abre y se convierte en un arreglo que despues pasa a ser un .dat
data = []
n_lines = 0
a = open('Notas.dat', 'w')
for line in reader:
    data.append(line)
    n_lines += 1
    a.write(line[0] + '+' + line[1] + '+' + line[2] + '+' + line[3] + '+' + line[4] + '+' + line[5] + '+' +
    line[6] + '+' + line[7] +  '\n') #necestio una forma de hacer que imprima todo sistematicamente
     



# In[110]:

a.close() #terminal para mostrar que hay en el areglo
#get_ipython().system(u'cat Notas.dat ')



# In[111]:

#get_ipython().system(u'ls #')


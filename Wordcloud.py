#!/usr/bin/env python
# coding: utf-8

# # WordCloud nico.-
# Este programa permite obtener una imagen de tipo WordCloud a partir de un archivo de texto.
# Hasta el momento es necesario tener el archivo en formato. txt

# In[1]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

'''
esta funcion genera una lista a partir del archivo txt que se carga
'''

def get_words(file):
    word_list = []
    for linea in file:
        words = linea.replace("\n", " ")
        word_list.append(words)
    
    return create_str(word_list)    

'''
esta funcion genera una string a partir de los elemntos de la lista generada con la funcion anterior
'''

def create_str(lst):
    raw_text = ' '
    for i in lst:
        raw_text = raw_text + i
        
    return raw_text

dic = {'\n':' ',
       '.':' ',
       ',':' ',
       ':':' ',
      '?':' ',
      '¿':' ',
       ")":' ',
       "(":' ',
       '-':''
      }

def replace_all(words, dic):
    for key, value in dic.items():
        words = words.replace(key, value)
    return words

############################################################################################################################

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>x<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n',
      '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>              WordCloud                        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n',
      '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>x<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

# estas lineas de codigo permiten abrir archivos comunes y archivos codificados en utf-8
# ademas usando combinaciones de try/except logramos que el programa no se rompa al abrir uno u otro tipo de archivo
input_file = 'Capítulo 3.txt'
with open(input_file, encoding='utf-8') as f:
    try:
        file = f.readlines()
        f.close()
        
    except UnicodeDecodeError:
        try:
            with open(input_file) as f:
                file = f.readlines()
                f.close()
                
        except Exception as e:
            print(e)
            
# words = get_words(file)

words = replace_all(get_words(file), dic)

    

# algunas palabras especiales no las podemos filtar con la funcion que definimos mas arriba por lo tanto incluimos una
# lista de palabras prohibidas. Esta lista puede ser modificada de acuerdo a las necesidades de cada caso.
stopwords = ['para', 'otra', 'este', 'esta', 'pero', 'como', 'través','Figura']



# Create the wordcloud object

wordcloud = WordCloud(font_path ='comic',
                      width=800,
                      height=400,
                      margin=0,
                      background_color='#79bed1',
                      colormap='pink_r',
                      normalize_plurals=True,
                      max_words=300,
                      stopwords=stopwords,
                      min_word_length=4
                     ).generate(words)
# color_map = ['autumn', 'Spectral', 'pink_r', 'twilight_shifted', 'Wistia', 'Purples_r','binary_r', 'bone',]  estos son los 
# estilos mas lindos de los que probe. 
# Display the generated image:
plt.figure( figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear') # esta linea no se para que sirve...
plt.axis("off")
plt.margins(x=1, y=1)
plt.title('Cap 3.-', fontsize=30, pad=10)
plt.show()


# ## Save file

# In[48]:


file_name = 'Cap3.png'
wordcloud.to_file(file_name)
print('--- File has been saved ---')


# ---
color_map = ['autumn', 'Spectral', 'pink_r', 'twilight_shifted', 'Wistia', 'Purples_r','binary_r', 'bone',] # estos son los 
# estilos mas lindos de los que probe.

La lista con todos los estilos es la siguiente:
'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'
# ---

# ---

# ## Parte #2.
# # Obtener una lista con las palabras mas usadas

# In[44]:


import pandas as pd
words_split = words.split(' ')
data_1 = list(filter(lambda x: (len(x) > 3),words_split))


# stopwords = ['para', 'otra', 'este', 'esta', 'pero', 'como']
data =[word for word in data_1 if word not in stopwords] # esta linea de codigo nos permite filtrar la lista data_1 con 
# las mismas palabras con que filtramos el WordCloud.


index = range(len(data))
df = pd.DataFrame(data=data, index=index, columns=['words'])
most_frequent_words = df['words'].value_counts().sort_values(ascending=False)
print(f'Palabras mas usadas\n{most_frequent_words.head(10)}')


# In[46]:


most_frequent_words.to_csv('Cap3.csv')
print('Data has been saved!!')


# In[ ]:





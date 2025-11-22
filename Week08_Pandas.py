import pandas as pd
import numpy as np
"""
Mengenal Fungsi Random Sampling pada Pandas Data Frame
d = {'col 1': [1, 2,3,4,5], 'col 2': [10, 20,30,40,50]}
df = pd.DataFrame(d)
print(df)

df.sample(n=4, replace=False, random_state=0) #Mengambil sampel acak sebanyak n baris dari Data Frame
df.sample(n=4, replace=True, random_state=0) #Mengambil sampel acak dengan pengembalian
"""

"""
Mengenal Fungsi Query pada Pandas Data Frame
n_rows = 5
n_cols = 5
Cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1,20,size=(n_rows,n_cols)), columns=Cols)
df.query('A > 10')
rerata = df['A'].mean()

df.query('A > @rerata') #Menggunakan variabel eksternal dalam query
"""
"""
Mengenal Tipe Data Kategorikal pada Pandas Data Frame
d = {'pelanggan': [11,12,13,14],'kepuasan':['baik','cukup','buruk','cukup']}

df = pd.DataFrame(d)

from pandas.api.types import CategoricalDtype

tingkat_kepuasan = CategoricalDtype(categories=['buruk','cukup','baik','sangat baik'], ordered=True)

df['kepuasan'] = df['kepuasan'].astype(tingkat_kepuasan)

df = df.sort_values('kepuasan', ascending=True) #Mengurutkan Data Frame berdasarkan kolom 'kepuasan' sesuai urutan kategori
df = df.sort_values('kepuasan', ascending=False) #Mengurutkan Data Frame berdasarkan kolom 'kepuasan' sesuai urutan

df[df['kepuasan'] >= 'cukup'] #Memfilter baris dengan kepuasan 'cukup' atau lebih tinggi
"""

n_rows = 40 
n_cols = 5
Cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1,20,size=(n_rows,n_cols)), columns=Cols)  
df.head()
df.plot(kind='line')

df[['A','B']].plot(kind='line')  #Membuat plot garis untuk kolom A dan B
df.head()

df.plot(kind='bar')  #Membuat plot batang untuk semua kolom
df[['A','B']].plot(kind='bar')  #Membuat plot batang untuk kolom A dan B
df[['A','B']].head().plot(kind='bar')  #Membuat plot batang untuk kolom A dan B berdasarkan 5 baris pertama
df[['A','B']].head().plot(kind='barh') #Membuat plot batang horizontal untuk kolom A dan B

df.head()
df.plot(kind='area')  #Membuat plot area untuk semua kolom
df[['A','B']].head().plot(kind='area')  #Membuat plot area untuk kolom A dan B

df.head()
df.plot(kind='box')  #Membuat plot box untuk semua kolom
df[['A','B']].plot(kind='box')  #Membuat plot box untuk kolom A dan B

df.head()
df.plot(kind='hist')  #Membuat plot histogram untuk semua kolom
df[['A','B']].plot(kind='hist')  #Membuat plot histogram untuk kolom A dan B

df.head()   
df.plot(kind='kde')  #Membuat plot KDE untuk semua kolom
df[['A','B']].plot(kind='kde')  #Membuat plot KDE untuk kolom A dan B

df.head()
df.plot(x='A', y='B', kind='scatter')  #Membuat plot scatter antara kolom A dan B


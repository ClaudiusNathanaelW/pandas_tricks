import pandas as pd
import numpy as np


#DataFrame Introduction (Includes Prefix, Suffix, Select, Negative (~) operator )
print(pd.__version__)  
print(np.__version__)

n_rows = 10
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), columns=cols)
df_prefix =df.add_prefix('kolom_') #(Add x Sebelum)
print(df_prefix)
df_suffix = df.add_suffix('_field') #(Add x setelah)

df_select = df[(df['A']==1)|(df['A']==3)] #(Select baris jika A = 1 atau 3)
df_select = df[(df['A'].isin([1,3]))] #(Alternatif Select baris jika A = 1 atau 3)
df_select = df[(~df['A'].isin([1,3]))] # ~ adalah operator negatif atau not
print(df, '\n\n')
print(df_select)



"""
#Mengubah tipe data
df={'col1':['1','2','3','text'],'col2':['1','2','3','4']}
tipe = df.dtypes #Cek tipe data
print(df)
print(tipe)

#df_x = df.astype({'col2':'float'}) #Mengubah tipe data satu kolom
df_x = df.apply(pd.to_numeric, errors='coerce') #Mengubah tipe data satu kolom secara paksa

print(df_x,'\n')
print(df_x.dtypes)



n_rows = 5
n_cols = 2
cols = ['bil_bulat', 'bil_pecahan']
df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)
df['bil_pecahan'] = df ['bil_pecahan'].astype('float')
df.index = pd.date_range(start='2025-09-21',periods=n_rows,freq='h')
df = df.reset_index()

df['teks'] = list('ABCDE')

num = df.select_dtypes(include='number')
float = df.select_dtypes(include='float')
int = df.select_dtypes(include='int')
object = df.select_dtypes(include='object')
datetime = df.select_dtypes(include='datetime')
combine = df.select_dtypes(include=['number','object'])


print(num) #Memilih data angka
print(float) #Memilih tipe data float
print(int)  #Memilih tipe data int
print(object)   #Memilih tipe data String atau Object 
print(datetime)   #Memilih tipe data tanggal dan waktu
print(combine)  #Memilihi tipe data yang dikombinasikan 


tipe = df.dtypes
print(df,'\n')
print(tipe)
"""
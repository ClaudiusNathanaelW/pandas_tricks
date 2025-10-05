#Week 03 - Pandas 5/10/2025
#Membagi DF menjadi dua secara acak
#Mulai 15.30 WIB
#Selesai 16.00 WIB
import pandas as pd
import numpy as np


n_rows = 10
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)

"""
Ukurandf = df.shape
print(Ukurandf)

proporsi = 0.7
df1 = df.sample(frac=proporsi) #Mengambil 70% data secara acak
df2 = df.drop(df1.index) #Mengambil sisa data

print(f'df1_shape: {df1.shape}')
print(f'df2_shape: {df2.shape}')

print(df1)
print(df2)
"""

"""
Mengganti nama kolom DataFrame berdasarkan pola

dff = pd.read_csv("D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv")
dff.columns = ['Passenger Id','Pclass', 'Survived', 'full name', 'Sex', 'Age', 'Sib SP', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
df_backup = dff.copy() #Membuat salinan df untuk backup
dff.columns = dff.columns.str.lower().str.replace(' ', '_') #Mengganti nama kolom menjadi huruf kecil dan mengganti spasi dengan underscore
dff.head()
print(dff)
"""

"""
Melakukan seleksi kolom dan baris pada DataFrame menggunakan .loc

dflocate = df.loc[[0,3,4], ['B','E']] #Memilih baris 0,3,dan 4 + kolom B dan E
print(dflocate)
print()

dflocateconditional = df.loc[df['B']>10, ['B','D','E']] #Memilih baris dengan kondisi kolom B > 10 + kolom B, D, dan E
print(dflocateconditional)
print()

#slicing
slicingexample = df.loc[2:5, 'A':'C'] #Memilih baris 2 sampai 5 dan kolom A sampai C 
print(slicingexample)
"""

"""
Membentuk kolom bertipe datetime dari sejumlah kolom lain pada DataFrame
"""
data = {'day': [1, 2, 3, 4, 5],
        'month': [1, 2, 3, 4, 5],
        'year': [2020, 2021, 2022, 2023, 2024]}

df = pd.DataFrame(data)
df['penanggalan'] = pd.to_datetime(df[['day', 'month', 'year']]) #Membuat kolom tanggalan dari kolom day, month, year
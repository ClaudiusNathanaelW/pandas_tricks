#Pandas - Week 4 13/10/2025
#Mulai 15.00 WIB
#Selesai 14.00 WIB
import pandas as pd
import numpy as np

"""
Konversi nilai numerik ke dalam kategori pada Data Frame
Pengelompokan data usia ke dalam kategori menggunakan pd.cut
n_rows = 10
n_cols = 1
cols = ('usia',)
df = pd.DataFrame(np.random.randint(1, 99, size=(n_rows, n_cols)), columns=cols)
df['kelompok usia'] = pd.cut(df['usia'], bins=[0, 12, 19, 35, 60, 99], labels=['Anak-anak', 'Remaja', 'Dewasa', 'Paruh Baya', 'Lansia'])
print(df)
"""

"""
Menggabungkan dua Pandas Data Frame

n_rows = 5
n_cols = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)
df1 = df.copy(deep=True)
df1 = df1.drop(columns=[1, 4])

df2 = df.copy(deep=True)
df2 = df2.drop(columns=[0, 3])

df_inner = pd.merge(df1, df2, how='inner', left_index=True, right_index=True) #Menggabungkan df1 dan df2 dengan metode inner join
df_outer = pd.merge(df1, df2, how='outer', left_index=True, right_index=True) #Menggabungkan df1 dan df2 dengan metode outer join
"""

"""
Memecah nilai string ke dalam beberapa kolom pada Data Frame
data = {'full name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'], 'tempat_kelahiran': ['New York , NY', 'Los Angeles , CA', 'Chicago , IL', 'Houston , TX ']}
df = pd.DataFrame(data)
pd.DataFrame(df['full name'].str.split(' ', expand=True))
df[['kota', 'provinsi']] = df['tempat_kelahiran'].str.split(' ,', expand=True)
print(df)
"""

"""
Menata ulang Data Frame dengan multiple indexes menggunakan unstack
df = pd.read_csv("D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv")
df.groupby(['Sex', 'Pclass'])['survived'].mean().to_frame().unstack()
print(df)
"""


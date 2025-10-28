#Pandas - Week 5 28/10/2025
#Mulai 15.00 WIB
#Selesai 16.00 WIB
import pandas as pd
import numpy as np

"""
Agregasi pada Pandas Data Frame dengan agg
df = pd.read('./data/iris.csv')
df.groupby('species')['PetalLengthCm'].count().to_frame()
df.groupby('species')['PetalLengthCm'].mean().to_frame()
df.groupby('species')['PetalLengthCm'].median().to_frame()
df.groupby('species')['PetalLengthCm'].agg(['count', 'mean', 'median'])
df.groupby('species')['PetalLengthCm'].describe()
"""

"""
Mengecek penggunaan memori pada Data Frame
df_titanic = pd.read_csv("D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv")
df_titanic.head()
df_iris = pd.read_csv("./data/iris.csv")
df_iris.head()

df_titanic.info(memory_usage='deep')
df_iris.info(memory_usage='deep')
df_titanic.describe(deep=True)
df_iris.describe(deep=True)
"""

"""
Melakukan query pada Data Frame menggunakan metode query
d = {'kolom_satu': [1, 2, 3,4,5], 'kolom_dua': [10,20,30,40,50]}
df = pd.DataFrame(d)

df.query('kolom_satu > 2')
df.query('kolom_dua < 30')
"""

s = pd.Series([range(1591683521, 1592201921, 3600)]) #Membuat Series dengan rentang nilai timestamp
s = pd.to_datetime(s, unit='s') #Mengonversi nilai timestamp ke dalam format datetime
s.head()

s = s.dt.tz_localize('UTC') #Menambahkan informasi zona waktu UTC pada Series
s.head()
s = s.dt.tz_convert('Asia/Jakarta') #Mengonversi zona waktu ke Asia/Jakarta 
s.head()
s = s.dt.tz_convert('Australia/Hobart') #Mengonversi zona waktu ke Australia/Hobart
s.head()


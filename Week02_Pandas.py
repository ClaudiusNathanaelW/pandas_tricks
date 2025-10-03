"""
Latihan Pandas Week 02
Claudius Nathanael Wijaya
2473010
28/09/2025
14.20
"""
import pandas as pd
import numpy as np
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')


df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)), columns=cols)
print('Normal Data Frame\n',df,'\n',sep='')

"""
Pandas 05
Membalik urutan baris dan kolom pada DF

dfswitchcol = df.loc[:, ::-1]
print('Collumn Switch\n',dfswitchcol,'\n',sep='')

dfswitchrow = df.loc[::-1]
print('Row Switch\n',dfswitchrow,'\n',sep='')
#.reset index(drop=True) #untuk mengembalikan index ke 0,1,2,3...

dfswitchboth = df.loc[::-1, ::-1]
print('Switch Both\n',dfswitchboth,'\n',sep='')
"""

"""
Pandas 06
Mengganti nama (label) kolom pada DF

# Untuk mengganti nama kolom pada DataFrame:
# df.rename(columns={'nama_kolom_lama': 'nama_kolom_baru', ...})
dfrename = df.rename(columns={'A':'kolom_1', 'B':'kolom_2', 'C':'kolom_3', 'D':'kolom_4', 'E':'kolom_5'})
print('Rename Columns\n',dfrename.to_string(justify='center'),'\n',sep='')

#dfrename = dfrename.to_string(justify='center') #Untuk meratakan tengah
"""

"""
Pandas 07
Menghapus drop values (NaN) pada DF

# Membuat DataFrame dengan missing values (NaN)
dfmiss = pd.DataFrame(
    np.random.randn(5, 5),
    columns=list('ABCDE')
)
dfmiss.iloc[1, 2] = np.nan
dfmiss.iloc[3, 0] = np.nan
dfmiss.iloc[4, 4] = np.nan
dfmiss = dfmiss.reset_index(drop=True)
dfmiss.head()

#dfmiss.head() berfungsi untuk menampilkan 5 baris pertama
dfmiss = dfmiss.rename(columns={'index':'Z'})
dfmiss.head()

#Sebelum menghapus NaN, buat backup data frame
dfmiss_backup = dfmiss.copy(deep=True) #Membuat backup data frame
dfdrop = dfmiss.dropna(axis='columns') #Menghapus baris yang memiliki NaN
print('Data Frame after drop NaN\n\n',dfdrop.to_string(justify='center'),'\n',sep='')

#Persentase missing value untuk setiap kolom
dfmiss = dfmiss_backup.copy(deep=True) #Mengembalikan data frame ke kondisi awal
dfmiss.isna().mean()

threshold = len(dfmiss)*0.9
dfmiss = dfmiss.dropna(thresh=threshold, axis='columns') #Menghapus kolom dengan threshold
print('Data Frame after drop NaN with threshold 90%\n\n',dfmiss.to_string(justify='center'),'\n',sep='')
"""

"""
Pandas 08
Memeriksa kesamaan antar dua buah kolom (Series) pada DF
"""

data = {'A': [15,15,18, np.nan, 12],
        'B': [15,15,18, np.nan, 12],}

df = pd.DataFrame(data)
# Series adalah kolom pada data frame
# Memeriksa kesamaan dengan operator ==
checksame = df['A'] == df['B']
print('Sama\n',checksame,'\n',sep='')
# Memeriksa kesamaan dengan method .equals()
df1 = df.copy(deep=True)
df.equals(df1)
df == df1
print('Sama??\n\n',df.equals(df1),'\n',sep='')

# Selesai jam 15.30 (28/09/2025)
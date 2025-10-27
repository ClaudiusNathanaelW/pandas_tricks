#Pandas - Week 5 27/10/2025
#Mulai 15.00 WIB
#Selesai 16.00 WIB
import pandas as pd
import numpy as np
"""
#Resampling pada data deret waktu
n_rows = 365 * 24
n_cols = 2
cols = ('col1', 'col2')

df = pd.DataFrame(np.random.randint(1, 20, size=(n_rows, n_cols)), columns=cols)
df.index = pd.util.testing.makeDateIndex(n_rows, freq='H') #Membuat index datetime dengan frekuensi per jam

resampleM = df.resample('M').col1.sum().to_frame() #Resampling data per bulan dengan menjumlahkan nilai pada col1
resampleD = df.resample('D').col1.sum().to_frame() #Resampling data per bulan dengan menjumlahkan nilai pada col1
print(df)
"""

"""
#Membentuk Data Frame dari Dictionary

df = pd.DataFrame({'col1': [1,2,3,4], 'col2': [5,6,7,8]}) 

n_rows = 5
n_cols = 3
arr = np.random.randint(1, 20, size=(n_rows, n_cols))
df2=pd.DataFrame(arr, columns=['ABC'])

dfR=pd.util.testing.makeDataFrame() #Membuat Data Frame dengan data acak dan kolom bertipe float
dfM=pd.util.testing.makeMixedDataFrame() #Membuat Data Frame dengan data acak dan kolom bertipe campuran
dfT=pd.util.testing.makeTimeDataFrame() #Membuat Data Frame dengan data acak dan index bertipe datetime
dfMissing=pd.util.testing.makeMissingDataframe() #Membuat Data Frame dengan data acak dan beberapa nilai hilang (NaN)
print(df)
"""
"""
#Formatting tampilan Data Frame

n_rows = 5
n_cols = 2  
cols = ('omset','operasional')
df = pd.DataFrame(np.random.randint(10,20, size=(n_rows, n_cols)), columns=cols)
df['omset'] = df['omset']*100_000 #Mengalikan kolom omset dengan 100.000
df['operasional'] = df['operasional']*10_000 #Mengalikan kolom operasional dengan 10.000

df_index = pd.util.testing.makeDateIndex(n_rows, freq='D') #Membuat index datetime dengan frekuensi harian
df = df.reset_index()
df = df.rename(columns={'index': 'tanggal'})
print(df)

formatku = {'tanggal': '{:%d%m%Y}', 'omset': 'Rp {:,.2f}', 'operasional': 'Rp {:,.2f}'} #Format tampilan untuk setiap kolom
laporan = df.style.format(formatku) #Menerapkan format pada Data Frame
type(laporan)
laporan.hide_index()
laporan.set_caption("Data Omset dan Operasional")
laporan.highlight_min('omset', color='pink')
laporan.highlight_max('omset', color='lightgreen')

laporan.highlight_min('operasional', color='lightblue')
laporan.highlight_max('operasional', color='evergreen')
print(laporan)
"""

#Menggabungkan dua data frame secara berdampingan
d1 = {'col1': [1,2,3], 'col2': [10,20,30]}
df1 = pd.DataFrame(d1)
d2 = {'col3': [4,5,6], 'col4': [40,50,60]}
df2 = pd.DataFrame(d2)

df = pd.merge(df1, df2, left_index=True, right_index=True) #Menggabungkan df1 dan df2 secara berdampingan
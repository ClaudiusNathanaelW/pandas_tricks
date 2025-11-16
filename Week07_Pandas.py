import pandas as pd
"""
df = pd.read_csv('D:\\College\\3rd Semester\\pandas_tricks\\archive\\Titanic-Dataset.csv')
pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_colwidth', 20)

print(df)

pd.reset_option('^display', silent=True) #Mengembalikan semua opsi display ke pengaturan awal
pd.describe_option() #Menampilkan semua opsi konfigurasi pandas beserta nilainya
"""

"""
Membuat DF dari Select Spreadsheet
df = pd.read_clipboard()  #Membuat Data Frame dari data yang disalin ke clipboard
print(df)
"""

"""
Fungsi Agregasi First dan Last pada Data Frame
d = {'dokter': ['Budi', 'Wati', 'Iwan', 'Budi', 'Budi', 'Wati'], 'pasien': ['Abdul', 'Rahmat', 'Asep', 'Joko', 'Wiwin', 'Lisa']}
df = pd.DataFrame(d)
df.groupby('dokter').pasien.count().to_frame() #Menghitung jumlah pasien per dokter
df.groupby('dokter').pasien.first().to_frame() #Mengambil nama pasien pertama per dokter
df.groupby('dokter').pasien.last().to_frame() #Mengambil nama pasien terakhir per dokter
"""

#Mengenal Explode dan Implode List pada Pandas Data Frame
d = {'Team':['DC','Marvel'], 'Heroes':['Superman','Batman','Wonder Woman','Ironman','Spiderman','Hulk']}
df = pd.DataFrame(d)
df1 = df.explode('Heroes') #Mengubah setiap elemen dalam list pada kolom 'Heroes' menjadi baris terpisah

d = {'Team'['DC','DC','DC','Marvel','Marvel','Marvel']}
df2 = pd.DataFrame(d)
df2['imploded'] = df1.groupby['Heroes'].agg(list) #Menggabungkan kembali baris-baris menjadi list berdasarkan kolom 'Team'
print(df2)
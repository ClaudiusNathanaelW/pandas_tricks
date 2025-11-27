import pandas as pd

"""
Menampilkan nilai kumulatif pada Data Frame

d = {'pemain':['Budi', 'Joni', 'Iwan', 'Budi', 'Budi', 'Iwan', 'Asep', 'Joni'], 
     'goal':[2, 1, 3, 1, 1, 2, 2, 3]}
df = pd.DataFrame(d)
df['goal'].cumsum().to_frame()
df['jumlah_goal_kumulatif'] = df['goal'].cumsum()
df['jumlah_goal_kumulatif_tiap_pemain'] = df.groupby('pemain')['goal'].cumsum()
df['cummax'] = df['goal'].cummax()
df['cummin'] = df['goal'].cummin()
df['cumprod'] = df['goal'].cumprod()
"""

"""
Mapping pada Data Frame dengan applymap()
df = pd.DataFrame({'jenis_kelamin':['Pria', 'Wanita', 'lelaki', 'Lelaki', 'perempuan'], 
                   'usia':[23, 21, 24, 22, 21], 
                   'shift':['pagi', 'siang', 'Malam', 'Siang', 'pagi']})
df = df.applymap(lambda x: x.lower() if type(x) == str else x)
mapping = {'pria':'L',
           'lelaki':'L',
           'wanita':'P',
           'perempuan':'P',
           'pagi':1,
           'siang':2,
           'malam':3}
df.applymap(mapping.get)
df[['jenis_kelamin', 'shift']] = df[['jenis_kelamin', 'shift']].applymap(mapping.get)
"""

"""
Memadukan fungsi agregasi dengan transform()

d = {'no_nota':[1, 1, 1, 2, 2, 3, 4, 5], 
     'kopi': ['latte', 'cappuccino', 'espresso', 'latte', 'espresso', 'cappuccino', 'latte', 'espresso'],
     'harga':[50, 60, 80, 150, 120, 60, 100, 40]}

df = pd.DataFrame(d)
df.groupby('no_nota')['harga'].sum().to_frame()
df['total_harga'] = df.groupby('no_nota')['harga'].transform(sum)
df.groupby('kopi')['harga'].sum().to_frame()
df['total_omset'] = df.groupby('kopi')['harga'].transform(sum)
"""

"""
Menyatukan kolom dengan str.cat()
"""
data = {'nama': ['bayu', 'indra', 'devi', 'agni'],
        'jenis_kelamin': ['L', 'L', 'P', 'L'], 
        'usia': [23, 21, 22, 25]}

df = pd.DataFrame(data)
df['nama'].str.cat(df['jenis_kelamin'], sep=', ').to_frame()
df['nama_jk'] = df['nama'].str.cat(df['jenis_kelamin'], sep=', ')
df['nama'].str.cat(df['usia'].astype('str'), sep=' - ').to_frame()
df['nama_usia'] = df['nama'].str.cat(df['usia'].astype('str'), sep=' - ')

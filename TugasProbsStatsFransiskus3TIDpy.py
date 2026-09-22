
import pandas as pd
import matplotlib.pyplot as plt

# Pengorganisasian Data
path = r"C:\FilePython\frans.xlsx"
dataraw = pd.read_excel(path)

pd.set_option('display.max_columns', None)

print("=== DATA RAW ===")
print(dataraw)

# Pembuatan tabel frekuensi
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
print("\n=== TABEL FREKUENSI ===")
print(datafrq)


# Penyajian Data
datafrq.plot(title="Grafik Garis Frekuensi Grade")

# Grafik Batang
datafrq.plot(kind='bar', title="Grafik Batang Frekuensi Grade")

# Pie Chart
datafrq.plot(kind='pie', y='Frekuensi', autopct='%1.0f%%', legend=False, title="Pie Chart Grade")

# Menampilkan semua grafik ke layar
plt.show()

# Statistika Deskriptif 
dataraw["Final Score"] = pd.to_numeric(dataraw["Final Score"], errors='coerce')
dt = dataraw["Final Score"]

stats = dt.describe()
stats['Standard Error'] = dt.sem()
stats['Median'] = dt.median()
stats['Mode'] = dt.mode().iloc[0]
stats['variance'] = dt.var()
stats['range'] = dt.max() - dt.min()
stats['skewness'] = dt.skew()
stats['kurtosis'] = dt.kurtosis()

print("\n=== STATISTIKA DESKRIPTIF ===")
print(stats)
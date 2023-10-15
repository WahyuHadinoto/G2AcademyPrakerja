# TUGAS Unjuk Kemampuan

# ------------------------------------------------------------------------------
# 1. Melakukan download data
import pandas as pd # import library pandas dengan inisial pd

# Mengambil dataset dari https://www.kaggle.com/code/toramky/eda-for-automobile-dataset/input?select=Automobile_data.txt
# Link Dataset
sumber ='https://storage.googleapis.com/kagglesdsdata/datasets/1291/2317/Automobile_data.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231015%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231015T024022Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=6234cfce246eb2d85467baadd54bf414caddb8736148b89d3879ebe7f9288ab66a5d993af681502699d97fecea54a4e4f6709ce024955619d498f3c222f02cbcd169cb94c6fde08eb18c39dcdb824eb8450519e0df1d5f576d654260c324ec9075ecaff426281fc564280d70cab39cabb15a8981c7cbf9b9f9bee3f6b2557bb8f81eb717592b3a3e45e49672ec5dfe8816af5bd5083a62ff2b531ec4a17ca982daf7837d6309de548c3c964ce1796cca63e374ec6ea25c283bf9451a09b0c906ae03721045203459b52aa5b35a756aa49d9a37545876977218c0ae672d3d70eca88009f368105a2a9647d96efc0c65ff3424c3c6a89fd003f29096daea12f032'

# Membaca dataset secara langsung dari kegel data tabular ke data csv
data_mobil = pd.read_table(sumber, sep = ',')
data_mobil.to_csv('Automobile_data.csv',sep = ',')

#-------------------------------------------------------------------------------
# 2. Membaca Data csv dengan pandas
# Import dataset yang diunduh manual dalam bentuk csv
data_mobil = pd.read_csv('Automobile_data.csv',index_col = [0]) # Untuk membaca txt, gunakan read_table dengan separator ','


#-------------------------------------------------------------------------------
# 3A. Melakukan data cleaning
# Mengecek statistik deskripsi dataset
deskripsi = data_mobil.describe()
data_tanda = []

# Mengetahui kolom mana yang mengandung data '?'
for i in data_mobil.columns:
    x = list(data_mobil[i] == '?').count(True)
    if x != 0:
        data_tanda.append([i,x])

# Kelompok 1 untuk di clean ('bore','stroke',dan 'peak-rpm)
for i in ['bore', 'stroke', 'peak-rpm']:
    data_mobil[i] = pd.to_numeric(data_mobil[i],errors='coerce')
    
# Kelompok 2 untuk di clean ('normalized-losses', 'horsepower', dan 'price')
for i in ['normalized-losses', 'horsepower', 'price']:
    sementara = data_mobil[i].loc[data_mobil[i] != '?']
    sementara_mean = sementara.astype(str).astype(int).mean()
    data_mobil[i] = data_mobil[i].replace('?',sementara_mean).astype(int)

# Kelompok 3 untuk di clean ('num-of-doors')
data_mobil = data_mobil[data_mobil['num-of-doors'] != '?']

# Menyimpan data yang telah di bersihkan
data_mobil.to_csv('Automobile_data_clean.csv',sep = ',')

#-------------------------------------------------------------------------------
# 3B. Melakukan data exploratory

    
#Mengimpor Pustaka yang Diperlukan
#Mengimpor modul-modul yang dibutuhkan dalam program
import h5py
import numpy as np
from PIL import Image
from google.colab import drive
#Keempat modul tersebut memiliki fungsi sebagai berikut:

#h5py: Digunakan untuk berinteraksi dengan file HDF5, yang cocok untuk menyimpan data kompleks seperti array multidimensi atau dataset besar.
#numpy: Pustaka dasar untuk komputasi numerik di Python, membantu dalam manipulasi dan analisis array data berdimensi tinggi.
#PIL (Python Imaging Library): Berguna untuk memanipulasi gambar, membuka, menyimpan, dan memanipulasi berbagai jenis format gambar.
g#oogle.colab: Modul khusus untuk Google Colab, memfasilitasi kolaborasi tim, pembelajaran mesin, dan penelitian dengan menyediakan sumber daya komputasi yang besar serta alat khusus untuk bekerja dalam lingkungan Colab.
#Mengakses File dari Google Drive
# Mount Google Drive
drive.mount('/content/drive')
#Kode di atas digunakan untuk mengakses file di Google Drive langsung dari notebook Colab.

#Menyimpan dan Membaca File HDF5
#Pertama-tama, fungsi ini membaca sebuah gambar, mengonversinya menjadi array NumPy, dan kemudian menyimpan array tersebut ke dalam file HDF5 dengan dataset bernama 'image'.

def save_image_to_hdf5(image_path, hdf5_file):
    # Baca gambar menggunakan PIL
    image = Image.open(image_path)
    # Konversi gambar menjadi array numpy
    image_array = np.array(image)

    # Simpan array gambar ke dalam file HDF5
    with h5py.File(hdf5_file, 'w') as hf:
        hf.create_dataset('image', data=image_array)
#Fungsi berikutnya akan membaca array gambar dari file HDF5 dan mengembalikan gambar dalam format PIL.

def read_image_from_hdf5(hdf5_file):
    # Baca array gambar dari file HDF5
    with h5py.File(hdf5_file, 'r') as hf:
        image_array = np.array(hf['image'])

    # Konversi array numpy ke dalam gambar PIL
    image = Image.fromarray(image_array)
    return image
#Kode berikut ini akan melakukan beberapa langkah:

#Menyimpan gambar dari path tertentu ke dalam file HDF5 menggunakan fungsi save_image_to_hdf5.

#Membaca kembali gambar dari file HDF5 yang baru saja disimpan menggunakan fungsi read_image_from_hdf5.

#Menampilkan informasi mengenai gambar yang dibaca, seperti ukuran dan mode gambar.

#Menampilkan gambar yang dibaca menggunakan metode show() dari objek gambar PIL.

#Dengan demikian, kode ini akan menyimpan gambar ke dalam file HDF5, membacanya kembali, serta menampilkan informasi dan gambar yang telah dibaca.

# Path ke gambar
image_path = '/content/drive/My Drive/Pistaschio/kirmizi (7).jpg'

# Nama file HDF5
hdf5_file = '/content/drive/My Drive/Pistaschio/kirmizi.h5'

# Simpan gambar ke dalam file HDF5
save_image_to_hdf5(image_path, hdf5_file)

# Baca gambar dari file HDF5
retrieved_image = read_image_from_hdf5(hdf5_file)

# Tampilkan informasi gambar
print("Ukuran Gambar:", retrieved_image.size)
print("Mode Gambar:", retrieved_image.mode)

# Tampilkan gambar yang dibaca
retrieved_image.show()
#Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
#Ukuran Gambar: (600, 600)
#Mode Gambar: RGB
#Gambar Telah berhasil disimpan.

#Berikut merupakan proses dari tugas multimedia Database
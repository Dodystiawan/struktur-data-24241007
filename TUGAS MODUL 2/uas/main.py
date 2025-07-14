# mencatat data belanja custemer di sebuah toko

# data customer
data_customer = {}

# Meminta jumlah customer
jumlah = int(input("Masukkan nama customer: "))

# Input data untuk setiap customer
for i in range(jumlah):
    print(f"\nnama Customer ke-{i+1}")
    nama_barang = input("Masukkan barang: ")
    nama = input("Masukkan Nama: ")
    jumlah_barang = int(input("Masukkan Data Customer: "))
    
    nama_barang = {}
    total_harga= 0
    
    for j in range(jumlah_barang):
        nama_barang = input(f"  Nama barang ke-{j+1}: ")
        jumlah_barang= float(input(f"  jumlah barang {jumlah_barang}: "))
        nama_barang[nama_barang]
        total_harga
    
    jumlah_barang= total_harga / jumlah_barang
    data_customer[nama] = {
        "nama": nama,
        "nama barang": nama_barang,
        "jumlah barang": jumlah_barang
    }

# Menampilkan hasil
print("\n=== Daftar Belanja Customer===")
for nama, info in data_customer.items():
    print(f"\nNama    : {nama}")
    print(f"harga barang    : {info['nama barang']}")
    print("jumlah barang:")
    for nb, nilai in info['matkul'].items():
        print(f"  {nb} : {nilai}")
    print(f"harga barang: {info['rata_rata']:.2f}")
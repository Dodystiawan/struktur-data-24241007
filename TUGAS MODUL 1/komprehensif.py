# Program Rekap Nilai Mahasiswa

# Menyimpan semua data mahasiswa
data_mahasiswa = {}

# Meminta jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Input data untuk setiap mahasiswa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    
    matkul = {}
    total_nilai = 0
    
    for j in range(jumlah_matkul):
        nama_matkul = input(f"  Nama Mata Kuliah ke-{j+1}: ")
        nilai = float(input(f"  Nilai Mata Kuliah {nama_matkul}: "))
        matkul[nama_matkul] = nilai
        total_nilai += nilai
    
    rata_rata = total_nilai / jumlah_matkul
    data_mahasiswa[nim] = {
        "nama": nama,
        "matkul": matkul,
        "rata_rata": rata_rata
    }

# Menampilkan hasil
print("\n=== Daftar Nilai Mahasiswa ===")
for nim, info in data_mahasiswa.items():
    print(f"\nNIM     : {nim}")
    print(f"Nama    : {info['nama']}")
    print("Nilai Mata Kuliah:")
    for mk, nilai in info['matkul'].items():
        print(f"  {mk} : {nilai}")
    print(f"Rata-rata Nilai: {info['rata_rata']:.2f}")
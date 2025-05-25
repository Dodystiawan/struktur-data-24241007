 # Insertion pada tengah elemen array
# membuat array
arr = [12, 16, 20, 40, 50, 70]

# cetak arr sebelum penyisipan
print("Array Sebelum Insertion : ", arr)

# cetak panjang array sebelum penyisipan
print("Panjang Array : ", len(arr))

# menyisipkan array pada tengah elemen menggunakan .insert(pos, x)
arr.insert(4, 5)

# cetak arr setelah penyisipan
print("Array Setelah Insertion : ", arr)

# cetak panjang array setelah penyisipan
print("Panjang Array : ", len(arr))

# jika tidak menggunakan fungsi .insert()
# membuat array dan cetak array
arr = [12, 16, 20, 40, 50, 70]
print("Array Sebelum Penyisipan : " , arr)

# Deklarasi elemen tengah yang disisipkan
pos = 4

# Deklarasi nilai yang akan disisipkan
x = 5

# menambah elemen dummy agar menambah panjang array
arr.append(0) # arr = [12, 16, 20, 40, 50, 70, 0]

# melakukan pergeseran elemen mulai dari belakang
for i in range(len(arr) - 2, pos-1, -1):
    arr[i + 1] = arr[i]

# memasukkan nilai x pada elemen yang diinginkan
arr[pos] = x

# Cetak array baru
print("Array Sesudah Penyisipan : ", arr)
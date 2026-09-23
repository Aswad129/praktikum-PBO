# Sistem Manajemen dan Pemesanan Kamar Kost

## Deskripsi Program

Program ini digunakan untuk menggambarkan proses pengelolaan kamar kost dan pemesanan kamar oleh calon penghuni. Program memiliki dua jenis pengguna, yaitu **User** sebagai calon penghuni/pelanggan dan **Admin** sebagai pemilik atau pengelola kost.

# Struktur Class

Program terdiri dari 5 class utama:

```text
Sistem Manajemen dan Pemesanan Kamar Kost
│
├── User
├── Admin
├── Kamar
├── Pemesanan
└── Pembayaran
```

---

## 1. Class `User`

Class `User` digunakan untuk menyimpan data pelanggan atau calon penghuni kost.

### Atribut Class

```python
nama_sistem
total_user
status_sistem
```

Atribut tersebut digunakan sebagai informasi yang bersifat umum dan dapat digunakan oleh seluruh objek `User`.

### Instance Attribute

```python
id_user
nama
username
__password
```

`__password` merupakan **private attribute** karena berisi data penting dan tidak diakses secara langsung dari luar class.

### Method

- `tampilkan_data()` → menampilkan data user.
- `dari_data()` → class method untuk membuat objek berdasarkan data.
- `validasi_username()` → static method untuk melakukan validasi username.

### Property

```python
@property
def password(self):
```

Digunakan sebagai getter untuk mengambil password.

Setter digunakan untuk mengubah password sekaligus melakukan validasi.

---

## 2. Class `Admin`

Class `Admin` digunakan untuk merepresentasikan pemilik atau pengelola kost.

### Atribut Class

```python
nama_role
total_admin
hak_akses
```

### Instance Attribute

```python
id_admin
nama
username
__password
```

Password dibuat sebagai private attribute menggunakan:

```python
__password
```

### Method

- `tampilkan_data()` → menampilkan data admin.
- `kelola_kamar()` → menggambarkan fungsi admin dalam mengelola kamar.
- `konfirmasi_pemesanan()` → menggambarkan fungsi admin dalam mengelola pemesanan.
- `dari_data()` → class method untuk membuat objek admin.
- `validasi_username()` → static method untuk validasi username.

### Property

Property `password` digunakan untuk mengakses dan mengubah password dengan validasi.

---

## 3. Class `Kamar`

Class `Kamar` digunakan untuk menyimpan informasi kamar kost.

### Atribut Class

```python
nama_kost
total_kamar
lokasi_kost
```

### Instance Attribute

```python
id_kamar
nomor
fasilitas
status
__harga
```

Atribut `__harga` dibuat sebagai private attribute karena harga merupakan data yang perlu divalidasi.

### Method

- `tampilkan_info()` → menampilkan informasi kamar.
- `ubah_status()` → mengubah status kamar.
- `dari_data()` → class method untuk membuat objek kamar.
- `validasi_harga()` → static method untuk melakukan validasi harga.

### Property

Property `harga` digunakan untuk mengambil dan mengubah harga kamar.

Setter harga melakukan validasi agar harga yang dimasukkan harus lebih dari 0.

---

## 4. Class `Pemesanan`

Class `Pemesanan` digunakan untuk menyimpan data pemesanan kamar oleh user.

### Atribut Class

```python
nama_sistem
total_pemesanan
status_default
```

### Instance Attribute

```python
id_pemesanan
user
kamar
tanggal
__status
```

Atribut `__status` merupakan private attribute.

### Method

- `tampilkan_pemesanan()` → menampilkan informasi pemesanan.
- `konfirmasi()` → mengubah status pemesanan menjadi dikonfirmasi.
- `tolak()` → mengubah status pemesanan menjadi ditolak.
- `dari_data()` → class method untuk membuat objek pemesanan.
- `validasi_tanggal()` → static method untuk validasi tanggal.

### Property

Property `status` digunakan untuk mengakses dan mengubah status pemesanan.

Status yang diperbolehkan:

```text
Menunggu
Dikonfirmasi
Ditolak
```

---

## 5. Class `Pembayaran`

Class `Pembayaran` digunakan untuk menyimpan data pembayaran dari pemesanan kamar.

### Atribut Class

```python
nama_sistem
total_pembayaran
mata_uang
```

### Instance Attribute

```python
id_pembayaran
pemesanan
metode
__jumlah
__status
```

Atribut `__jumlah` dan `__status` merupakan private attribute.

### Method

- `tampilkan_pembayaran()` → menampilkan informasi pembayaran.
- `konfirmasi_pembayaran()` → mengubah status pembayaran.
- `dari_data()` → class method untuk membuat objek pembayaran.
- `validasi_jumlah()` → static method untuk validasi jumlah pembayaran.

### Property

Property yang digunakan:

```python
jumlah
status
```

Setter melakukan validasi terhadap nilai yang diberikan.

---

# Encapsulation

Encapsulation diterapkan dengan membuat beberapa atribut menjadi **private** menggunakan dua garis bawah (`__`).

Contohnya:

```python
self.__password
```

atau:

```python
self.__harga
```

Atribut private tidak diakses secara langsung dari luar class.

Sebagai gantinya, digunakan property:

```python
@property
def password(self):
    return self.__password
```

dan setter:

```python
@password.setter
def password(self, password):
```

Dengan cara tersebut, data dapat dikontrol sebelum diubah.

---

# 🔎 Getter dan Setter

Program menggunakan `@property` sebagai getter dan `@property.setter` sebagai setter.

Contoh:

```python
@property
def harga(self):
    return self.__harga

@harga.setter
def harga(self, harga):
    if harga <= 0:
        raise ValueError("Harga harus lebih dari 0")
    self.__harga = harga
```

Jika nilai yang diberikan tidak sesuai aturan, program akan memberikan peringatan atau `ValueError`.

Contohnya:

```python
kamar1.harga = 500000
```

Nilai tersebut diterima karena valid.

Sedangkan:

```python
kamar1.harga = -100000
```

akan ditolak karena harga tidak boleh bernilai negatif.

---

# Jenis Method

Program menerapkan tiga jenis method.

## 1. Instance Method

Instance method menggunakan parameter `self`.

Contoh:

```python
def tampilkan_data(self):
    ...
```

Method ini digunakan melalui objek.

Contoh:

```python
user1.tampilkan_data()
```

---

## 2. Class Method

Class method menggunakan decorator:

```python
@classmethod
```

dan menerima parameter `cls`.

Contoh:

```python
@classmethod
def dari_data(cls, data):
    ...
```

Class method digunakan untuk membuat objek berdasarkan data tertentu atau mengakses atribut milik class.

---

## 3. Static Method

Static method menggunakan:

```python
@staticmethod
```

Method ini tidak membutuhkan `self` ataupun `cls`.

Contoh:

```python
@staticmethod
def validasi_username(username):
    ...
```

Static method digunakan untuk fungsi bantuan atau validasi yang tidak bergantung pada objek tertentu.

---

# Panduan Pengujian

## 1. Pengujian Object

Program membuat minimal dua objek untuk setiap class.

Contoh:

```python
user1 = User(...)
user2 = User(...)

admin1 = Admin(...)
admin2 = Admin(...)

kamar1 = Kamar(...)
kamar2 = Kamar(...)
```

Hal yang sama dilakukan untuk class `Pemesanan` dan `Pembayaran`.

---

## 2. Pengujian Instance Method

Instance method dipanggil melalui objek.

Contoh:

```python
user1.tampilkan_data()
kamar1.tampilkan_data()
pemesanan1.tampilkan_pemesanan()
pembayaran1.tampilkan_pembayaran()
```

Tujuannya untuk memastikan method dapat dijalankan oleh objek.

---

## 3. Pengujian Class Method

Class method diuji dengan memanggil method melalui class.

Contoh:

```python
User.dari_data(...)
Kamar.dari_data(...)
```

Tujuannya untuk memastikan class method dapat membuat objek berdasarkan data yang diberikan.

---

## 4. Pengujian Static Method

Static method diuji menggunakan contoh validasi.

Contoh:

```python
User.validasi_username("andi")
Kamar.validasi_harga(500000)
```

Tujuannya untuk memastikan proses validasi dapat berjalan tanpa membutuhkan objek.

---

## 5. Pengujian Setter dengan Data Valid

Contoh:

```python
kamar1.harga = 850000
```

Hasil yang diharapkan:

```text
Harga berhasil diubah.
```

---

## 6. Pengujian Setter dengan Data Tidak Valid

Contoh:

```python
kamar1.harga = -500000
```

Hasil yang diharapkan adalah program menolak nilai tersebut dan memberikan pesan kesalahan.

Contoh:

```text
Harga harus lebih dari 0.
```

Pengujian serupa dilakukan pada property lain seperti password, status, dan jumlah pembayaran.

---

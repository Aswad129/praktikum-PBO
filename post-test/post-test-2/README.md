# Sistem Manajemen dan Pemesanan Kamar Kost

## Deskripsi Program

Program ini digunakan untuk menggambarkan proses pengelolaan kamar kost dan pemesanan kamar oleh calon penghuni. Program memiliki tiga jenis pengguna, yaitu **User** sebagai pengguna umum, **Penghuni** sebagai penghuni kost yang dapat memesan kamar, dan **Admin** sebagai pemilik atau pengelola kost.

Program dibuat dengan **Python** menggunakan konsep **Pemrograman Berorientasi Objek (OOP)**, meliputi inheritance, encapsulation, agregasi, komposisi, serta tiga jenis method (instance, class, dan static).

# Struktur Class

Program terdiri dari 6 class utama:

```text
Sistem Manajemen dan Pemesanan Kamar Kost
│
├── User
│   ├── Penghuni   (inheritance)
│   └── Admin      (inheritance)
├── Kamar
├── Pemesanan
└── Pembayaran
```

## Relasi Antar Class

```text
Admin     ◇── Kamar        Agregasi  : Admin mengelola daftar kamar (daftar_kamar)
Pemesanan ──► User/Penghuni            : pemesanan dilakukan oleh user
Pemesanan ──► Kamar                    : pemesanan untuk kamar tertentu
Pemesanan ◆── Pembayaran   Komposisi : pembayaran dibuat oleh pemesanan
```

- **Inheritance**: `Penghuni` dan `Admin` mewarisi class `User`.
- **Agregasi**: objek `Kamar` dibuat terpisah, lalu ditambahkan ke `Admin` melalui `tambah_kamar()`. Kamar tetap ada walaupun admin tidak ada.
- **Komposisi**: objek `Pembayaran` dibuat langsung di dalam `Pemesanan` melalui `buat_pembayaran()`. Pembayaran tidak berdiri sendiri tanpa pemesanan.

---

## 1. Class `User`

Class `User` merupakan **parent class** yang menyimpan data dasar pengguna sistem.

### Atribut Class

```python
nama_aplikasi
total_user
status
```

Atribut tersebut digunakan sebagai informasi yang bersifat umum dan dapat digunakan oleh seluruh objek `User`. `total_user` bertambah setiap kali objek `User` (termasuk `Penghuni` dan `Admin`) dibuat.

### Instance Attribute

```python
id_user
nama
_username
__password
_status_akun
```

- `_username` dan `_status_akun` merupakan **protected attribute** (satu garis bawah).
- `__password` merupakan **private attribute** karena berisi data penting dan tidak diakses secara langsung dari luar class.

### Method

- `tampilkan_data()` → menampilkan data user.
- `dari_data()` → class method untuk membuat objek berdasarkan data (dictionary).
- `validasi_username()` → static method untuk validasi username (tidak boleh kosong dan tidak boleh mengandung spasi).

### Property

```python
@property
def password(self):
```

Digunakan sebagai getter untuk mengambil password.

Setter digunakan untuk mengubah password sekaligus melakukan validasi:

- password tidak boleh kosong
- password minimal 6 karakter

---

## 2. Class `Penghuni` (turunan `User`)

Class `Penghuni` merepresentasikan penghuni kost yang dapat melakukan pemesanan kamar.

### Instance Attribute

```python
id_user
nama
_username
__password
_status_akun
nomor_kamar
```

Atribut dari `User` diwariskan menggunakan `super().__init__()`, sedangkan `nomor_kamar` merupakan atribut tambahan milik `Penghuni`.

### Method

- `tampilkan_data()` → **method overriding**, menampilkan data penghuni beserta nomor kamar.
- `pesan_kamar()` → menggambarkan fungsi penghuni dalam memesan kamar.
- `dari_data()` → class method untuk membuat objek penghuni (memerlukan key `nomor_kamar`).

---

## 3. Class `Admin` (turunan `User`)

Class `Admin` digunakan untuk merepresentasikan pemilik atau pengelola kost.

### Instance Attribute

```python
id_user
nama
_username
__password
_status_akun
hak_akses
daftar_kamar
```

`daftar_kamar` berupa list yang menampung objek `Kamar` (**agregasi**).

### Method

- `tampilkan_data()` → **method overriding**, menampilkan data admin beserta hak akses.
- `kelola_kamar()` → menggambarkan fungsi admin dalam mengelola kamar.
- `tambah_kamar()` → menambahkan objek `Kamar` ke daftar kelolaan admin.
- `tampilkan_daftar_kamar()` → menampilkan seluruh kamar yang dikelola admin.

---

## 4. Class `Kamar`

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
nomor_kamar
fasilitas
status
__harga
```

Atribut `__harga` dibuat sebagai private attribute karena harga merupakan data yang perlu divalidasi.

### Method

- `tampilkan_kamar()` → menampilkan informasi kamar.
- `ubah_status()` → mengubah status kamar.
- `dari_data()` → class method untuk membuat objek kamar.
- `validasi_harga()` → static method untuk melakukan validasi harga.

Status kamar yang diperbolehkan:

```text
Tersedia
Terisi
Dalam maintenance
```

### Property

Property `harga` digunakan untuk mengambil dan mengubah harga kamar.

Setter harga melakukan validasi agar harga yang dimasukkan harus lebih dari 0.

---

## 5. Class `Pemesanan`

Class `Pemesanan` digunakan untuk menyimpan data pemesanan kamar oleh user.

### Atribut Class

```python
nama_aplikasi
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
pembayaran
```

- `__status` merupakan private attribute.
- `pembayaran` berisi objek `Pembayaran` (**komposisi**), awalnya `None` sampai `buat_pembayaran()` dipanggil.

### Method

- `tampilkan_pemesanan()` → menampilkan informasi pemesanan.
- `konfirmasi()` → mengubah status pemesanan menjadi dikonfirmasi dan status kamar menjadi `Terisi`.
- `tolak()` → mengubah status pemesanan menjadi ditolak.
- `buat_pembayaran()` → membuat objek `Pembayaran` dengan jumlah sesuai harga kamar.
- `dari_data()` → class method untuk membuat objek pemesanan (menerima `data`, `user`, dan `kamar`).
- `validasi_tanggal()` → static method untuk validasi format tanggal `YYYY-MM-DD`.

### Property

Property `status` digunakan untuk mengakses dan mengubah status pemesanan.

Status yang diperbolehkan:

```text
Menunggu
Dikonfirmasi
Ditolak
```

---

## 6. Class `Pembayaran`

Class `Pembayaran` digunakan untuk menyimpan data pembayaran dari pemesanan kamar.

### Atribut Class

```python
nama_aplikasi
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

Atribut `__jumlah` dan `__status` merupakan private attribute. Status awal pembayaran adalah `Belum Lunas`.

### Method

- `tampilkan_pembayaran()` → menampilkan informasi pembayaran.
- `konfirmasi_pembayaran()` → mengubah status pembayaran menjadi `Lunas`.
- `dari_data()` → class method untuk membuat objek pembayaran (menerima `data` dan `pemesanan`).
- `validasi_jumlah()` → static method untuk validasi jumlah pembayaran.

### Property

Property yang digunakan:

```python
jumlah
status
```

Setter melakukan validasi terhadap nilai yang diberikan.

---

# Inheritance dan Method Overriding

`Penghuni` dan `Admin` mewarisi atribut dan method dari `User`.

```python
class Penghuni(User):
    def __init__(self, id_user, nama, username, password, nomor_kamar):
        super().__init__(id_user, nama, username, password)
        self.nomor_kamar = nomor_kamar
```

Method `tampilkan_data()` ditulis ulang (**override**) pada `Penghuni` dan `Admin` sehingga setiap class menampilkan data sesuai perannya.

---

# Agregasi dan Komposisi

## Agregasi (`Admin` dan `Kamar`)

Objek `Kamar` dibuat secara terpisah, kemudian dimasukkan ke dalam daftar milik admin.

```python
admin1.tambah_kamar(kamar1)
admin1.tambah_kamar(kamar2)
admin1.tampilkan_daftar_kamar()
```

## Komposisi (`Pemesanan` dan `Pembayaran`)

Objek `Pembayaran` dibuat di dalam `Pemesanan`, sehingga pembayaran bergantung pada pemesanan.

```python
pemesanan1.buat_pembayaran("B001", "Transfer")
pemesanan1.pembayaran.tampilkan_pembayaran()
```

---

# Encapsulation

Encapsulation diterapkan dengan membuat beberapa atribut menjadi **protected** (`_`) dan **private** (`__`).

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
def password(self, password_baru):
```

Dengan cara tersebut, data dapat dikontrol sebelum diubah.

---

# Getter dan Setter

Program menggunakan `@property` sebagai getter dan `@property.setter` sebagai setter.

Contoh:

```python
@property
def harga(self):
    return self.__harga

@harga.setter
def harga(self, harga_baru):
    if harga_baru <= 0:
        raise ValueError("Harga harus lebih dari 0!")
    self.__harga = harga_baru
    print("harga kamar berhasil di ubah")
```

Jika nilai yang diberikan tidak sesuai aturan, program akan memberikan `ValueError`.

Contohnya:

```python
kamar1.harga = 500000
```

Nilai tersebut diterima karena valid.

Sedangkan:

```python
kamar1.harga = -100000
```

akan ditolak karena harga harus lebih dari 0.

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

Class method digunakan sebagai _alternative constructor_, yaitu membuat objek berdasarkan data tertentu (dictionary).

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

penghuni1 = Penghuni(...)
penghuni2 = Penghuni(...)

admin1 = Admin(...)
admin2 = Admin(...)

kamar1 = Kamar(...)
kamar2 = Kamar(...)

pemesanan1 = Pemesanan(...)
pemesanan2 = Pemesanan(...)
```

Objek `Pembayaran` dibuat melalui `pemesanan1.buat_pembayaran(...)` dan `pemesanan2.buat_pembayaran(...)`.

---

## 2. Pengujian Agregasi

```python
admin1.tambah_kamar(kamar1)
admin1.tambah_kamar(kamar2)
admin1.tampilkan_daftar_kamar()
```

Tujuannya untuk memastikan admin dapat menyimpan dan menampilkan daftar kamar yang dikelola.

---

## 3. Pengujian Komposisi

```python
pemesanan1.buat_pembayaran("B001", "Transfer")
pemesanan1.pembayaran.tampilkan_pembayaran()
```

Tujuannya untuk memastikan pembayaran berhasil dibuat dari pemesanan.

---

## 4. Pengujian Instance Method

Instance method dipanggil melalui objek.

Contoh:

```python
kamar1.ubah_status("Terisi")
pemesanan1.konfirmasi()
pemesanan1.pembayaran.konfirmasi_pembayaran()
```

Tujuannya untuk memastikan method dapat dijalankan oleh objek dan status berubah sesuai proses.

---

## 5. Pengujian Class Method

Class method diuji dengan memanggil method melalui class.

Contoh:

```python
Kamar.dari_data(data_kamar)
User.dari_data(data_user)
```

Tujuannya untuk memastikan class method dapat membuat objek berdasarkan data yang diberikan.

---

## 6. Pengujian Static Method

Static method diuji menggunakan contoh validasi.

Contoh:

```python
Kamar.validasi_harga(800000)
User.validasi_username("andi")
Pemesanan.validasi_tanggal("2026-10-06")
Pembayaran.validasi_jumlah(500000)
```

Tujuannya untuk memastikan proses validasi dapat berjalan tanpa membutuhkan objek.

---

## 7. Pengujian Getter

```python
print(user1.password)
print(kamar1.harga)
print(pemesanan1.status)
print(pemesanan1.pembayaran.jumlah)
```

Tujuannya untuk memastikan nilai atribut private dapat diakses melalui property.

---

## 8. Pengujian Setter dengan Data Valid

Contoh:

```python
kamar1.harga = 850000
```

Hasil yang diharapkan:

```text
harga kamar berhasil di ubah
```

---

## 9. Pengujian Setter dengan Data Tidak Valid

Contoh:

```python
kamar1.harga = -500000
```

Hasil yang diharapkan adalah program menolak nilai tersebut dan memberikan pesan kesalahan.

Contoh:

```text
ValueError: Harga harus lebih dari 0!
```

Pengujian serupa dapat dilakukan pada property lain, seperti:

```python
user1.password = "abc"
user1.password = ""
```

---

# Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
python nama_file.py
```

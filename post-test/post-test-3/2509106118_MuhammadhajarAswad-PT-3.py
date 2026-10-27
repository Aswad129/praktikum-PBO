from abc import ABC, abstractmethod

class User(ABC):
    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_user = 0
    status = "aktif"
    peran = "user"

    def __init__(self, id_user, nama, username, password):
        self.id_user = id_user
        self.nama = nama
        self._username = username
        self.__password = password
        User.total_user += 1
        self._status_akun = "aktif"


    @abstractmethod
    def tampilkan_data(self):
        pass

    @abstractmethod
    def aksi_utama(self):
        pass


    def jalankan(self):
        print(f"\nSelamat datang di {self.nama_aplikasi}")
        print(f"Menjalankan aplikasi sebagai {self.peran}")
        self.tampilkan_data()
        self.aksi_utama()


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if password_baru == "":
            raise ValueError("Password tidak boleh kosong.")
        if len(password_baru) < 6:
            raise ValueError("Password harus minimal 6 karakter!")

        self.__password = password_baru
        print("Password berhasil di ubah!")


    @staticmethod
    def validasi_username(username):
        if username == "":
            return False
        if " " in username:
            return False
        return True


class Penghuni(User):
    peran = "penghuni"

    def __init__(self, id_user, nama, username, password, nomor_kamar):
        super().__init__(id_user, nama, username, password)
        self.nomor_kamar = nomor_kamar
        self.kamar = None

    def tampilkan_data(self):
        print("===== Data Penghuni =====")
        print("ID Penghuni  :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self._username)
        print("Nomor Kamar  :", self.nomor_kamar)
        print("Status Akun  :", self._status_akun)


    def pesan_kamar(self):
        print(self.nama, "Dapat melakukan Pemesanan kamar kost")

    def aksi_utama(self):
        self.pesan_kamar()

    @classmethod
    def dari_data(cls, data):
        return cls(
            data["id_user"],
            data["nama"],
            data["username"],
            data["password"],
            data["nomor_kamar"]
        )


class Admin(User):
    peran = "admin"

    def __init__(self, id_user, nama, username, password, hak_akses):
        super().__init__(id_user, nama, username, password)
        self.hak_akses = hak_akses
        self.daftar_kamar = []

    def tampilkan_data(self):
        print("====== Data Admin ======")
        print("ID Admin     :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self._username)
        print("Hak Akses    :", self.hak_akses)
        print("Status Akun  :", self._status_akun)


    def kelola_kamar(self):
        print(self.nama, "Sedang mengelola kamar kost")

    def aksi_utama(self):
        self.kelola_kamar()

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)
        print(f"Kamar {kamar.nomor_kamar} Berhasil di tambahkan ke daftar kelola admin")

    def tampilkan_daftar_kamar(self):
        print("\n===== Daftar Kamar Kelola Admin =====")

        for kamar in self.daftar_kamar:
            print(f"{kamar.id_kamar} - {kamar.nomor_kamar} - {kamar.status}")

    def __len__(self):
        return len(self.daftar_kamar)

    @classmethod
    def dari_data(cls, data):
        return cls(
            data["id_user"],
            data["nama"],
            data["username"],
            data["password"],
            data["hak_akses"]
        )


class Kamar:
    nama_kost = "Kost LUKI"
    total_kamar = 0
    lokasi_kost = "samarinda"


    def __init__(self, id_kamar, nomor_kamar, harga, fasilitas, status="Tersedia"):
        self.id_kamar = id_kamar
        self.nomor_kamar = nomor_kamar
        self.__harga = harga
        self.fasilitas = fasilitas
        self.status = status
        Kamar.total_kamar += 1

    def tampilkan_kamar(self):
        print("\n===== Data Kamar =====")
        print("ID Kamar     :", self.id_kamar)
        print("Nomor Kamar  :", self.nomor_kamar)
        print("Harga        : Rp", self.__harga)
        print("Fasilitas    :", self.fasilitas)
        print("Status       :", self.status)

    def ubah_status(self, status_baru):
        status_valid = [
            "Tersedia",
            "Terisi",
            "Dalam maintenance"
        ]

        if status_baru not in status_valid:
            print("Status tidak valid")
            return

        self.status = status_baru
        print("Status kamar berhasil di ubah")

    def deskripsi(self):
        return f"Kamar {self.nomor_kamar} Rp {self.__harga} {self.status}"

    def __str__(self):
        return f"Kamar {self.nomor_kamar} Rp {self.__harga}"

    def __lt__(self, other):
        return self.__harga < other.harga

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga harus lebih dari 0!")

        self.__harga = harga_baru
        print("Harga Kamar Berhasil di Ubah")

    @classmethod
    def dari_data(cls, data):
        return cls(
            data["id_kamar"],
            data["nomor"],
            data["harga"],
            data["fasilitas"],
            data["status"]
        )

    @staticmethod
    def validasi_harga(harga):
        return harga > 0



class Pembayaran:
    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_pembayaran = 0
    mata_uang = "Rupiah"

    def __init__(self, id_pembayaran, pemesanan, jumlah, metode):
        self.id_pembayaran = id_pembayaran
        self.pemesanan = pemesanan
        self.__jumlah = jumlah
        self.metode = metode
        self.__status = "Belum Lunas"
        Pembayaran.total_pembayaran += 1


    def tampilkan_pembayaran(self):
        print("\n===== Data Pembayaran =====")
        print("ID Pembayaran :", self.id_pembayaran)
        print("Pelanggan     :", self.pemesanan.user.nama)
        print("Jumlah        : Rp", self.__jumlah)
        print("Metode        :", self.metode)
        print("Status        :", self.__status)

    def konfirmasi_pembayaran(self):
        self.__status = "Lunas"
        print("Pembayaran Berhasil di Konfirmasi")


    def deskripsi(self):
        return f"Pembayaran {self.id_pembayaran} Rp {self.__jumlah} {self.metode} {self.__status}"

    def __add__(self, other):
        return self.__jumlah + other.jumlah

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru <= 0:
            raise ValueError("Jumlah Pembayaran Harus Lebih dari 0!")
        self.__jumlah = jumlah_baru
        print("Jumlah pembayaran berhasil di ubah")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        status_valid = ["Belum Lunas", "Lunas"]

        if status_baru not in status_valid:
            raise ValueError("Status pembayaran tidak valid!")
        self.__status = status_baru

    @classmethod
    def dari_data(cls, data, pemesanan):
        return cls(
            data["id_pembayaran"],
            pemesanan,
            data["jumlah"],
            data["metode"]
        )

    @staticmethod
    def validasi_jumlah(jumlah):
        return jumlah > 0



class Pemesanan:
    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_pemesanan = 0
    status_default = "Menunggu"

    def __init__(self, id_pemesanan, user, kamar, tanggal):
        self.id_pemesanan = id_pemesanan
        self.user = user
        self.kamar = kamar
        self.tanggal = tanggal
        self.__status = "Menunggu"
        Pemesanan.total_pemesanan += 1

        self.pembayaran = None

    def tampilkan_pemesanan(self):
        print("\n===== Data Pemesanan =====")
        print("ID Pemesanan :", self.id_pemesanan)
        print("Pelanggan    :", self.user.nama)
        print("Kamar        :", self.kamar.nomor_kamar)
        print("Tanggal      :", self.tanggal)
        print("Status       :", self.__status)

    def konfirmasi(self):
        self.__status = "Dikonfirmasi"
        self.kamar.status = "Terisi"
        print("Pemesanan berhasil dikonfirmasi.")

    def tolak(self):
        self.__status = "Ditolak"
        print("Pemesanan ditolak.")

    def buat_pembayaran(self, id_pembayaran, metode):
        self.pembayaran = Pembayaran(
            id_pembayaran,
            self,
            self.kamar.harga,
            metode
        )
        print(f"Pembayaran untuk pemesanan {self.id_pemesanan} berhasil dibuat")


    def deskripsi(self):
        return f"Pemesanan {self.id_pemesanan} {self.user.nama} Kamar {self.kamar.nomor_kamar} {self.__status}"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        status_valid = [
            "Menunggu",
            "Dikonfirmasi",
            "Ditolak"
        ]
        if status_baru not in status_valid:
            raise ValueError("Status pemesanan tidak valid!")
        self.__status = status_baru


    @classmethod
    def dari_data(cls, data, user, kamar):
        return cls(
            data["id_pemesanan"],
            user,
            kamar,
            data["tanggal"]
        )

    @staticmethod
    def validasi_tanggal(tanggal):
        bagian = tanggal.split("-")

        if len(bagian) != 3:
            return False

        if len(bagian[0]) != 4:
            return False

        if len(bagian[1]) != 2:
            return False

        if len(bagian[2]) != 2:
            return False

        return True


def cetak_ringkasan(objek):
    print(objek.deskripsi())


print("===== BUKTI ABSTRAKSI =====")
try:
    user_abstrak = User("U000", "Test", "test", "test123")
except TypeError as error:
    print("TypeError:", error)


print("\n===== PEMBUATAN OBJEK =====")

penghuni1 = Penghuni("P001", "Siti Aminah", "siti", "siti123", "K001")
penghuni2 = Penghuni("P002", "Joko Widodo", "joko", "joko123", "K002")

admin1 = Admin("A001", "Budiono Siregar", "Diono", "diono123", "Penuh")
admin2 = Admin("A002", "Adi Putra", "Putra", "adi123", "Penuh")

kamar1 = Kamar("K001", "101", 1500000, ["AC", "Kamar Mandi Dalam", "Lemari"])
kamar2 = Kamar("K002", "102", 1200000, ["Kipas Angin", "Kamar Mandi Luar", "Lemari", "Meja Belajar"])

penghuni1.kamar = kamar1
penghuni2.kamar = kamar2

print("Total user   :", User.total_user)
print("Total kamar  :", Kamar.total_kamar)


print("\n===== POLIMORFISME VIA PEWARISAN =====")

daftar_akun = [penghuni1, penghuni2, admin1, admin2]

for akun in daftar_akun:
    akun.jalankan()


print("\n===== AGREGASI =====")

admin1.tambah_kamar(kamar1)
admin1.tambah_kamar(kamar2)
admin1.tampilkan_daftar_kamar()


print("\n===== ASOSIASI & KOMPOSISI =====")

pemesanan1 = Pemesanan("PM001", penghuni1, kamar1, "2024-06-01")
pemesanan2 = Pemesanan("PM002", penghuni2, kamar2, "2024-06-02")

pemesanan1.buat_pembayaran("B001", "Transfer")
pemesanan2.buat_pembayaran("B002", "Cash")

pemesanan1.tampilkan_pemesanan()
pemesanan1.pembayaran.tampilkan_pembayaran()


print("\n===== DUCK TYPING =====")

for objek in [kamar1, pemesanan1, pemesanan1.pembayaran]:
    cetak_ringkasan(objek)


print("\n===== OPERATOR OVERLOADING =====")

kamar3 = Kamar.dari_data({
    "id_kamar": "K003",
    "nomor": "B01",
    "harga": 750000,
    "fasilitas": "WiFi, Kasur",
    "status": "Tersedia"
})

print("__str__ :", kamar1)
print("__lt__  : kamar2 < kamar1 =", kamar2 < kamar1)
print("sorted  :", [str(k) for k in sorted([kamar1, kamar2, kamar3])])
print("__len__ : kamar dikelola admin1 =", len(admin1))
print("__add__ : total pembayaran Rp", pemesanan1.pembayaran + pemesanan2.pembayaran)


print("\n===== INSTANCE METHOD =====")

kamar1.ubah_status("Terisi")
pemesanan1.konfirmasi()
pemesanan1.pembayaran.konfirmasi_pembayaran()
pemesanan1.tampilkan_pemesanan()
pemesanan1.pembayaran.tampilkan_pembayaran()


print("\n===== CLASS METHOD =====")

penghuni3 = Penghuni.dari_data({
    "id_user": "P003",
    "nama": "Citra",
    "username": "citra",
    "password": "citra123",
    "nomor_kamar": "B01"
})
penghuni3.tampilkan_data()

kamar3.tampilkan_kamar()


print("\n===== STATIC METHOD =====")

print("Validasi harga Rp800000     :", Kamar.validasi_harga(800000))
print("Validasi harga Rp0          :", Kamar.validasi_harga(0))
print("Validasi username 'andi'    :", User.validasi_username("andi"))
print("Validasi username ''        :", User.validasi_username(""))
print("Validasi tanggal 2026-10-06 :", Pemesanan.validasi_tanggal("2026-10-06"))
print("Validasi jumlah Rp500000    :", Pembayaran.validasi_jumlah(500000))


print("\n===== GETTER =====")

print("Password Penghuni :", penghuni1.password)
print("Harga Kamar       :", kamar1.harga)
print("Status Pesanan    :", pemesanan1.status)
print("Jumlah Bayar      :", pemesanan1.pembayaran.jumlah)


print("\n===== SETTER =====")

kamar1.harga = 1600000

try:
    kamar1.harga = -500000
except ValueError as error:
    print("ValueError:", error)

try:
    penghuni1.password = "abc"
except ValueError as error:
    print("ValueError:", error)
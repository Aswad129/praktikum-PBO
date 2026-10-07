class User:
    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_user = 0
    status = "aktif"

    def __init__(self, id_user, nama, username, password):
        self.id_user = id_user
        self.nama = nama
        self._username = username
        self.__password = password
        User.total_user +=1
        self._status_akun = "aktif"


    def tampilkan_data(self):
        print("\n===== Data User =====")
        print("ID User      :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self._username)
        print("Status Akun  :", self._status_akun)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if password_baru == "":
            raise ValueError("Password tidak boleh kosong!")
        
        if len(password_baru) < 6:
            raise ValueError("Password harus memiliki panjang minimal 6 karakter!")
        
        self.__password = password_baru
        print("Password anda berhasil diubah.")


    @classmethod
    def dari_data(cls, data):
        return cls(data["id_user"], 
            data["nama"], 
            data["username"], 
            data["password"])

    @staticmethod
    def validasi_username(username):
        if username == "":
            return False
    
        if " " in username:
            return False
        return True


class Penghuni(User):
    def __init__(self,id_user,nama,username,password,nomor_kamar):
        super().__init__(id_user, nama, username, password)
        self.nomor_kamar = nomor_kamar


    def tampilkan_data(self):
        print("\n===== Data Penghuni =====")
        print("ID Penghuni  :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self._username)
        print("Nomor Kamar  :", self.nomor_kamar)
        print("Status Akun  :", self._status_akun)


    def pesan_kamar(self):
        print(self.nama, "dapat melakukan pemesanan kamar.")

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
    def __init__(self, id_user, nama, username, password, hak_akses):
        super().__init__(id_user, nama, username, password)
        self.hak_akses = hak_akses


        self.daftar_kamar = []

    def tampilkan_data(self):
        print("\n====== Data Admin ======")
        print("ID Admin     :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self._username)
        print("Hak Akses    :", self.hak_akses)
        print("Status Akun  :", self._status_akun)


    def kelola_kamar(self):
        print(self.nama, "sedang mengelola kamar kost.")


    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)
        print("kamar", kamar.nomor_kamar, "berhasil di tambahkan ke daftar kelolaan admin")

    def tampilkan_daftar_kamar(self):
        print("\n===== Daftar Kamar Kelola Admin =====")

        for kamar in self.daftar_kamar:
            print(kamar.id_kamar, "-", kamar.nomor_kamar, "-", kamar.status)


class Kamar :
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
            print("Status tidak valid!!")
            return

        self.status = status_baru
        print("Status kamar berhasil di ubah")


    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga harus lebih dari 0!")

        self.__harga = harga_baru
        print("harga kamar berhasil di ubah")


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
        self.__status = "Belum Lunas"
        self.metode = metode
        Pembayaran.total_pembayaran +=1

    def tampilkan_pembayaran(self):
        print("\n===== Data Pembayaran =====")
        print("ID Pembayaran :", self.id_pembayaran)
        print("Pelanggan     :", self.pemesanan.user.nama)
        print("Jumlah        : Rp", self.__jumlah)
        print("Metode        :", self.metode)
        print("Status        :", self.__status)

    def konfirmasi_pembayaran(self):
        self.__status = "Lunas"
        print("Pembayaran berhasil dikonfirmasi")


    @property
    def jumlah(self):
        return self.__jumlah


    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru <= 0:
            raise ValueError("Jumlah pembayaran harus lebih dari 0!")

        self.__jumlah = jumlah_baru
        print("Jumlah pembayaran berhasil diubah")


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        status_valid = ["Belum lunas", "Lunas"]

        if status_baru not in status_valid:
            raise ValueError("Status pembayaran tidak valid")
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



class Pemesanan :
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

        self.Pembayaran = None

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

        print("Pembayaran untuk pemesanan", self.id_pemesanan, "berhasil dibuat.")


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




user1 = User(
    "U001",
    "Muhammad Andi",
    "andi",
    "andi123"
)

user2 = User(
    "U002",
    "Budiono",
    "budi",
    "budi123"
)

user1.tampilkan_data()
user2.tampilkan_data()


penghuni1 = Penghuni(
    "P001",
    "Siti Aminah",
    "siti",
    "siti123",
    "K001"
)

penghuni2 = Penghuni(
    "P002",
    "Joko Widodo",
    "joko",
    "joko123",
    "K002"
)

penghuni1.tampilkan_data()
penghuni2.tampilkan_data()

penghuni1.pesan_kamar()


admin1 = Admin(
    "A001",
    "Budiono Siregar",
    "Diono",
    "diono123",
    "Penuh"
)

admin1.tampilkan_data()
admin1.kelola_kamar()


admin2 = Admin(
    "A002",
    "Adi Putra",
    "Putra",
    "adi123",
    "Penuh"
)

admin1.tampilkan_data() 
admin2.tampilkan_data()

admin1.kelola_kamar()

kamar1 = Kamar(
    "K001",
    "101",
    1500000,
    ["AC", "Kamar Mandi Dalam", "Lemari"]
)

kamar2 = Kamar(
    "K002",
    "102",
    1200000,
    ["Kipas Angin", "Kamar Mandi Luar", "Lemari", "Meja Belajar"]
) 

kamar1.tampilkan_kamar()
kamar2.tampilkan_kamar()


penghuni1.kamar = kamar1
penghuni2.kamar = kamar2


print("\n===== Agregasi =====")

admin1.tambah_kamar(kamar1)
admin1.tambah_kamar(kamar2)

admin1.tampilkan_daftar_kamar()

pemesanan1 = Pemesanan(
    "PM001",
    penghuni1,
    kamar1,
    "2024-06-01"
)

pemesanan2 = Pemesanan(
    "PM002",
    penghuni2,
    kamar2,
    "2024-06-02"
)

pemesanan1.tampilkan_pemesanan()
pemesanan2.tampilkan_pemesanan()

print("\n===== Composition =====")

pemesanan1.buat_pembayaran(
    "B001",
    "Transfer"
)

pemesanan2.buat_pembayaran(
    "B002",
    "Cash"
)

pemesanan1.pembayaran.tampilkan_pembayaran()
pemesanan2.pembayaran.tampilkan_pembayaran()


print("\n===== INSTANCE METHOD =====")

kamar1.ubah_status("Terisi")
kamar1.tampilkan_kamar()

pemesanan1.konfirmasi()
pemesanan1.tampilkan_pemesanan()

pemesanan1.pembayaran.konfirmasi_pembayaran()
pemesanan1.pembayaran.tampilkan_pembayaran()


print("\n===== CLASS METHOD =====")

data_kamar = {
    "id_kamar": "K003",
    "nomor": "B01",
    "harga": 750000,
    "fasilitas": "WiFi, Kasur",
    "status": "Tersedia"
}

kamar3 = Kamar.dari_data(data_kamar)

print("Object kamar berhasil dibuat melalui class method.")
kamar3.tampilkan_kamar()


data_user = {
    "id_user": "U003",
    "nama": "Citra",
    "username": "citra",
    "password": "citra123"
}

user3 = User.dari_data(data_user)

print("\nObject user berhasil dibuat melalui class method.")
user3.tampilkan_data()


print("\n===== STATIC METHOD =====")

print(
    "Validasi harga Rp800000 :",
    Kamar.validasi_harga(800000)
)

print(
    "Validasi harga Rp0       :",
    Kamar.validasi_harga(0)
)

print(
    "Validasi username 'andi' :",
    User.validasi_username("andi")
)

print(
    "Validasi username ''     :",
    User.validasi_username("")
)

print(
    "Validasi tanggal 2026-10-06 :",
    Pemesanan.validasi_tanggal("2026-10-06")
)

print(
    "Validasi jumlah Rp500000 :",
    Pembayaran.validasi_jumlah(500000)
)

print("\n===== GETTER =====")

print(
    "Password User :",
    user1.password
)

print(
    "Harga Kamar   :",
    kamar1.harga
)

print(
    "Status Pesanan:",
    pemesanan1.status
)

print(
    "Jumlah Bayar  :",
    pemesanan1.pembayaran.jumlah
)


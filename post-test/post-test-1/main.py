class User :
    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_user = 0
    status = "Aktif"

    def __init__(self, id_user, nama, username, password):
        self.id_user = id_user
        self.nama = nama
        self.username = username
        self.__password = password
        User.total_user += 1


    def tampilkan_data(self):
        print("\n===== Data User =====")
        print("ID User      :", self.id_user)
        print("Nama         :", self.nama)
        print("Username     :", self.username)


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


class Admin:
    nama_role = "Admin"
    total_admin = 0
    hak_akses = "Penuh" 

    def __init__(self, id_admin, nama, username, password):
        self.id_admin = id_admin
        self.nama = nama
        self.username = username
        self.__password = password
        Admin.total_admin += 1

    def tampilkan_data(self):
        print("\n===== Data Admin =====")
        print("ID Admin     :", self.id_admin)
        print("Nama         :", self.nama)
        print("Username     :", self.username)
        print("Role         :", Admin.nama_role)

    def kelola_kamar(self):
        print(self.nama, "sedang mengelola kamar kost.")

    def konfirmasi_pemesanan(self):
        print(self.nama, "dapat mengkonfirmasi pemesanan kamar kost.")


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
        return cls(data["id_admin"], 
                   data["nama"], 
                   data["username"], 
                   data["password"])

    @staticmethod
    def validasi_username(username):
        return username != "" and " " not in username



class Kamar :
    nama_kost = "Kost LUKI"
    total_kamar = 0
    lokasi_kost = "Samarinda"

    def __init__(self, id_kamar, nomor_kamar, harga, fasilitas, status="tersedia"):
        self.id_kamar = id_kamar
        self.nomor_kamar = nomor_kamar
        self.__harga = harga
        self.fasilitas = fasilitas
        self.status = status
        Kamar.total_kamar += 1


    def tampilkan_data(self):
        print("\n===== Data Kamar =====")
        print("ID Kamar     :", self.id_kamar)
        print("Nomor Kamar  :", self.nomor_kamar)
        print("Harga        : Rp ", self.__harga)
        print("Fasilitas    :", self.fasilitas)
        print("Status       :", self.status)

    def ubah_status(self, status_baru):
        status_valid = ["tersedia", "terisi", "dalam perbaikan"]

        if status_baru not in status_valid:
            print("Status tidak valid!")
            return

        self.status = status_baru
        print("Status kamar berhasil diubah")

    @property
    def harga(self):
        return self.__harga


    @harga.setter
    def harga(self, harga_baru):

        if harga_baru <= 0:
            raise ValueError("harga harus lebih dari 0!")

        self.__harga = harga_baru
        print("Harga kamar berhasil di ubah")


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


    def tampilkan_pemesanan(self):
        print("\n===== DATA PESANAN =====")
        print("ID Pemesanan        :", self.id_pemesanan)
        print("Pelanggan           :", self.user.nama)
        print("Kamar               :", self.kamar.nomor_kamar)
        print("Tanggal             :", self.tanggal)
        print("Status              :", self.__status)


    def konfirmasi(self):
        self.__status = "Dikonfirmasi"
        self.kamar.status = "Terisi"
        print("Pemesanan berhasil di konfirmasi")

    def tolak(self):
        self.__status = "Ditolak"
        print("Pemesanan di tolak")


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
            raise ValueError("Status pemesanan tidak valid")

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

        if len(bagian[0]) != 4:
            return False

        if len(bagian[1]) != 2:
            return False

        if len(bagian[2]) != 2:
            return False

        return True



class Pembayaran :

    nama_aplikasi = "Sistem Manajemen dan Pemesanan Kamar Kost"
    total_pembayaran = 0
    mata_uang = "Rupiah"

    def __init__(self, id_pembayaran, pemesanan, jumlah, metode):
        self.id_pembayaran = id_pembayaran
        self.pemesanan = pemesanan
        self.__jumlah = jumlah
        self.__status = "Belum lunas"
        self.metode = metode
        Pembayaran.total_pembayaran += 1

    def tampilkan_pembayaran(self):
        print("\n===== DATA PEMBAYARAN =====") 
        print("ID Pembayaran :", self.id_pembayaran) 
        print("Pelanggan :", self.pemesanan.user.nama) 
        print("Jumlah : Rp", self.__jumlah) 
        print("Metode :", self.metode) 
        print("Status :", self.__status)

    def konfirmasi_pembayaran(self):
        self.__status = "Lunas"
        print("Pembayaran berhasil di konfirmasi")

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru <= 0:
            raise ValueError("Jumlah pembayaran harus lebih dari 0")

        self.__jumlah = jumlah_baru

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        status_valid = [
            "Belum Lunas",
            "Lunas"
        ]

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



        #main pro

user1 = User(
    "U001",
    "Muhammad Andi",
    "andi",
    "123andi"

)

user2 = User(
    "U002",
    "Budiono",
    "budi",
    "budi123"
)

user1.tampilkan_data()
user2.tampilkan_data()



admin1 = Admin(
    "A001",
    "Pak Ahmad",
    "ahmadd",
    "ahmad123"

)

admin2 = Admin(
    "A002",
    "Budiana",
    "budi",
    "123budi"
)

admin1.tampilkan_data()
admin2.tampilkan_data()

admin1.kelola_kamar()
admin2.konfirmasi_pemesanan()



kamar1 = Kamar(
    "K001",
    "A01",
    800000,
    "WiFi, Kasur, Lemari"
)

kamar2 = Kamar(
    "K002",
    "A02",
    900000,
    "WiFi, AC, Kasur, Lemari"
)

kamar1.tampilkan_data()
kamar2.tampilkan_data()


pemesanan1 = Pemesanan(
    "P001",
    user1,
    kamar1,
    "2026-09-22"
)

pemesanan2 = Pemesanan(
    "P002",
    user2,
    kamar2,
    "2026-09-23"
)

pemesanan1.tampilkan_pemesanan()
pemesanan2.tampilkan_pemesanan()



pembayaran1 = Pembayaran(
    "B001",
    pemesanan1,
    800000,
    "Transfer"
)

pembayaran2 = Pembayaran(
    "B002",
    pemesanan2,
    900000,
    "Cash"
)

pembayaran1.tampilkan_pembayaran()
pembayaran2.tampilkan_pembayaran()


print("\n===== INSTANCE METHOD =====")

kamar1.ubah_status("terisi")
kamar1.tampilkan_data()

pemesanan1.konfirmasi()
pemesanan1.tampilkan_pemesanan()

pembayaran1.konfirmasi_pembayaran()
pembayaran1.tampilkan_pembayaran()


print("\n\n===== CLASS METHOD =====")

data_kamar = {
    "id_kamar": "K003",
    "nomor": "B01",
    "harga": 750000,
    "fasilitas": "WiFi, Kasur",
    "status": "Tersedia"
}

kamar3 = Kamar.dari_data(data_kamar)
print("Object berhasil di buat")
kamar3.tampilkan_data()

data_user = {
    "id_user": "U003",
    "nama": "Citra",
    "username": "citra",
    "password": "citra123"
}

user3 = User.dari_data(data_user)
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
    "Validasi tanggal 2026-09-22 :",
    Pemesanan.validasi_tanggal("2026-09-22")
)

print(
    "Validasi jumlah Rp500000 :",
    Pembayaran.validasi_jumlah(500000)
)


print("\n===== GETTER / PROPERTY =====")

print("Harga kamar 1 :", kamar1.harga)
print("Password user 1 :", user1.password)
print("Jumlah pembayaran 1 :", pembayaran1.jumlah)
print("Status pembayaran 1 :", pembayaran1.status)


print("\n===== SETTER DATA VALID =====")

try:
    kamar1.harga = 850000
    print("Harga baru kamar 1 :", kamar1.harga)

    user1.password = "passwordbaru"
    print("Password berhasil diperbarui.")

    pembayaran1.jumlah = 850000
    print("Jumlah pembayaran baru :", pembayaran1.jumlah)

except ValueError as e:
    print("Error:", e)


print("\n\n===== SETTER DATA TIDAK VALID =====")


try:
    kamar1.harga = -500000

except ValueError as e:
    print("Validasi harga:", e)

try:
    user1.password = "123"

except ValueError as e:
    print("Validasi password:", e)

try:
    pembayaran1.jumlah = -100000

except ValueError as e:
    print("Validasi pembayaran:", e)






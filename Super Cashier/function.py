# Import modul tabulate untuk menampilkan data dalam bentuk tabel yang rapi
from tabulate import tabulate

# Membuat class Transaction untuk mengelola semua operasi transaksi
class Transaction:

    """
    Kelas Transaction digunakan untuk mengelola sistem kasir sederhana.
    Menyimpan data item yang dibeli customer dan menyediakan berbagai
    method untuk menambah, menghapus, memperbarui, serta menghitung total harga.
    """

    # Inisialisasi dictionary kosong sebagai keranjang belanja
    def __init__(self):
        """
        Inisialisasi objek Transaction baru dengan keranjang kosong.
        """
        self.Keranjang = {}

    # Menambahkan item baru ke dalam keranjang
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        """
        Menambahkan item baru ke dalam keranjang belanja.

        Args:
            nama_item (str): Nama item yang ingin ditambahkan.
            jumlah_item (int): Jumlah item yang dibeli.
            harga_per_item (int): Harga per item.

        Returns:
            None
        """
        # Menyimpan data item dalam bentuk dictionary bersarang
        self.Keranjang[nama_item] = {
            'jumlah item': jumlah_item, 
            'harga/item': harga_per_item, 
            'total harga': harga_per_item * jumlah_item
        }

    # Mengubah nama item yang sudah ada
    def update_item_name(self, nama_item, update_nama_item):
        """
        Mengubah nama item yang sudah ada di dalam keranjang.

        Args:
            nama_item (str): Nama item yang ingin diubah.
            update_nama_item (str): Nama baru untuk item tersebut.

        Returns:
            None
        """
        # Mengecek apakah item ada dalam keranjang
        if nama_item in self.Keranjang:
            # pop untuk memindahkan data lama ke nama baru
            self.Keranjang[update_nama_item] = self.Keranjang.pop(nama_item)
        else:
            print("Nama item tidak ditemukan")

    # Mengubah jumlah item tertentu
    def update_item_qty(self, nama_item, update_jumlah_item):
        """
        Mengubah jumlah item tertentu di dalam keranjang.

        Args:
            nama_item (str): Nama item yang ingin diperbarui.
            update_jumlah_item (int): Jumlah item baru yang ingin disimpan.

        Returns:
            None
        """
        # Mengecek apakah item ada
        if nama_item in self.Keranjang:
            # Update jumlah item
            self.Keranjang[nama_item]['jumlah item'] = update_jumlah_item
            # Update total harga sesuai jumlah baru
            self.Keranjang[nama_item]['total harga'] = (
                self.Keranjang[nama_item]['harga/item'] * update_jumlah_item
            )
        else:
            print("Nama item tidak ditemukan")

    # Mengubah harga per item
    def update_item_price(self, nama_item, update_harga_item):
        """
        Mengubah harga per item untuk item tertentu.

        Args:
            nama_item (str): Nama item yang ingin diperbarui.
            update_harga_item (int): Harga baru per item.

        Returns:
            None
        """
        if nama_item in self.Keranjang:
            # Update harga per item
            self.Keranjang[nama_item]['harga/item'] = update_harga_item
            # Hitung ulang total harga berdasarkan harga baru
            self.Keranjang[nama_item]['total harga'] = (
                self.Keranjang[nama_item]['jumlah item'] * update_harga_item
            )
        else:
            print("Nama item tidak ditemukan")
    
    # Menghapus item dari keranjang
    def delete_item(self, nama_item):
        """
        Menghapus item tertentu dari keranjang.

        Args:
            nama_item (str): Nama item yang ingin dihapus.

        Returns:
            None
        """
        # Mengecek apakah item ada dalam keranjang
        if nama_item in self.Keranjang:
            del self.Keranjang[nama_item]
        else:
            print("Nama item tidak ditemukan")
    
    # Menghapus semua isi keranjang (reset transaksi)
    def reset_transaction(self):
        """
        Menghapus seluruh isi keranjang dan mengatur ulang transaksi.

        Returns:
            None
        """
        self.Keranjang = {}

    # Mengecek apakah input item valid dan menampilkan isi keranjang
    def check_order(self):
        """
        Menampilkan daftar item yang ada di dalam keranjang
        dalam format tabel sederhana.

        Returns:
            None
        """
        # Validasi setiap item di keranjang
        for key, value in self.Keranjang.items():
            if len(key) <=0 or value['jumlah item'] <= 0 or value['harga/item'] <= 0:
                print("Terdapat kesalahan pada item:", key)
            else:
                pass

        # Mengonversi dictionary menjadi list untuk ditampilkan dalam tabel
        keranjang_list = [[key,]+list(value.values()) for key,value in self.Keranjang.items()]

        # Menambahkan nomor urut di depan tabel
        No = 1
        keranjang_akhir = []
        for x in keranjang_list:
            keranjang_akhir.append([No,]+x)
            No += 1

        # Header tabel
        head = ["No", "Nama Item", "Jumlah Item", "Harga/item", "Total Harga"]

        # Menampilkan tabel menggunakan tabulate
        table = tabulate(keranjang_akhir, headers=head, tablefmt='github', stralign='center')
        print(table)

    # Menghitung total harga seluruh item di keranjang
    def total_price(self):
        """
        Menghitung dan menampilkan total harga seluruh item di dalam keranjang.
        Jika total pembelian mencapai batas tertentu, akan diterapkan diskon otomatis.

        Returns:
            None
        """
        total_harga = 0
        # Menjumlahkan seluruh total harga item
        for x in self.Keranjang.values():
            total_harga += x['total harga']
        if total_harga >500_000:
            total_harga = total_harga * 0.9  # Diskon 10%
            print("Selamat! Anda mendapatkan diskon 10% karena total belanja di atas 500.000")
        elif total_harga >300_000:
            total_harga = total_harga * 0.92  # Diskon 8%
            print("Selamat! Anda mendapatkan diskon 8% karena total belanja di atas 300.000")
        elif total_harga >200_000:
            total_harga = total_harga * 0.95  # Diskon 5%
            print("Selamat! Anda mendapatkan diskon 5% karena total belanja di atas 200.000")
        print("Total harga keseluruhan adalah:", total_harga)


# Mengimpor semua function dan class dari file function.py
from function import *

# Membuat instance/objek transaksi
trnsct123 = Transaction()

# Fungsi utama untuk menampilkan menu interaktif
def menu():
    # Tampilan awal menu
    print("-" * 50)
    print("Selamat datang di program super cashier")
    print("Silahkan pilih menu yang tersedia")
    print("1. Tambah item")
    print("2. Update nama item") 
    print("3. Update jumlah item")
    print("4. Update harga item")
    print("5. Hapus item")
    print("6. Reset transaksi")
    print("7. Cek pesanan")
    print("8. Total harga")
    print("9. Keluar")
    print("-" * 50)

    # Input pilihan user
    pilihan = str(input("Masukkan pilihan Anda (1-9): "))

    # Menambah item ke keranjang
    if pilihan == '1':
        nama_item = input("Masukkan nama item: ")
        jumlah_item = int(input("Masukkan jumlah item: "))
        harga_per_item = int(input("Masukkan harga per item: "))
        trnsct123.add_item(nama_item, jumlah_item, harga_per_item)
        menu()

    # Mengupdate nama item
    if pilihan == '2':
        nama_item = input("Masukkan nama item yang ingin diubah: ")
        nama_item_baru = input("Masukkan nama item baru: ")
        trnsct123.update_item_name(nama_item, nama_item_baru)
        input() # Pause agar user bisa membaca hasil
        menu()

    # Mengupdate jumlah item
    if pilihan == '3':
        nama_item = input("Masukkan nama item yang ingin diubah: ")
        jumlah_item_baru = int(input("Masukkan jumlah item baru: "))
        trnsct123.update_item_qty(nama_item, jumlah_item_baru)
        menu()

    # Mengupdate harga item
    if pilihan == '4':
        nama_item = input("Masukkan nama item yang ingin diubah: ")
        harga_item_baru = int(input("Masukkan harga item baru: "))
        trnsct123.update_item_price(nama_item, harga_item_baru)
        menu()

    # Menghapus item dari keranjang
    if pilihan == '5':
        nama_item = input("Masukkan nama item yang ingin dihapus: ")
        trnsct123.delete_item(nama_item)
        menu()

    # Mereset transaksi (menghapus semua item)
    if pilihan == '6':
        trnsct123.reset_transaction()
        print("Semua item telah dihapus dari keranjang.")
        input("Tekan Enter untuk kembali ke menu...")
        menu()

    # Mengecek pesanan
    if pilihan == '7':
        trnsct123.check_order()
        input("Tekan Enter untuk kembali ke menu...")
        menu()

    # Menghitung total harga
    if pilihan == '8':
        trnsct123.check_order()
        trnsct123.total_price()
        input("Tekan Enter untuk kembali ke menu...")
        menu()

    # Keluar dari program
    if pilihan == '9':
        print("Terima kasih telah menggunakan program ini.")
        print("Sampai jumpa lagi!")
        exit()


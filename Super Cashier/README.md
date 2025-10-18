# 💸 Super Cashier

## 🧠 Background Project

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia.  
Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu membuat sistem kasir **self-service** di supermarket miliknya.  
Dengan sistem ini, customer dapat langsung memasukkan item yang dibeli, jumlah item, serta harga per item tanpa bantuan kasir.  

Tujuan utamanya agar proses transaksi menjadi lebih efisien dan meminimalkan kesalahan input manual.  
Selain itu, sistem ini juga memungkinkan pelanggan yang berada jauh dari kota tempat supermarket berdiri untuk tetap melakukan pembelian secara daring.  

Setelah melakukan riset, Andi menyadari bahwa ia membutuhkan seorang **programmer** untuk merancang sistem kasir self-service tersebut.  
Programmer tersebut bertugas membuat fitur-fitur dasar kasir seperti menambah, mengubah, menghapus, memeriksa, dan menghitung total harga barang — agar sistem kasir self-service dapat berjalan dengan lancar.  

---

## 🎯 Requirements / Objectives

Program **Super Cashier** ini dibuat untuk memenuhi kebutuhan sistem kasir self-service yang efisien dan mudah digunakan.

### Tujuan Utama:
1. Membuat sistem kasir berbasis teks dengan bahasa Python.
2. Menerapkan konsep **Object-Oriented Programming (OOP)**.
3. Menerapkan struktur **modular code** untuk memisahkan fungsi-fungsi utama.
4. Menyediakan fitur:
   - Tambah item
   - Update nama, jumlah, dan harga item
   - Hapus item
   - Reset transaksi
   - Menampilkan daftar pesanan dan total harga

---

## ⚙️ Flowchart Program

Berikut flowchart utama dari sistem **Super Cashier** (berdasarkan hasil rancangan):

![Flowchart Program](Flowchart%20Program.drawio.png)

**Penjelasan singkat:**
1. Program dimulai (Start)
2. Menampilkan menu interaktif
3. User memilih opsi 1–9
4. Setiap pilihan akan menjalankan fungsi berbeda:
   - `1` Add Item  
   - `2` Update Item Name  
   - `3` Update Item Quantity  
   - `4` Update Item Price  
   - `5` Delete Item  
   - `6` Reset Transaction  
   - `7` Check Order  
   - `8` Total Price  
   - `9` Exit
5. Setelah menjalankan fungsi, program kembali ke menu sampai user memilih keluar.

---

## 💻 Demonstrasi Program (Test Case dan Expected Output)

### 🧪 **Test 1 – Menambahkan Item**
Customer ingin menambahkan dua item baru menggunakan method `add_item()`.  
Item yang ditambahkan adalah:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000  
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000  

**Expected Output:**
```
|   No |  Nama Item  |   Jumlah Item |   Harga/item |   Total Harga |
|------|-------------|---------------|--------------|---------------|
|    1 | Ayam Goreng |             2 |        20000 |         40000 |
|    2 | Pasta Gigi  |             3 |        15000 |         45000 |
```

---

### 🧪 **Test 2 – Menghapus Salah Satu Item**
Customer salah membeli salah satu item, yaitu *Pasta Gigi*,  
maka customer menggunakan method `delete_item()`.

**Expected Output:**
```
|   No |  Nama Item  |   Jumlah Item |   Harga/item |   Total Harga |
|------|-------------|---------------|--------------|---------------|
|    1 | Ayam Goreng |             2 |        20000 |         40000 |
Item 'Pasta Gigi' telah dihapus dari keranjang.
```

---

### 🧪 **Test 3 – Reset Semua Item**
Customer merasa semua barang yang dimasukkan salah,  
sehingga ia menggunakan `reset_transaction()` untuk menghapus semua item.

**Expected Output:**
```
Semua item telah dihapus dari keranjang.
```

---

### 🧪 **Test 4 – Menghitung Total Harga**
Setelah Customer selesai berbelanja,  
Customer akan menghitung total harga menggunakan `total_price()`.

Item yang ada di keranjang:
- Ayam Goreng: Qty 2, Harga 20000  
- Pasta Gigi: Qty 3, Harga 15000  
- Mainan Mobil: Qty 1, Harga 200000  
- Mi Instan: Qty 5, Harga 3000  

**Expected Output:**
```
|   No |  Nama Item   |   Jumlah Item |   Harga/item |   Total Harga |
|------|--------------|---------------|--------------|---------------|
|    1 | Ayam Goreng  |             2 |        20000 |         40000 |
|    2 |  Pasta Gigi  |             3 |        15000 |         45000 |
|    3 | Mainan Mobil |             1 |       200000 |        200000 |
|    4 |  Mi Instan   |             5 |         3000 |         15000 |
Total harga keseluruhan adalah: 300000
```

---

## 🚀 Cara Menjalankan Program

Program ini terdiri dari tiga file utama:
```
├── main.py
├── Menu.py
└── function.py
```

### 🧩 1. **Penjelasan File**
- **`function.py`** → Berisi class utama `Transaction` (fungsi logika kasir).
- **`Menu.py`** → Menampilkan menu utama sistem.
- **`main.py`** → File utama yang dijalankan untuk memulai program.

---

### 💡 2. **Langkah Menjalankan Program**
Buka terminal dan ketik:
```bash
python main.py
```
Tampilan menu akan muncul seperti berikut:
```
--------------------------------------------------
Selamat datang di program super cashier
Silahkan pilih menu yang tersedia
1. Tambah item
2. Update nama item
3. Update jumlah item
4. Update harga item
5. Hapus item
6. Reset transaksi
7. Cek pesanan
8. Total harga
9. Keluar
--------------------------------------------------
Masukkan pilihan Anda (1-9):
```

---

### 📋 3. **Contoh Penggunaan Menu**
- **Add Item:** Tambah barang baru.  
- **Update Item Name:** Ubah nama barang.  
- **Update Item Qty:** Ubah jumlah barang.  
- **Update Item Price:** Ubah harga barang.  
- **Delete Item:** Hapus satu item.  
- **Reset Transaction:** Hapus semua item.  
- **Check Order:** Tampilkan daftar belanja.  
- **Total Price:** Hitung total belanja.  
- **Exit:** Keluar dari program.

---

### ⚙️ 4. **Menjalankan Fungsi Secara Langsung (Testing Manual)**
Kamu juga bisa menjalankan fungsi langsung dari `function.py`:
```python
from function import Transaction

# Membuat objek transaksi baru
trns = Transaction()

# Tambah item
trns.add_item("Ayam Goreng", 2, 20000)
trns.add_item("Pasta Gigi", 3, 15000)

# Update jumlah item
trns.update_item_qty("Ayam Goreng", 5)

# Hapus item
trns.delete_item("Pasta Gigi")

# Tampilkan isi keranjang
trns.check_order()

# Hitung total harga
trns.total_price()
```

---

## ✅ Conclusion

Dari hasil pembuatan program **Super Cashier**, diperoleh sistem kasir sederhana yang dapat digunakan oleh pelanggan secara mandiri.  
Program ini memenuhi kebutuhan Andi untuk membuat sistem kasir **self-service**, dengan fitur yang mudah digunakan dan hasil output yang akurat.  

Dengan struktur **modular** dan berbasis **OOP**, program dapat dikembangkan lebih lanjut ke bentuk **GUI (Graphical User Interface)** atau **web application** menggunakan framework seperti Flask atau Django.

---

## 👨‍💻 Identitas

**Nama:** Intifada Afkar Lazain Muhammad  
**Judul Proyek:** Super Cashier  
**Tujuan:** Membuat sistem kasir self-service dengan konsep modular programming  

---

## 📚 Referensi

- [https://github.com/putusetya/LMS-Project](https://github.com/putusetya/LMS-Project)  
- [https://github.com/jovitakurniawan/python-LMS](https://github.com/jovitakurniawan/python-LMS)  
- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)  
- [GitHub Documentation Handbook](https://github.com/jamiebuilds/documentation-handbook)

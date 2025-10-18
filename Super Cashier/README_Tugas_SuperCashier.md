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

## ⚙️ Alur Program (Flowchart)

```
┌────────────────────┐
│ Mulai Program      │
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│ Tampilkan Menu     │
└───────┬────────────┘
        │
        ▼
┌───────────────────────────────┐
│ User memilih menu (1 - 9)     │
└───────┬───────────────────────┘
        │
        ├─► [1] Tambah Item
        ├─► [2] Update Nama Item
        ├─► [3] Update Jumlah Item
        ├─► [4] Update Harga Item
        ├─► [5] Hapus Item
        ├─► [6] Reset Transaksi
        ├─► [7] Cek Pesanan
        ├─► [8] Total Harga
        └─► [9] Keluar Program
        │
        ▼
┌────────────────────┐
│ Ulang ke Menu Awal │
└───────┬────────────┘
        │
        ▼
┌────────────────────┐
│ Program Selesai    │
└────────────────────┘
```

---

## 🔍 Penjelasan Functions dan Attributes

### 📦 File: `function.py`
Class `Transaction` menyimpan semua logika utama dari sistem kasir.

| Function | Deskripsi | Contoh Penggunaan |
|-----------|------------|-------------------|
| `add_item(nama_item, jumlah_item, harga_per_item)` | Menambahkan item baru ke keranjang. | `add_item("Roti", 2, 5000)` |
| `update_item_name(nama_item, update_nama_item)` | Mengubah nama item yang sudah ada. | `update_item_name("Roti", "Roti Coklat")` |
| `update_item_qty(nama_item, update_jumlah_item)` | Mengubah jumlah item tertentu. | `update_item_qty("Roti", 5)` |
| `update_item_price(nama_item, update_harga_item)` | Mengubah harga per item. | `update_item_price("Roti", 6000)` |
| `delete_item(nama_item)` | Menghapus item dari keranjang. | `delete_item("Roti")` |
| `reset_transaction()` | Menghapus seluruh isi keranjang. | `reset_transaction()` |
| `check_order()` | Menampilkan isi keranjang dalam bentuk tabel. | `check_order()` |
| `total_price()` | Menghitung total seluruh harga. | `total_price()` |

Setiap item disimpan dalam dictionary seperti berikut:
```python
{
    "Nama Item": {
        "jumlah item": int,
        "harga/item": int,
        "total harga": int
    }
}
```

---

## 💻 Demonstrasi Program (Test Case dan Output)

### 🧩 Test Case 1 — Tambah Item
**Input:**
```
1
Masukkan nama item: Roti
Masukkan jumlah item: 2
Masukkan harga per item: 5000
```

**Output:**
```
Item 'Roti' berhasil ditambahkan.
-----------------------------------
No  Nama Item  Jumlah Item  Harga/item  Total Harga
1   Roti       2            5000        10000
```

---

### 🧩 Test Case 2 — Update Jumlah Item
**Input:**
```
3
Masukkan nama item yang ingin diubah: Roti
Masukkan jumlah item baru: 5
```

**Output:**
```
Jumlah item berhasil diperbarui.
-----------------------------------
No  Nama Item  Jumlah Item  Harga/item  Total Harga
1   Roti       5            5000        25000
```

---

### 🧩 Test Case 3 — Hapus Item
**Input:**
```
5
Masukkan nama item yang ingin dihapus: Roti
```

**Output:**
```
Item 'Roti' telah dihapus dari keranjang.
```

---

### 🧩 Test Case 4 — Total Harga
**Input:**
```
8
```

**Output:**
```
Total harga keseluruhan adalah: 25000
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

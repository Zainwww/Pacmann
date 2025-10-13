# untuk membuat table
from tabulate import tabulate

# square root, untuk menghitung euclidean distance
from math import sqrt

# method untuk menampilkan benefit membership
def show_benefit():
    membership_table = [["Platinum","15%","Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
                        ["Gold","10%","Benefit Silver + Voucher Ojek Online"],
                        ["Silver","8%","Voucher Makanan"]]
    head_membership_table = ["Membership","Discount","Another Benefit"]
    
    print(tabulate(membership_table, headers = head_membership_table, tablefmt = 'github', stralign = 'center'))


# method untuk menampilkan requirements membership
def show_requirements():
        requirements_membership_table = [["Platinum",8,15],
                                         ["Gold",6,10],
                                         ["Silver",5,7]]
        head_requirements_membership_table = ["Membership","Monthly Expense (juta)","Monthly Income (juta)"]
       
        print(tabulate(requirements_membership_table, headers = head_requirements_membership_table, tablefmt = 'github', stralign = 'center'))

# inisialisasi data
data = {
    "Sumbul" : "Platinum",
    "Ana" : "Gold",
    "Cahya" : "Platinum"
}

def show_data():
    print(data)

class Membership:
    
    # inisialisai attribute
    def __init__(self,username):
        self.username = username

    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self,monthly_expense, monthly_income):
        membership = {"Platinum" : [8,15],
                      "Gold" : [6,10],
                      "Silver" : [5,7]}
        hasil ={}
        for key, value in membership.items():
            jarak = sqrt((monthly_expense-value[0])**2+(monthly_income-value[1])**2)
            hasil.update({key:jarak})
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {hasil}")
        hasil = (sorted(hasil.items(), key =lambda item : item[1]))
        data.update({self.username:hasil[0][0]})
        print(hasil[0][0])

    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def jenis_member(self):
        for key, value in data.items():
            if self.username == key:
                print(value)
                break
    
    
    # method untuk menghitung final price berdasarkan membership
    def calculate_price(self, list_harga_barang):
        membership = data.get(self.username)
        diskon = {"Platinum" : 0.15,
                  "Gold" :0.1,
                  "Silver" :0.08}
        diskon_pelanggan = diskon.get(membership)
        harga_total = 0
        for x in list_harga_barang:
            harga_total += x
        harga_akhir = harga_total * (1-diskon_pelanggan)
        print(f"total harga adalah {harga_akhir}")

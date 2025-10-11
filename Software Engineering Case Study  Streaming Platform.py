from tabulate import tabulate

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

table = [["True","True","True","Bisa Stream"],
             ["True","True","True","Bisa Download"],
             ["True","True","True","Kualitas SD"],
             ["False","True","True","Kualitas HD"],
             ["False","False","True","Kualitas UHD"],
             [1,2,4,"Number of device"],
             ["3rd party Movie only",
              "Basic Plan Content + Sports",
              "Basic Plan + Standard Plan + PacFlix Original Series" ,
              "Jenis Konten"],
             [120000,160000,200000,"Harga"]
            ]
head = ["Basic Plan","Standard Plan","Premium Plan","Services"]

def check_benefit():
    print("PacFlix plan List")
    print()
    print()
    print()
    print(tabulate(table,headers = head))
    
    
class User:
    def __init__(self,username,duration_plan,current_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan
        
    def check_plan(self):
        print(self.current_plan)
        print()
        print(self.duration_plan)
        print()
        print()
        print(f"{self.current_plan} PacFlix Benefit List")
        print()
        print()
        table_customer = []
        table_customer_head = []
        key_customer_plan = head.index(self.current_plan)
        key_services = head.index("Services")
        table_customer_head.append(head[key_customer_plan])
        table_customer_head.append(head[key_services])
        for x in table:
            temp = [x[key_customer_plan],x[key_services]]
            table_customer.append(temp)
        print(tabulate(table_customer,headers = table_customer_head))
        
    def upgrade_plan(self, current_plan, new_plan):
        if current_plan != new_plan:
            for key,value in data.items():
                if key == self.username:
                    duration_plan = value[1] 
            key_customer_plan = head.index(current_plan)
            key_new_plan = head.index(new_plan)
            harga_customer_plan = table[-1][key_customer_plan]
            harga_new_plan = table[-1][key_new_plan]
            if duration_plan > 12:
                harga_upgrade = harga_new_plan *(0.95)
            else:
                harga_upgrade = harga_new_plan
            print(harga_upgrade)
        

class NewUser:
    def __init__(self,username):
        self.username = username
        temp = list()
        check = []
        for key,value in data.items():
            check.append(key)
        if username not in check:
            temp_dict = {username:temp}
            data.update(temp_dict)
        else:
            print("username telah ada")
    def pick_plan(self,new_plan, code_referral):
        key_new_plan = head.index(new_plan)
        harga_new_plan = table[-1][key_new_plan]
        t=False
        if new_plan in head:   
            for key,value in data.items():
                if len(value)==0:
                    pass
                elif code_referral == value[-1]:
                    t=True
                    print(harga_new_plan*(0.96))
            if t ==False:
                raise Exception("Referral Code doesn't exist") 
        else:
            print("Plan doesn't exist")
                
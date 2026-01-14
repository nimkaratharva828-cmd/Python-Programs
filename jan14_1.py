class Players:
    def __init__(self,jn,nm,r,w,tn):
        self.jersey_number = jn
        self.p_name = nm
        self.runs = r
        self.wickets = w
        self.t_name = tn

p1 = Players(7, "MS Dhoni", 15000, 0, "CSK")
p2 = Players(18, "Virat Kohli", 20000, 0, "RCB")
p3 = Players(10, "Sachin Tendulkar", 34000, 0, "MI")
p4 = Players(45, "Rohit Sharma", 12000, 0, "MI")
p5 = Players(9, "Anil Kumble", 2500, 619, "RCB")

rcb_list=[]
rcb_list.append(p1)
rcb_list.append(p2)
rcb_list.append(p3)
rcb_list.append(p4)
rcb_list.append(p5)
rcb_list.append(Players(4, "AB de Villiers", 9500, 0, "RCB"))
rcb_list.append(Players(3, "Yuzvendra Chahal", 500, 150, "RCB"))
rcb_list.append(Players(11, "Devdutt Padikkal", 2000, 0, "RCB"))

for p in rcb_list:
    print(p.p_name)

for p in rcb_list:
    if p.runs>5000:
        print(p.p_name, p.runs)
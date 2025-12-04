
def tanggalbaru(tanggal, bulan):
        while True:
            print("Masukkan bulan:")
            bulan = input("> ").lower().strip()
            if bulan == "":
                print("   ⚠  Tugas tidak boleh kosong.\n")
                continue
            elif not bulan.isdigit():
                print("   ⚠  Masukkan angka\n")
                continue
            elif bulan.isdigit():
                b=int(bulan)
                if len(bulan)>=3 or bulan == 0:
                    print("   ⚠  Input tidak valid\n")
                    continue
            elif bulan =="":
                print("   ⚠  Bulan tidak boleh kosong.\n")
            else:
                if bulan == "januari" or bulan == "january":
                    b=1
                elif bulan == "februari" or bulan == "february":
                    b=2
                elif bulan == "maret" or bulan == "march":
                    b=3
                elif bulan == "april" or bulan == "april":
                    b=4
                elif bulan == "mei" or bulan == "may":
                    b=5
                elif bulan == "juni" or bulan == "june":
                    b=6
                elif bulan == "juli" or bulan == "july":
                    b=7
                elif bulan == "agustus" or bulan == "august":
                    b=8
                elif bulan == "september" or bulan == "september":
                    b=9
                elif bulan == "oktober" or bulan == "october":
                    b=10
                elif bulan == "november" or bulan == "november":
                    b=11
                elif bulan == "desember" or bulan == "december":
                    b=12
                else:
                    print("   ⚠  input tidak valid.\n")
                    continue     
            if b in [1,3,5,7,8,10,12]:
                hari = 31
            elif b in [4,6,9,11]:
                hari = 30
            elif b ==  2:
                hari = 29
            else:
                print("   ⚠  input tidak valid.\n")
                continue
            while True:
                print("----------------------------------------------------\n")
                print("Masukkan tanggal:")
                tanggal = input("> ").strip()
                if tanggal.isdigit():
                    tgl = int(tanggal)
                    if len(tanggal)>=3 or tanggal == 0:
                        print("   ⚠  Input tidak valid\n")
                    elif tgl == 0:
                        print("   ⚠  Input tidak valid\n")
                        continue
                    else:
                        if 1 <= tgl <= hari:
                            return tgl, b
                        else:
                            print("   ⚠  Tanggal melebihi batas\n")
                elif tanggal == "":
                    print("   ⚠  Tanggal tidak boleh kosong.\n")      
                else:
                    print("   ⚠  Masukkan angka\n")


def tugasbaru(tugas):
        while True:
            print("\nMasukkan tugas baru:")
            tugas= input("> ").strip()
            if tugas =="":
                print("   ⚠  Tugas tidak boleh kosong.\n")
                continue
            else: 
                return tugas
            
def checklist(hapus):
        while True:
            print("\nMasukkan tugas:")
            tugas= input("> ").strip()
            if tugas =="":
                print("   ⚠  Tugas tidak boleh kosong.\n")
                continue
            else: 
                return tugas
            




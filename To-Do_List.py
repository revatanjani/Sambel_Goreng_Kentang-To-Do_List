daftar_tugas = {}

def cek(menu):
        if len(daftar_tugas)==0:
            print("\n           ⚠  Anda belum memasukkan tugas              \n")
        else:
            if menu == "4" or  menu == "5":
                print("")
            else:
                print("\n\n========================================================")
                print("                   TUGAS SELESAI                       ")
                print("========================================================\n")
                isi = 0
                for id,data in daftar_tugas.items():
                        if data[4]=="Selesai":
                            isi += 1
                            print(f"No.ID       : {id}")
                            print(f"judul tugas : {data[0]}")
                            print(f"Deadline    : {data[1]}-{data[2]}-{data[3]}")
                            print(f"Status      : {data[4]}")
                            print("---------------------------")                    
                if isi == 0:
                    print("                     Tidak ada tugas                              \n\n\n")


            print("\n\n========================================================")
            print("                   TUGAS BELUM SELESAI                      ")
            print("========================================================\n")
            if len(daftar_tugas) == 0:
                print("               Anda belum memasukkan tugas                    ")
            else:
                isi = 0
                for id,data in daftar_tugas.items():
                    if data [4]!="Selesai":
                        isi += 1
                        print(f"No.ID       : {id}")
                        print(f"judul tugas : {data[0]}")
                        print(f"Deadline    : {data[1]}-{data[2]}-{data[3]}")
                        print(f"Status      : {data[4]}")
                        print("---------------------------")
            if menu == "1" or menu == "cek" :
                print("\n",isi,"Tugas belum terselesaikan")
                print("---------------------------")
            else:
                print("")
            if isi == 0:
                print("                     Tidak ada tugas                              \n\n\n")
def hapus(n):
    if len(daftar_tugas)==0:
        print("\n   ⚠  Anda belum memasukkan tugas\n")
    else:
        print("\n----------------------DELETE------------------------")
        cek(n)
        print("----------------------------------------------------")

        print("Masukkan ID tugas yang ingin dihapus:")
        print("Ketik 0 jika ingin batal \n")
        nomor = input("> ").strip()
        if nomor == "0":
            return
        else:
            while True:
                if nomor in daftar_tugas:
                    print("\n      [ID ditemukan]\n")
                    print("---------------------------")
                    data = daftar_tugas[nomor]
                    print(f"No.ID       : {nomor}")
                    print(f"judul tugas : {data[0]}")
                    print(f"Deadline    : {data[1]}-{data[2]}-{data[3]}")
                    print(f"Status      : {data[4]}")
                    print("---------------------------")
                    makesure = input("\nKamu yakin ingin menhapus tugas?(y/n)").strip().lower()
                    if makesure == "y":
                        del daftar_tugas[nomor]
                        baru = {}
                        nomor_baru = 1
                        for key in sorted(daftar_tugas, key=int):
                            baru[str(nomor_baru)] = daftar_tugas[key]
                            nomor_baru += 1
                        daftar_tugas.clear()
                        daftar_tugas.update(baru)
                        print("\n   ✔  Tugas berhasil dihapus")
                        print("----------------------------------------------------\n")
                        break
                    elif makesure == "n":
                        print("\n---------------------------")
                        print("   ← Penghapusan dibatalkan")
                        print("---------------------------")
                        break
                    
                    else:
                        print("   ⚠  Input tidak diketahui\n")
                        continue
                else:
                    print("\n   ⚠  ID tidak ditemukan\n")
                    continue 

def tambah():
    
    print("\n----------------------CREATE------------------------")
    nomor = str(len(daftar_tugas)+ 1)
    while True:
        print("\nMasukkan tugas:")
        print("Ketik 0 jika ingin batal \n")
        tugas= input("> ").strip()
        if tugas == "0":
            return
        elif tugas =="":
            print("   ⚠  Tugas tidak boleh kosong.\n")
            continue
        else: 
            break
    while True:
            print("----------------------------------------------------\n")
            print("Masukkan bulan:")
            bulan = input("> ").lower().strip()
            if bulan == "":
                print("   ⚠  Tugas tidak boleh kosong.\n")
                continue
            elif not bulan.isdigit():
                print("   ⚠  Masukkan angka\n")
                continue
            elif bulan.isdigit():
                b = int(bulan)
                if len(bulan)>=3 or bulan == 0:
                    print("   ⚠  Input tidak valid\n")
                    continue
            elif bulan == "":
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
                    if len(tanggal)>=3:
                        print("   ⚠  Input tidak valid\n")
                        continue
                    elif tgl == 0:
                        print("   ⚠  Input tidak valid\n")
                        continue
                    else:
                        if 1 <= tgl <= hari:
                            daftar_tugas[nomor] = [tugas,tanggal,bulan,2025,"Belum Selesai"]
                            print("\n   ✔  Tugas berhasil ditambahkan")
                            return
                        else:
                            print("   ⚠  Tanggal melebihi batas\n")
                elif tanggal == "":
                    print("   ⚠  Tanggal tidak boleh kosong.\n")      
                else:
                    print("   ⚠  Masukkan angka\n")



def checklist(n):
    if len(daftar_tugas)==0:
        print("\n   ⚠  Anda belum memasukkan tugas\n")
    else:
        print("\n---------------------CHECKLIST----------------------")
        while True:
            cek(n)
            print("Masukkan ID tugas yang ingin dichecklist:")
            print("Ketik 0 jika ingin batal \n")
            centang = input("> ").strip()
            if centang == "0":
                return
            else:
                if centang not in daftar_tugas:
                    print("\n   ⚠  ID tidak ditemukan\n")
                    continue
                if daftar_tugas[centang][4]== "SELESAI":
                    print("\n⚠  Tugas tersebut sudah dichecklist\n")
                    break
                else:
                    if not centang.isdigit():
                        print("   ⚠  Input harus berupa angka\n")
                        continue
                    
                    elif centang in daftar_tugas:
                            print("\n      [ID ditemukan]\n")
                            print("---------------------------")
                            data = daftar_tugas[centang]
                            print(f"No.ID       : {centang}")
                            print(f"judul tugas : {data[0]}")
                            print(f"Deadline    : {data[1]}-{data[2]}-{data[3]}")
                            print(f"Status      : {data[4]}")
                            print("---------------------------")

                    else:
                        print("\n   ⚠  Input tidak diketahui\n")
                        continue
                    while True:
                        makesure = input("Kamu yakin telah menyelesaikan tugas ini? (y/n)\n").strip().lower()
                        print("---------------------------")
                        if makesure == "y":
                            daftar_tugas[centang][4]= "Selesai"

                            print("\n   ✔  Tugas berhasil dichecklist")
                            return
                        elif makesure =="n":
                            print("   ←  Checklist dibatalkan")
                            print("---------------------------")
                            return
                        else:
                            print("\n   ⚠  Input tidak diketahui\n")
                            continue
def perbarui(n):
            if len(daftar_tugas)==0:
                print("\n   ⚠  Anda belum memasukkan tugas\n")
            else:
                print("\n---------------------UPDATE----------------------")
                while True: 
                    cek(n)
                    print("Masukkan ID tugas yang ingin diperbarui:")
                    print("ketik 0 jika ingin batal ")
                    update = input("> ").strip()
                    if update == "0":
                        return
                    else:
                        if not update.isdigit():
                            print("   ⚠  Input harus berupa angka\n")
                        elif update not in daftar_tugas:
                            print("\n   ⚠  ID tidak ditemukan\n")
                        elif update in daftar_tugas and daftar_tugas[update][4]=="SELESAI":
                            print("\n   ⚠ Tugas sudah diselesaikan tidak dapat edit\n")
                            continue
                        else:
                            while True:
                                    cek(n)
                                    print("\n\n+===============================================+")
                                    print("                  -Menu Update-                     ")
                                    print("\n+===============================================+\n")
                                    print(" [1] Tugas       - Memperbarui tugas                       ")
                                    print(" [2] Tanggal     - Memperbarui tanggal deadline            ")
                                    print(" [3] Batal       - Membatalkan pembaruan                   ")
                                    print("\n-------------------------------------------------")
                                    baru= input(" > ").strip().lower()
                                    if baru == "1" or baru == "Tugas":
                                        from lemari_fungsi import tugasbaru
                                        tugass=tugasbaru("")
                                        makesure = input("Kamu yakin ingin merubah tugasnya?(y/n)").strip().lower()
                                        if makesure == "y":
                                            print("\n   ✔  Tugas berhasil diperbarui")
                                            daftar_tugas[update][0] = tugass
                                            continue
                                        else: 
                                            print("---------------------------")
                                            print("   ←  Update dibatalkan") 
                                            print("---------------------------")
                                            break
                                    elif baru == "2" or baru == "Tanggal":
                                        from lemari_fungsi import tanggalbaru
                                        tgl, bln= tanggalbaru("", "")
                                        makesure = input("Kamu yakin ingin merubah tanggalnya?(y/n)").strip().lower()
                                        if makesure == "y":
                                            print("\n   ✔  Tanggal berhasil diperbarui")
                                            daftar_tugas[update][1]= tgl
                                            daftar_tugas[update][2]= bln
            
                                        else: 
                                            print("---------------------------")
                                            print("   ←  Update dibatalkan") 
                                            print("---------------------------")
                                            break
                                    elif baru == "3" or baru == "Batal":
                                        return
                                    else:
                                        print("\n ⚠  Menu tidak diketahui")
                                        continue            
while True:
    print("\n+==================================================+")
    print("                  -Menu Utama-                     ")
    print("\n                 TO-DO List APP                     ")
    print("\n+==================================================+\n")

    print(" [1] Cek         - Cek Semua Tugas                          ")
    print(" [2] Tambah      - Tambah Tugas                             ")
    print(" [3] Hapus       - Hapus Tugas                              ")
    print(" [4] Checklist   - Tandai Tugas Selesai                     ")
    print(" [5] Perbarui    - Edit Tugas                               ")
    print(" [6] Keluar      - Keluar Program                           ")
    print("\n----------------------------------------------------")
    menu = input ("pilih menu: ").lower().strip()
    if menu == "1" or menu == "cek": cek(menu)
    elif menu == "2" or menu == "tambah": tambah()
    elif menu == "3" or menu == "hapus" : hapus(menu)
    elif menu == "4" or menu == "checklist": checklist(menu)
    elif menu == "5" or menu == "perbarui" : perbarui(menu)
    elif menu == "6" or menu == "keluar" : 
        print(" ⚠   Keluar program")
        break
    else: print(" ⚠  Menu tidak diketahui")
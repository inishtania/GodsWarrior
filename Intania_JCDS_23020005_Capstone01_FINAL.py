import datetime
from datetime import date

dataNasabah = {
    0:{'id':2402100700000061,'NIK':3678910,'Nama': 'Intania','Tanggal Lahir': '10-07-1992','Alamat':'Jl.Makmur no 98','Tanggal Buat':'19-02-2024','Dana Nasabah':1000000000,'Status':'Prioritas'},
    1:{'id':2310120800000139,'NIK':3798007,'Nama': 'Nur Komala Saijah','Tanggal Lahir': '12-08-1986','Alamat':'Jl.Setiabudi Kasih no.115','Tanggal Buat':'10-10-2023','Dana Nasabah':275000000,'Status':'Non Prioritas'},
    2:{'id':2112080200000147,'NIK':1800759,'Nama': 'Haris Purwadhana','Tanggal Lahir': '08-02-1994','Alamat':'Jl.Maju Bersama no.88','Tanggal Buat':'09-12-2021','Dana Nasabah':750000000,'Status':'Non Prioritas'},
    3:{'id':2008010500000087,'NIK':9007966,'Nama': 'Angel Kumala','Tanggal Lahir': '01-05-1992','Alamat':'Jl. Panca Indera no.5','Tanggal Buat':'08-08-2020','Dana Nasabah':785000000,'Status':'Prioritas'},
    4:{'id':2401140300000104,'NIK':1288997,'Nama': 'Gista Renata','Tanggal Lahir': '14-03-1998','Alamat':'Jl. Kesetiaan no 71','Tanggal Buat':'01-01-2024','Dana Nasabah':350000000,'Status':'Non Prioritas'},
    5:{'id':1810280300000093,'NIK':7894561,'Nama': 'Josh Gibran','Tanggal Lahir': '28-03-1980','Alamat':'Jl.Setiadharma no 98','Tanggal Buat':'12-10-2018','Dana Nasabah':900000000,'Status':'Non Prioritas'}
}

#-----------------------------------VARIABEL PENGULANGAN-----------------------------------
count = 5           #untuk looping data
keys_dataNasabah = 5
angka = 0           #untuk menampung angka pilihan untuk setiap input menu
kamarPenemuan =0    #kalau ketemu data dirubah menjadi 1
kamarNIK =0         #untuk menampung data ID Nasabah
hasilData =0        #untuk menampung def tarik_data_keys_item yakni dataNasabah keys
kamar_y=''          #untuk menyimpan data di menu Update karena data dataNasabah[0][i] merupakan string
kamarMenu = ''
salah = 'Input angka anda salah'
judulPerusahaan =('''\t\t\t\t\t\t\t DATA NASABAH PT ABC SEKURITAS
                  ''')
judulTabelNasabah=(f'''ID\t\t    |NIK\t  |Nama\t\t\t    |Tanggal Lahir\t|Alamat\t\t\t       |Tanggal Buat\t|Dana Nasabah\t|Status''')
#-----------------------------------FUNGSI - FUNGSI TERULANG-----------------------------------
def menuUtama ():
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t\t\tMenu Utama : 
    \t\t\t\t    
          \t\t\t\t\t\t  1. Melihat Data Nasabah
          \t\t\t\t\t\t  2. Menambah Data Nasabah
          \t\t\t\t\t\t  3. Mengupdate Data Nasabah
          \t\t\t\t\t\t  4. Menghapus Data Nasabah
          \t\t\t\t\t\t  5. Pelayanan Nasabah Prioritas
          \t\t\t\t\t\t  6. Keluar
          ''')

def cekData():
    global kamarPenemuan #dibikin global supaya kamarPenemuan default 0
    kamarPenemuan=0
    global kamarNIK
    kamarNIK =0

    cekNik = int(input('''\t\t\t\t    Masukkan ID Nasabah (9 untuk melihat data,0 untuk ke menu utama):'''))
    if cekNik == 9:
        lihatData()
        cekData()
    elif cekNik == 0:
        kamarPenemuan = 8
        print()
    else:
        for i in dataNasabah.values():
            for j in i.values():
                if j == cekNik:
                    kamarPenemuan=1
                    kamarNIK = cekNik
                    break
                else:
                    continue
                            
        


def tarik_data_keys_items():
    for i,j in dataNasabah.items():
        for k in j.values():
            if k == kamarNIK:
                global hasilData
                hasilData=(int(i))
                break
            else:
                continue

def print_satu_data():
    print(judulPerusahaan)
    print()
    print(judulTabelNasabah)
    print(f'''{str(dataNasabah[hasilData]['id']).ljust(20)}|{str(dataNasabah[hasilData]['NIK']).ljust(13)}|{dataNasabah[hasilData]['Nama'].ljust(25)}|{dataNasabah[hasilData]['Tanggal Lahir'].ljust(15)}    |{dataNasabah[hasilData]['Alamat'].ljust(30)}|{dataNasabah[hasilData]['Tanggal Buat'].ljust(15)} |{dataNasabah[hasilData]['Dana Nasabah']}\t|{dataNasabah[hasilData]['Status']}''')

def print_per_baris():
    print(f'''{str(dataNasabah[hasilData]['id']).ljust(20)}|{str(dataNasabah[hasilData]['NIK']).ljust(13)}|{dataNasabah[hasilData]['Nama'].ljust(25)}|{dataNasabah[hasilData]['Tanggal Lahir'].ljust(15)}    |{dataNasabah[hasilData]['Alamat'].ljust(30)}|{dataNasabah[hasilData]['Tanggal Buat'].ljust(15)} |{dataNasabah[hasilData]['Dana Nasabah']}\t|{dataNasabah[hasilData]['Status']}''')

def lihatData():
    print(judulPerusahaan)
    print()
    print(judulTabelNasabah)
    for i in dataNasabah:
        print(f'''{str(dataNasabah[i]['id']).ljust(20)}|{str(dataNasabah[i]['NIK']).ljust(13)}|{dataNasabah[i]['Nama'].ljust(25)}|{dataNasabah[i]['Tanggal Lahir'].ljust(15)}    |{dataNasabah[i]['Alamat'].ljust(30)}|{dataNasabah[i]['Tanggal Buat'].ljust(15)} |{dataNasabah[i]['Dana Nasabah']}\t|{dataNasabah[i]['Status']}''')
        

def lihatDataNIK():
    if kamarPenemuan==0:
        print('\t\t\t\t\t\t\t  Data tidak ditemukan')
        cekData()
        lihatDataNIK()
    # elif kamarPenemuan == 8 :
    #     menuUtama()
    else:
        tarik_data_keys_items()
        print_satu_data()

def lihatLagiLagi(): 
    lihatLagi = input('\t\t\t\t    Apakah masih mau mencari lagi atau kembali ke menu sebelumnya? (Y/T)  : ')
    if lihatLagi.lower() == 'y':
        cekData()
        global kamarPenemuan
        if kamarPenemuan == 8:
            menuUtama()
        else:
            lihatDataNIK()  
            lihatLagiLagi()          
    elif lihatLagi.lower() == 't': 
        menu1()
    else:
        print(salah)
        menu1()
   

#-----------------------------------MENU 01-----------------------------------
def menu1():
    print('''\t\t\t\t\t\t\t  Database Nasabah :
          \t\t\t\t\t\t  1. Melihat semua data
          \t\t\t\t\t\t  2. Melihat berdasarkan ID Nasabah
          \t\t\t\t\t\t  3. Menu Utama
          ''')
    try:
        angka = int(input("\t\t\t\t\t\t\t  Masukkan angka : "))
        if angka == 1 :
            lihatData()
            menu1()
        elif angka == 2 :
            cekData()
            global kamarPenemuan
            if kamarPenemuan == 1 :
                lihatDataNIK()
                lihatLagiLagi() 
            elif kamarPenemuan == 8 :
                menuUtama()
            else :
                menuUtama()
        elif angka == 3:
            menuUtama()
        else:
            print('\t\t\t\t\t\t\t  Salah, silahkan pilih kembali')
            menu1()
    except ValueError:
        print("\t\t\t\t\t\t  Input anda tidak benar. Masukkan angka 1,2,3")
        menu1()

#-----------------------------------MENU 02-----------------------------------
dict_baru = {
    10 : {'id':0,'NIK':0,'Nama': '','Tanggal Lahir': '','Alamat':'','Tanggal Buat':'','Dana Nasabah':0,'Status':''} 
}

def idNasabahGenerator():
    import re
    date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    tambahLahirid = input("Masukkan tanggal lahir nasabah (dd-mm-yyyy):")
    if not date_pattern.match(tambahLahirid):
        print("Format tanggal salah. Pastikan Anda memasukkan tanggal dalam format dd-mm-yyyy.")
        idNasabahGenerator()
    else:
        dict_baru[10]['Tanggal Lahir']= tambahLahirid

    from datetime import date
    tambahTanggalid = date.today().strftime('%d-%m-%Y')
    dict_baru[10]['Tanggal Buat']= tambahTanggalid

    bulanIni = tambahTanggalid[8:10]+tambahTanggalid[3:5]
    bulanUltah = dict_baru[10]['Tanggal Lahir'][0:2]+dict_baru[10]['Tanggal Lahir'][3:5]

    abjad = "abcdefghijklmnopqrstuvwxyz"
    nama = dict_baru[10]['Nama']
    id_tanggal_lower = nama.lower()
    c = 0
    for i in id_tanggal_lower: 
        if i !=' ':
            c += abjad.index(i)

    buat_id_nasabah = int(bulanIni) * 1000000000000 + int(bulanUltah)*100000000 + c
    dict_baru[10]['id'] = buat_id_nasabah
    
def cetak_data_input_baru():
    print(judulPerusahaan)
    print(judulTabelNasabah)
    print(f'''{str(dict_baru[10]['id']).ljust(20)}|{str(dict_baru[10]['NIK']).ljust(13)}|{dict_baru[10]['Nama'].ljust(25)}|{dict_baru[10]['Tanggal Lahir'].ljust(15)}    |{dict_baru[10]['Alamat'].ljust(30)}|{dict_baru[10]['Tanggal Buat'].ljust(15)} |{dict_baru[10]['Dana Nasabah']}\t|{dict_baru[10]['Status']}''')
    # print(f'''{str(dict_baru[10]['id']).ljust(20)}|{str(dict_baru[10]['NIK']).ljust(20)}|{dict_baru[10]['Nama'].ljust(30)}|{dict_baru[10]['Tanggal Lahir'].ljust(15)}|{dict_baru[10].get('Alamat', '').ljust(30)}|{dict_baru[10]['Tanggal Buat'].ljust(15)}|{dict_baru[10]['Dana Nasabah']}''')

def dataBenar():
    global keys_dataNasabah
    keys_dataNasabah += 1 
    dataNasabah[keys_dataNasabah] = {}
    dataNasabah[keys_dataNasabah]['id']= dict_baru[10]['id']
    dataNasabah[keys_dataNasabah]['NIK']= dict_baru[10]['NIK']
    dataNasabah[keys_dataNasabah]['Nama']= dict_baru[10]['Nama']
    dataNasabah[keys_dataNasabah]['Tanggal Lahir']= dict_baru[10]['Tanggal Lahir']
    dataNasabah[keys_dataNasabah]['Alamat']= dict_baru[10]['Alamat']
    dataNasabah[keys_dataNasabah]['Tanggal Buat']= dict_baru[10]['Tanggal Buat']
    dataNasabah[keys_dataNasabah]['Dana Nasabah']= dict_baru[10]['Dana Nasabah']
    dataNasabah[keys_dataNasabah]['Status']= dict_baru[10]['Status']

def isi_kamar_menu():
    global kamarMenu
    if kamarMenu == 'menu1':
        menu1()
    elif kamarMenu == "menu2":
        menu2()
    elif kamarMenu =="menu3":
        menu3()
    elif kamarMenu== "menu4":
        menu4()
    elif kamarMenu == "menu5":
        menu5()

def memastikanKembali(): 
    pastikan = input("Apakah data sudah benar? (Y/T) : ")
    if pastikan.lower() == 'y':
        print('Data telah berhasil diinput')
    elif pastikan.lower() == 't':
        kolom()
        cetak_data_input_baru()
        memastikanKembali()

def kolom ():
    print('''Pilih kode kolom yang ingin anda ubah :
                - NIK
                - Nama
                - Tanggal Lahir
                - Alamat
                - Dana Nasabah
                - Status
            ''')
    kolom_input = (input ('Ketikkan kode yang ingin anda ubah, pastikan sama : '))
    gantiKolom(kolom_input)


def gantiTanggal():
    import re
    date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    while True :
        inputTanggalLahir = input("Masukkan tanggal lahir nasabah (dd-mm-yyyy):")
        if not date_pattern.match(inputTanggalLahir):
            print("Format tanggal salah. Pastikan Anda memasukkan tanggal dalam format dd-mm-yyyy.")
            continue
        else:
            dict_baru[10]['Tanggal Lahir']= inputTanggalLahir
            break

def gantiKolom (kolom):
    if kolom == 'Tanggal Lahir':
        gantiTanggal()
    elif kolom in dict_baru[10]:
        if isinstance(dict_baru[10][kolom], str):
            value = input('Masukkan data yang benar: ')
            dict_baru[10][kolom] = value
        elif isinstance(dict_baru[10][kolom], int):
            value = int(input('Masukkan data yang benar: '))
            dict_baru[10][kolom] = value
    elif kolom not in dict_baru[10]:
        print('Tidak ada kode tersebut. Mohon pastikan anda memasukkan kode yang benar')
        kolom_input = (input ('Ketikkan kode yang ingin anda ubah, pastikan sama : '))
        gantiKolom(kolom_input)


def tambahData():                                                                       
    # tambahNIK = int(input("Masukkan NIK Nasabah :"))
    # dict_baru[10]['NIK'] = tambahNIK
    while True:
        try:
            tambahNIK = int(input("Masukkan NIK Nasabah: "))
            break  
        except ValueError:
            print("NIK harus berupa bilangan bulat.")
    dict_baru[10]['NIK'] = tambahNIK

    tambahNama = input ("Masukkan nama lengkap nasabah : ")
    dict_baru[10]['Nama'] = tambahNama

    idNasabahGenerator()
    
    tambahAlamat = input("Masukkan alamat nasabah : ")
    dict_baru[10]['Alamat']= tambahAlamat
    
    while True:
        try:
            tambahDana = int(input("Masukkan total dana awal Nasabah: "))
            break  
        except ValueError:
            print("Dana harus berupa bilangan bulat.")
    dict_baru[10]['Dana Nasabah'] = tambahDana
    # tambahDana = int(input("Masukkan total dana awal Nasabah : "))
    # dict_baru[10]['Dana Nasabah']=tambahDana
    while True :
        tambahStatus = input("Apakah nasabah prioritas atau tidak?(P/T) :")
        if tambahStatus.lower() == 'p' :
            dict_baru[10]['Status']= 'Prioritas'
            break
        elif tambahStatus.lower() == 't' :
            dict_baru[10]['Status']= 'Non Prioritas'
            break
        else:
            print("Silahkan pilih P atau T")
            continue

    cetak_data_input_baru()
    memastikanKembali()
    dataBenar()
    lihatData()
    menu2()

def menu2():
    global kamarMenu
    kamarMenu == "menu2"
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t\t  DATABASE MANAGEMENT SYSTEM  :
          \t\t\t\t\t\t  1. Menambah data nasabah baru
          \t\t\t\t\t\t  2. Menu utama
                                         ''')
    print()
    try : 
        angka = int(input("\t\t\t\t\t\t\t  Masukkan angka : "))
        if angka == 1 : 
            cekData()
            if kamarPenemuan == 1 :
                print('\t\t\t\t\t\t\t\tData sudah ada')
                menu2()
            elif kamarPenemuan == 8 :
                menuUtama()
            else :
                print()
                print("\t\t\t\t\t   ID Nasabah tidak ditemukan. Silahkan menambahkan data terbaru.")
                print()
                tambahData()
        elif angka == 2 :
            menuUtama()
        else:
            print("\t\t\t\t\t\t\t Input anda tidak benar. Masukkan angka 1 atau 2")
            menu2()
    except ValueError:
        print("\t\t\t\t\t\t\t Input anda tidak benar. Masukkan angka 1 atau 2")
        menu2()

#-----------------------------------MENU 03-----------------------------------
#Diubah berdasarkan kolom dan dapat dilooping 
#Kalau sudah ditanya yakin atau tidak bisa dipilih apakah lanjut atau dibatalkan? Jika lanjut maka berubah, jika batal kembali ke data semula

def cariKolomDanKodeDict ():
    # ubah_key_dict_baru()
    dict_baru[10] = dataNasabah[hasilData].copy()
    print_satu_data()
    print()
    yakinUpdate = input(f'''Ini adalah data untuk {dict_baru[10]['Nama']}. Apakah ada yang mau anda rubah? (Y/T) :''')

    # kamarMenu == 3
    if yakinUpdate.lower() == 'y':
        kolom()
        cetak_data_input_baru()
        memastikanKembali()
        print()
    if yakinUpdate.lower() == 't':
        menu3()

def data_berhasil_diubah():
    dataNasabah[hasilData] = {}
    dataNasabah[hasilData]['id']= dict_baru[10]['id']
    dataNasabah[hasilData]['NIK']= dict_baru[10]['NIK']
    dataNasabah[hasilData]['Nama']= dict_baru[10]['Nama']
    dataNasabah[hasilData]['Tanggal Lahir']= dict_baru[10]['Tanggal Lahir']
    dataNasabah[hasilData]['Alamat']= dict_baru[10]['Alamat']
    dataNasabah[hasilData]['Tanggal Buat']= dict_baru[10]['Tanggal Buat']
    dataNasabah[hasilData]['Dana Nasabah']= dict_baru[10]['Dana Nasabah']
    dataNasabah[hasilData]['Status']= dict_baru[10]['Status']

def lanjut_tidak():
    lanjut = input("Apakah anda yakin ingin mengubahnya? Setelah diubah tidak bisa dibatalkan (Y/T) :")
    if lanjut.lower() == 'y':
        data_berhasil_diubah()
        print('Data telah berhasil diubah')
    elif lanjut.lower() == 't':
        print('Data tidak dirubah')

def menu3():
    global kamarMenu
    kamarMenu == 'menu3'
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t\t  DATABASE MANAGEMENT SYSTEM :
                                                           1. Mengubah data nasabah
                                                           2. Menu utama
                                         ''')
    print()
    try : 
        angka = int(input("\t\t\t\t\t\t\tMasukkan angka : "))
        if angka == 1 : 
            cekData()
            tarik_data_keys_items()
            if kamarPenemuan == 1 :
                cariKolomDanKodeDict()
                lanjut_tidak()
                lihatData()
                menu3()
            elif kamarPenemuan == 8 :
                menuUtama()
            elif kamarPenemuan == 0:
                print ( 'Data tersebut tidak ditemukan! ')
                menu3()
        elif angka == 2 :
            menuUtama()
        else:
            print("\t\t\t\t\t\t\t  Inputan anda salah")
            menu3()
    except ValueError:
        print("\t\t\t\t\t\t\t  Input anda tidak benar. Masukkan angka 1 atau 2")
        menu3()

#-----------------------------------MENU 04-----------------------------------
def hapus():
    for i,j in dataNasabah.items():
        for k in j.values():
            if k == kamarNIK:
                x=(int(i))
                break
    dataNasabah.pop(x)

def dataHapusKetemu():
    lihatDataNIK()
    yakin=input('Apakah anda yakin mau menghapusnya? (Y/T) : ')
    if yakin.lower() == 'y':
        hapus()
        global keys_dataNasabah
        keys_dataNasabah -=1
        print('Data telah berhasil dihapus')
        lihatData()
        menu4()
    else:
        menu4()


def dataTidakKetemu ():
    cobaLagi = (input("Data tidak ditemukan! Apakah ada data yang mau dihapus? (Y/T)  "))
    if cobaLagi.lower() == 'y' :
        cekData()
        if kamarPenemuan == 1 :
            dataHapusKetemu()
        elif kamarPenemuan == 0:
            dataTidakKetemu()
    else:
        menu4()

    
def menu4():
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t\t  DATABASE MANAGEMENT SYSTEM :
          \t\t\t\t\t\t  1. Menghapus Data Nasabah
           \t\t\t\t\t\t  2. Menu Utama
          ''')
    try:
        angka = int(input("\t\t\t\t\t\t\t  Masukkan angka : "))
        if angka == 1:
            cekData()
            if kamarPenemuan == 1:
                dataHapusKetemu()
            elif kamarPenemuan == 8:
                menuUtama()
            elif kamarPenemuan == 0:
                dataTidakKetemu()  
        elif angka == 2:
            menuUtama()
        else:
            print(salah)
            menu4()
    except ValueError:
        print("\t\t\t\t\t\t\t  Input anda tidak benar. Masukkan angka 1 atau 2")
        menu4()

#-----------------------------------MENU 05-----------------------------------
#Menu ini digunakan untuk menarik data pelanggan yang berulang tahun di saat bulan akses 
#Pilihan pun ada dua mau menggunakan bulan ini atau menggunakan bulan depan (bisa pilih bulan)
#Hasilnya adalah Nama Nasabah

#Menu kedua adalah untuk menentukan apakah ada orang yang bisa dijadikan target prioritas
def ulangTahun ():
    print(judulPerusahaan)
    print(judulTabelNasabah)
    tangkapBulan = 0
    bulanIni = date.today().strftime('%m')
    for i in dataNasabah:
        if dataNasabah[i]['Tanggal Lahir'][3:5] == bulanIni and dataNasabah[i]['Dana Nasabah'] >= 750000000 and 'Status' == 'Prioritas': 
            tangkapBulan +=1
            global hasilData
            hasilData = i
            print_per_baris()
        else:
            tangkapBulan +=0
    print()
    if tangkapBulan == 0 :
        print("\t\t\t\t\t\t\t  Tidak ada yang berulang tahun")
        print()
    else:
        print('')

def targetprioritas() :
    print(judulPerusahaan)
    print(judulTabelNasabah)
    for i in dataNasabah : 
        if dataNasabah[i]['Dana Nasabah'] >= 750000000 and dataNasabah[i]['Status'] == 'Non Prioritas':
            global hasilData
            hasilData = i
            print_per_baris()
        else:
            continue
    print()

def lihatPrioritas():
    print(judulPerusahaan)
    print(judulTabelNasabah)
    for i in dataNasabah:
        if dataNasabah[i]['Dana Nasabah'] >= 750000000 and dataNasabah[i]['Status'] == 'Prioritas':
            global hasilData
            hasilData = i
            print_per_baris()
        else:
            continue 
    print()


def menu5():
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t\t  Pelayanan Nasabah Prioritas :
          \t\t\t\t\t\t  1. Update Perayaan Bulanan
          \t\t\t\t\t\t  2. Target prioritas
          \t\t\t\t\t\t  3. Data Nasabah Prioritas
          \t\t\t\t\t\t  4. Menu Utama''')
    print()
    try : 
        angka = int(input("\t\t\t\t\t\t\tMasukkan angka : "))
        if angka == 1:
            ulangTahun()
            menu5()
        elif angka == 2:
            targetprioritas()
            menu5()
        elif angka == 3 :
            lihatPrioritas()
            menu5()
        elif angka == 4:
            menuUtama()
        else:
            print(salah)
            menu5()
    except ValueError:
        print("\t\t\t\t\t\t\t Input anda tidak benar. Masukkan angka 1,2, atau 3")
        menu5()

#-----------------------------------MULAI APLIKASI-----------------------------------

dataKaryawan = {
    'GM_PWDK': {'password':'gm123', 'position': 'General Manager'},
    'RT_PWDK': {'password':'rt456','position':'Relations Team'},
    'DT_ASS': {'password': 'data789', 'position': 'Data Team'}
}
aksesPosisi= {
    'General Manager': [1, 2, 3, 4, 5, 6],
    'Relations Team': [1, 5, 6],
    'Data Team' : [1,2,3,5,6]
}



def authenticate(username,password):
        if username in dataKaryawan and dataKaryawan[username]['password'] == password:
            return True, dataKaryawan[username]['position']
        else:
            return False, None

while True:
    print(judulPerusahaan)
    print('''\t\t\t\t\t\t     Silahkan Masukkan ID dan password anda''')
    username = input("\t\t\t\t\t\t\t    Masukkan id karyawan: ")
    password = input("\t\t\t\t\t\t\t    Masukkan password anda: ")
    print()
    authenticated, position = authenticate(username, password)

    if authenticated:
        print(f"\t\t\t\t\t\t Selamat datang, selamat bekerja tim {position}! .")
        hak_akses = aksesPosisi.get(position,[])
        print()
        menuUtama()
        while True :
            angkaUtama = int(input("\t\t\t\t\t\t\t  Masukkan angka : "))
            if angkaUtama in hak_akses:
                if angkaUtama == 1 :
                    menu1()
                elif angkaUtama == 2 :
                    menu2()
                elif angkaUtama == 3:
                    menu3()
                elif angkaUtama == 4:
                    menu4()
                elif angkaUtama == 5:
                    menu5()
                elif angkaUtama == 6 :
                    print('\t\t\t\t\t\t     Anda telah keluar dari sistem database')
                    break
                else : 
                    print('Anda memasukkan angka yang salah : ')
            else :
                print ('\t\t\t\t\t\t     Anda tidak memiliki akses ke menu ini!')
                menuUtama()
    else:
        print("\t\t\t\t\t\t     Username/password anda tidak sesuai! Silahkan coba lagi.")



   























#=================================================================AREA TIDAK TERPAKAI========================================================================
# dataNasabah ={
#     {'id': 2402100700061,'NIK':3678910,'Nama': 'Intania','Tanggal Lahir': '10-07-1992','Tanggal Buat':'19-02-2024','Dana Nasabah':1000000000},
#     {'id':2310120800139,'NIK':3798007,'Nama': 'Nur Komala Saijah','Tanggal Lahir': '12-08-1986','Tanggal Buat':'10-10-2023','Dana Nasabah':1500000000},
#     {'id':2109080400147,'NIK':1800759,'Nama': 'Haris Purwadhana','Tanggal Lahir': '08-04-1994','Tanggal Buat':'09-12-2021','Dana Nasabah':750000000},
#     {'id':2008010500087,'NIK':9007966,'Nama': 'Angel Kumala','Tanggal Lahir': '01-05-1992','Tanggal Buat':'08-08-2020','Dana Nasabah':925000000}
#     }
      
# def merubahData():
#     print(dataNasabah[hasilData][kamar_y]) 
#     if type(dataNasabah[hasilData][kamar_y])== int:
#         ubahDataInteger = int(input("Masukkan data yang ingin anda ubah : "))
#         #-----------------MEMASTIKAN SUDAH BENAR-------------------------
#         dataNasabah[hasilData][kamar_y] = ubahDataInteger
#         print_satu_data()
#         tanyaDulu = input("Berikut data yang ingin anda ubah. Apakah sudah benar? (Y/T):")
#         if tanyaDulu == 'Y':
#             print('Data sudah berhasil dirubah!')
#             lihatData()
#         else :
#             dataNasabah[hasilData][kamar_y] = dataNasabah[hasilData][kamar_y] #!!!TUJUANNYA UNTUK MENGEMBALIKAN DATA LAMA,jadi gak dirubah dulu
#             print(dataNasabah[hasilData][kamar_y]) 
#             cariKolomDanKodeDict()
#     elif type(dataNasabah[hasilData][kamar_y]) == str:
#         ubahDataString= input("Masukkan data yang ingin anda ubah : ")
#         dataNasabah[hasilData][kamar_y] = ubahDataString
#     print('Data anda sudah berhasil diubah')     

# keys_dict_baru = 0

# def ubah_key_dict_baru ():
#     for i in dict_baru.keys():
#         global keys_dict_baru
#         keys_dict_baru = i

# def change_dict_baru_key(d, keys_dict_baru, new_key, default_value=None):
#     d[new_key] = d.pop(keys_dict_baru, default_value)

# def change_dict_baru_value(d, keys_dict_baru):
#     d[keys_dict_baru] = dataNasabah[hasilData]

# ubah_key_dict_baru()
# change_dict_baru_key(dict_baru,keys_dict_baru,hasilData)
# dict_baru[keys_dict_baru]= dataNasabah[hasilData]
# print(dict_baru)
        
# menuUtama()
# while True:
#     angkaUtama = int(input("Masukkan angka : "))
#     if angkaUtama == 1 :
#         menu1()
#     elif angkaUtama == 2 :
#         menu2()
#     elif angkaUtama == 3:
#         menu3()
#     elif angkaUtama == 4:
#         menu4()
#     elif angkaUtama == 5:
#         menu5()
#     elif angkaUtama == 6 :
#         print('Anda telah keluar dari sistem database')
#         break
#     else : 
#         print('Anda memasukkan angka yang salah : ')

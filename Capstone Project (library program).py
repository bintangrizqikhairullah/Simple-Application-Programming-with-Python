from tabulate import tabulate
import os
import math as mt
import random as rd

header=[
    "ID",
    "Jenis",
    "Penulis",
    "Judul",
    "Status",
    "Peminjam"
]


data=[
    ["ISBN-100-85901","Filsafat","INTERNASIONAL","Timaeus and Critias","Dipinjam","G14170060"],
    ["ISBN-100-85912","Filsafat","INTERNASIONAL","Timaeus and Critias","Tersedia","Tidak ada"],
    ["ISBN-200-75121","Finansial","INTERNASIONAL","The Intellegent Investor","Tersedia","Tidak ada"],
    ["ISBN-300-65351","Ilmu Terapan","LOKAL","Pengantar Statistika","Dipinjam","G14160002"],
    ["ISBN-400-45461","Lainnya","LOKAL","Gadis Kretek","Tersedia","Tidak ada"],
    ["ISBN-400-45461","Lainnya","LOKAL","Dilan ","Dipinjam","G14160002"]

]


database_penunjang=[
    [100,200,300,400],
    ["Filsafat","Finansial","Ilmu Terapan","Lainnya"],
    ["INTERNASIONAL","LOKAL"],
    ["Tersedia","Dipinjam"],
]


menu='''Selamat datang di perpustakaan Alexandria, apa yang anda ingin lakukan?\n

1. Lihat daftar buku
2. Menghapus buku dari database
3. Menambahkan buku kedalam database
4. Memperbarui data buku
5. Exit

'''

menu_lihat='''Apakah anda ingin melihat daftar seluruh buku ?\n

1. Ya, lihat seluruh buku
2. Tidak, lihat buku berdasarkaan kriteria tertentu saja\n
'''

menu_lihat_2='''Anda dapat melihat buku berdasarkan kriteria dibawah ini\n

1. Lihat buku berdasarkan id
2. Lihat buku berdasarkan jenis
3. Lihat buku berdasarkan penulis
4. Lihat buku berdasarkan judul
5. Lihat buku berdasarkan status peminjaman
6. Lihat buku berdasarkan peminjam\n
'''


menu_ubah='''Data apa yang anda ingin perbarui?\n
1. Jenis buku
2. Penulis buku
3. Judul buku
4. Status peminjaman buku
5. Peminjam buku \n
'''

def stopper():
    enter_to_continue=input("\nTekan enter untuk melanjutkan: ")
    return enter_to_continue

def melanjutkan_menu(menu):
    while True:
        os.system("cls")
        try:
            if menu==1:
                input_terusan=str(input("\nApakah anda masih ingin melihat buku ? (ya/tidak) : ").lower())
            elif menu==2:
                input_terusan=str(input("\nApakah anda masih ingin menghapus buku ? (ya/tidak) : ").lower()) 
            elif menu==3:
                input_terusan=str(input("\nApakah anda masih ingin menambahkan buku ? (ya/tidak) : ").lower())
            elif menu==4:
                input_terusan=str(input("\nApakah anda masih ingin mengubah data buku ? (ya/tidak) : ").lower())
            if input_terusan=="ya":
                return True
            elif input_terusan=="tidak":
                return False
            else:
                print("\nMohon berikan input yang benar")
                stopper()
        except:
            print("\nMohon berikan input yang benar")

def notifikasi_perubahan(menu,id=""):
    index_=index_checker(id)
    if menu==1:
        print(f"\nBerikut list buku yang anda ingin lihat{id}")
    elif menu==2:
        print(f"\nBuku {id} ({data[index_][3]}) berhasil dihapus")
    elif menu==3:
        print(f"\nBuku {id} ({data[index_][3]}) berhasil ditambahkan")
    elif menu==4:
        print(f"\nData {id} ({data[index_][3]}) buku berhasil diubah")
    elif menu==5:
        print(f"\nStatus peminjaman buku ({id} {data[index_][3]}) berhasil diubah")

def bantuan_untuk_input(kolom):
    if kolom==1:
        print("\nApa jenis dari buku ini ?\n")
    elif kolom==2:
        print("\nBerdasarkan negaranya, penulis buku ini adalah penulis LOKAL atau INTERNASIONAL ?\n")
    elif kolom==3:
        print("\nApa judul dari buku ini ?\n")
    elif kolom==4:
        print("\nApa status peminjaman dari buku ini sekarang ?\n")
    elif kolom==5:
        print("\nMohon masukkan NIM peminjam buku ini\n")

def show_data(opsi="semua",kolom="semua",kriteria="semua",id="semua"):
    os.system("cls")
    if opsi=="semua":
        print(tabulate(data,header))
    elif opsi=="parsial":
        parsial=[]
        for i in range(len(data)):
            if data[i][kolom]==kriteria:
                parsial.append(data[i])
        print(f"\n{tabulate(parsial,header)}")  
    elif opsi=="data yang sedang digunakan saja" :
        index_=index_checker(id)
        print(f"\n{tabulate([data[index_]],header)}")  
    
def id_checker(objek,id):
    list_id=[]
    if objek=="buku":
        kolom=0
    elif objek=="peminjam":
        kolom=4
    for i in range(len(data)):
        list_id.append(data[i][kolom])
    if id not in list_id:
        return False
    else:
        return True 

def index_checker(id):
    for i in range(len(data)):
        if data[i][0]==id:
            return i

def create_id(jenis):
    for i in range(len(database_penunjang[1])):
        if database_penunjang[1][i]==jenis:
            id_baru="ISBN-"+str(database_penunjang[0][i])+"-"+str(rd.randint(10000,99999))
    return id_baru

def list_show(database,kolom):
    os.system("cls")
    unik=[database[0][kolom]]
    for i in range(len(database)):
        if i == 0 :
            continue
        elif database[i][kolom] not in unik:
            unik.append(database[i][kolom])
    for j in range(len(unik)):
        print(f"{j+1}.{unik[j]}")
    return unik

def list_opsi(kolom):
    list_=database_penunjang[kolom]
    for i in range(len(list_)):
        print(f"{i+1}.{list_[i]}")
    return list_

def validasi(attribut,input_):
    if attribut==5:
        if len(input_)!=9 or input_[0].isalpha()==False or input_[1:9].isnumeric()==False:
            print("\nNIM peminjam yang anda masukkan salah, berikut contoh NIM yang valid : G14170090\n")
            return False
        else:
            return True
    elif attribut==3:
        if len(input_)>50 or input_[0:len(input_)].isnumeric()==True or len(input_)==0 :
            print("\nJudul buku tidak boleh lebih dari 50 karakter, tidak boleh angka semua, dan tidak boleh kosong\n")
            return False
        else:
            return True

def new_data(kolom,type_pengisian):
        while True :
            os.system("cls")
            if type_pengisian=="Automatis":
                while True:
                    try:
                        os.system("cls")
                        bantuan_untuk_input(kolom)
                        opsi=list_opsi(kolom)
                        input_pilihan=int(input(f"\nmohon masukkan angka 1 sampai {len(opsi)} untuk mengisi data: "))-1
                        if input_pilihan>len(opsi)-1 or input_pilihan<0:
                            os.system("cls")
                            print(f"\nmohon masukkan angka 1 sampai {len(opsi)} untuk mengisi data")
                            stopper()
                        else:
                            result=opsi[input_pilihan]
                            return result
                    except:
                        os.system("cls")
                        print(f"\ninput harus berupa angka 1 sampai {len(opsi)}")
                        stopper()
            elif type_pengisian=="Manual":
                while True:
                    try:
                        bantuan_untuk_input(kolom)
                        input_manual=str(input("\nMohon masukkan data dengan cara mengetik secara manual: ").lower())
                        result=input_manual.capitalize()
                        if validasi(kolom,result)==True:
                            return result
                        else:
                            stopper()
                            os.system("cls")
                    except:
                        os.system("cls")
                        print("\ninput yang anda masukkan salah")
                        stopper()

while True:
    kondisi=True
    os.system("cls")
    try:
        print(menu)
        input_=int(input("Pilih menu yang anda diinginkan: "))
        if input_>5 or input_<1:
            print(("\nMohon masukkan angka bulat antara 1-5 untuk memilih menu"))
            stopper()
            continue
        elif input_==1:
            while kondisi==True:
                try:
                    os.system("cls")
                    print(menu_lihat)
                    ingin_lihat=int(input("\nPilih 1 untuk melihat semua buku dan 2 untuk melihat sebagian saja: "))
                    if ingin_lihat<=0 or ingin_lihat>3:
                        print("\nMenu yang anda pilih tidak ada")
                    elif ingin_lihat==1:
                        show_data()
                        stopper()
                    elif ingin_lihat==2:
                        while True:
                            try:
                                print(menu_lihat_2)
                                input_kriteria=int(input("\nBerdasarkan kriterianya, buku apa yang anda ingin lihat?"))-1
                                if input_kriteria<0 or input_kriteria>5:
                                    print("\nKriteria yang anda pilih tidak ada")
                                    stopper()
                                else:
                                    while True:
                                        try:
                                            opsi=list_show(data,input_kriteria)
                                            input_opsi=int(input(f"\nmohon masukkan angka 1 sampai {len(opsi)} untuk memilih kriteria buku: "))-1
                                            if input_opsi<0 or input_opsi>len(opsi):
                                                print("\nInput yang anda masukkan salah")
                                            else:
                                                kriteria=opsi[input_opsi]
                                                show_data("parsial",input_kriteria,kriteria,"semua")
                                                stopper()
                                            break
                                        except:
                                            print("\ninput yang anda masukkan salah")
                                            stopper()
                                    break
                            except:
                                print("\nMohon gunakan angka untuk memilih menu")
                                stopper()
                    kondisi=melanjutkan_menu(1)
                except:
                    print("Mohon gunakan angka 1 dan 2 untuk memilih menu")
                    stopper()
        elif input_==2:
            while kondisi==True:
                try:
                    os.system("cls")
                    show_data()
                    input_id=str(input("\nMasukkan id buku yang ingin anda hapus : "))
                    if id_checker("buku",input_id)==True:
                        show_data("data yang sedang digunakan saja","semua","semua",input_id)
                        notifikasi_perubahan(2,input_id)
                        del data[index_checker(input_id)]
                        stopper()
                        kondisi=melanjutkan_menu(2)
                    else:
                        print("\nid buku yang anda masukkan tidak ada")
                        stopper()
                except:
                    print("\nMohon masukkan input yang benar")
                    stopper()
        elif input_==3:
            while kondisi==True:
                try:
                    os.system("cls")
                    jenis_baru=new_data(1,"Automatis")
                    penulis_baru=new_data(2,"Automatis")
                    judul_baru=new_data(3,"Manual")
                    while True:
                        id_baru=create_id(jenis_baru)
                        if id_checker("buku",id_baru)==False:
                            break
                    data.append([id_baru,jenis_baru,penulis_baru,judul_baru,"Tersedia","Tidak ada"])
                    show_data("data yang sedang digunakan saja","semua","semua",id_baru)
                    notifikasi_perubahan(3,id_baru)
                    stopper()
                    kondisi=melanjutkan_menu(3)
                except:
                    print("\nMohon masukkan input yang benar")
                    stopper()
        elif input_==4:
            os.system("cls")
            while kondisi==True:
                try:
                    show_data()
                    input_id=str(input("\nMasukkan id buku yang ingin anda ubah datanya : "))
                    if id_checker("buku",input_id)==True:
                        index_=index_checker(input_id)
                        while True:
                            try:
                                show_data("data yang sedang digunakan saja","semua","semua",input_id)
                                print("")
                                print(menu_ubah)
                                input_kolom=int(input("\nData apa yang anda ingin diubah? "))
                                if input_kolom<1 or input_kolom>5:
                                    os.system("cls")
                                    print("\nMohon gunakan angka 1 sampai 5 untuk memilih menu")
                                    stopper()
                                    continue
                                elif input_kolom==1:
                                    print("\nMohon diperhatikan, pergantian jenis buku akan menyebakan 3 digit pertama pada ID buku berubah")
                                    stopper()
                                    jenis_baru=new_data(input_kolom,"Automatis")
                                    data[index_][input_kolom]=jenis_baru
                                    data[index_][0]=data[index_][0].replace(data[index_][0][5:8],create_id(jenis_baru)[5:8])
                                elif input_kolom==2:
                                    penulis_baru=new_data(input_kolom,"Automatis")
                                    data[index_][input_kolom]=penulis_baru
                                elif input_kolom==3:
                                    judul_baru=new_data(input_kolom,"Manual")
                                    data[index_][input_kolom]=judul_baru
                                elif input_kolom==4:
                                    status_baru=new_data(input_kolom-1,"Automatis")
                                    if status_baru=="Tersedia":
                                        data[index_][5]="Tidak ada"
                                    else:
                                        input_peminjam=new_data(input_kolom+1,"Manual")
                                        data[index_][5]=input_peminjam
                                    data[index_][input_kolom]=status_baru
                                elif input_kolom==5:
                                    if data[index_][4]=="Tersedia":
                                        print("\nBuku ini tidak sedang dalam peminjaman, mohon ubah status peminjamannya terlebih dahulu")
                                        stopper()
                                        continue
                                    else:
                                        peminjam_baru=new_data(input_kolom,"Manual")
                                        data[index_][input_kolom]=peminjam_baru
                                break                                    
                            except:
                                print("\ninput yang anda masukkan salah")
                                stopper()
                        show_data("data yang sedang digunakan saja","semua","semua",data[index_][0])
                        notifikasi_perubahan(4,data[index_][0])
                        stopper()
                        kondisi=melanjutkan_menu(4)
                    else:
                        print("\nid buku yang anda masukkan tidak ada")
                        stopper()
                except:
                    print("\nMohon masukkan input yang benar")
                    stopper()
        elif input_==5:
            break  
        kondisi=True              
    except:
        os.system("cls")
        print("Mohon masukkan angka bulat antara 1-5 untuk memilih menu")
        stopper()


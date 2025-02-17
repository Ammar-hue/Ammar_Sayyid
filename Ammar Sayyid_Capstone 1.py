 # Gudang (data stok) - ElectroHub

daftar_gudang_electroHub = [
    {'Id Barang': 'CX12', 'Nama Barang' : 'HP Samsung', 'Kategori': 'Smartphone', 'Harga': 24000000, 'Stock': 50, 'Supplier': 'Samsung', 'Lokasi_Rak': 'rak 001', 'Status': 'tersedia'},
    {'Id Barang': 'DE12', 'Nama Barang' : 'Laptop HP', 'Kategori': 'Laptop & PC', 'Harga': 15000000, 'Stock': 10, 'Supplier': 'Asus', 'Lokasi_Rak': 'rak 002', 'Status': 'tersedia'},
    {'Id Barang': 'E101', 'Nama Barang' : 'Monitor LG22', 'Kategori': 'Aksesoris', 'Harga': 2500000, 'Stock': 30, 'Supplier': 'LG', 'Lokasi_Rak': 'rak 003', 'Status': 'tersedia'},
    {'Id Barang': 'E787', 'Nama Barang' : 'Printer Epson', 'Kategori': 'Peralatan Kantor', 'Harga': 1900000, 'Stock': 20, 'Supplier': 'Epson', 'Lokasi_Rak': 'rak 004', 'Status': 'tersedia'},
    {'Id Barang': 'E121', 'Nama Barang' : 'TV LG 20"', 'Kategori': 'TV & Audio', 'Harga': 1500000, 'Stock': 0, 'Supplier': 'LG', 'Lokasi_Rak': 'rak 005', 'Status': 'tidak tersedia'},
    {'Id Barang': 'E512', 'Nama Barang' : 'Kulkas Sharp', 'Kategori': 'Elektronik Rumah', 'Harga': 4500000, 'Stock': 25, 'Supplier': 'Sharp', 'Lokasi_Rak': 'rak 006', 'Status': 'tersedia'},
]

from tabulate import tabulate

def menampilkan_daftar_gudang():

    data = []
    index = 0

    if len(daftar_gudang_electroHub) == 0:
        print("\n=== Data Kosong ===")

    for gudang in daftar_gudang_electroHub:
        data.append([
            index,
            gudang["Id Barang"],  
            gudang["Nama Barang"],
            gudang["Kategori"], 
            gudang["Harga"],  
            gudang["Stock"],  
            gudang["Supplier"],  
            gudang["Lokasi_Rak"],
            gudang["Status"],  
        ])
        index += 1
         
    print("\nDaftar Gudang ElectroHub\n")
    print(tabulate(data, headers=["Index","Id Barang", "Nama Barang", "Kategori", "Harga", "Stock", "Supplier","Lokasi_Rak", "Status"], tablefmt="grid"))
    print()

#===================================================================================================

def cari_id_barang(mencari_id):
    return mencari_id['Id Barang'].lower() == filter_id.lower()

#===================================================================================================

def filter_kategori_barang(mencari_kategori):
    return mencari_kategori['Kategori'].lower() == filter_kategori.lower()

def filter_status_barang(mencari_status):
    return mencari_status['Status'].lower() == filter_status.lower()

def filter_supplier_barang(mencari_supplier):
    return mencari_supplier['Supplier'].lower() == filter_supplier.lower()



def menu_filter():
    global filter_kategori, filter_status, filter_supplier
    while True:
        pilihan_filter = input('''
 Pilih filter:
                            
    1. Kategori
    2. Status
    3. Supplier
    4. Menu Utama
                                
Masukkan pilihan (a/b/c/d): ''')
        

        if pilihan_filter == '1':
            filter_kategori = input("Masukkan Kategori Barang: ").strip().lower()
            hasil_filter_kategori_dalam_list = list(filter(filter_kategori_barang, daftar_gudang_electroHub))

            if hasil_filter_kategori_dalam_list:
                 print("Hasil filter berdasarkan Kategori Barang: ")
                 for item in hasil_filter_kategori_dalam_list:
                    print(f"{item['Id Barang']} - {item['Nama Barang']} - {item['Kategori']} - (Rp.{item['Harga']}) - {item['Stock']} - {item['Supplier']} - {item['Lokasi_Rak']} - {item['Status']}")
                    read_menu()
                    return
            else:
                print("Barang dengan kategori tersebut tidak ditemukan. coba lagi sesuai list tertera.")
                read_menu()
                return

        elif pilihan_filter == '2':
            filter_status = input("Masukkan status barang (tersedia/tidak tersedia): ").strip().lower()
            
            if filter_status not in ["tersedia", "tidak tersedia"]:
                print("Status tidak valid, masukkan status barang (Tersedia/Tidak Tersedia).")
            
            hasil_filter_status_dalam_list = list(filter(filter_status_barang, daftar_gudang_electroHub))

            if hasil_filter_status_dalam_list:
                print("Hasil filter berdasarkan status: ")
                for item in hasil_filter_status_dalam_list:
                    print(f"{item['Id Barang']} - {item['Nama Barang']} - {item['Kategori']} - (Rp.{item['Harga']}) - {item['Stock']} - {item['Supplier']} - {item['Lokasi_Rak']} - {item['Status']}")
                    read_menu()
                    return
            else:
                print("Status tidak valid, masukkan status barang (tersedia/tidak tersedia).")
                read_menu()
                return

        elif pilihan_filter == '3':
            filter_supplier = input("Masukkan Nama Barang: ").strip().lower()
            hasil_filter_supplier_dalam_list = list(filter(filter_supplier_barang, daftar_gudang_electroHub))

            if hasil_filter_supplier_dalam_list:
                 print("Hasil filter berdasarkan Kategori Barang: ")
                 for item in hasil_filter_supplier_dalam_list:
                    print(f"{item['Id Barang']} - {item['Nama Barang']} - {item['Kategori']} - (Rp.{item['Harga']}) - {item['Stock']} - {item['Supplier']} - {item['Lokasi_Rak']} - {item['Status']}")
                    read_menu()
                    return
            else:
                print("Barang dengan Supplier tersebut tidak ditemukan. coba lagi sesuai list tertera.")
                read_menu()
                return
        
        elif pilihan_filter == '4':
            print("Kembali ke menu utama")
            return
        else:
            print("Pilihan tidak valid")
            read_menu()
            return
            
#====================================================================================================

def menambah_daftar_gudang():
    while True:
        menambah_id_barang = input("Masukkan id barang: ").strip().lower()
        for item in daftar_gudang_electroHub:
            if item['Id Barang'].lower() == menambah_id_barang:
                print("Id barang sudah ada. Barang tidak bisa ditambahkan")
                create_menu()
                return

        menambah_nama_barang = input("Masukkan nama barang: ")
        
        while True:
            menambah_kategori_lokasi = input('''                
                Pilihan Kategori:
                1. Smartphone (rak 001)
                2. Laptop & PC (rak 002)
                3. Aksesoris (rak 003)
                4. Peralatan Kantor (rak 004)
                5. TV & Audio (rak 005)
                6. Elektronik Rumah (rak 006)
                7. Menambahkan kategori dan lokasi baru
                               
                Masukkan pilihan (1/2/3/4/5/6)''')
        
            if menambah_kategori_lokasi == '1':
                kategori = 'Smartphone'
                lokasi_penyimpanan = 'rak 001'
                break
            elif menambah_kategori_lokasi == '2':
                kategori = 'Laptop & PC'
                lokasi_penyimpanan = 'rak 002'
                break
            elif menambah_kategori_lokasi == '3':
                kategori = 'Aksesoris'
                lokasi_penyimpanan = 'rak 003'
                break
            elif menambah_kategori_lokasi == '4':
                kategori = 'Peralatan Kantor'
                lokasi_penyimpanan = 'rak 004'
                break
            elif menambah_kategori_lokasi == '5':
                kategori = 'TV & Audio'
                lokasi_penyimpanan = 'rak 005'
                break
            elif menambah_kategori_lokasi == '6':
                kategori = 'Elektronik Rumah'
                lokasi_penyimpanan = 'rak 006'
                break
            elif menambah_kategori_lokasi == '7':
                kategori_baru = input("Masukkan kategori baru: ")
                if kategori_baru in ['Smartphone','Laptop & PC', 'Aksesoris', 'Peralatan Kantor', 'TV & Audio', 'Elektronik Rumah']:
                    print("Kategori sudah ada, Silahkan pilih kategori lain")
                    create_menu()
                    return
                else:
                    print(f"Kategori baru berhasil ditambahkan ({kategori_baru})")
                    kategori = kategori_baru
                
                lokasi_penyimpanan = input("Masukkan lokasi rak baru dengan format ('rak X'): ")
                if "rak" in lokasi_penyimpanan.lower():
                    print("Lokasi rak valid.")
                    break
                else:
                    print("Lokasi rak tidak valid")
                    create_menu()
                    return
            else:
                print("Kategori tidak valid. Silahkan masukkan pilihan (1/2/3/4/5/6).")
                create_menu()
                return
        
        while True:
            try:
                menambah_harga = int(input("Masukkan harga barang: "))
                if menambah_harga < 0:
                    print("Harga tidak boleh negatif")
                    create_menu()
                    return
                break
            except ValueError:
                print("Input harus angka, coba lagi.")
                create_menu()
                return

        while True:
            try:
                menambah_stock = int(input("Masukkan stock barang: "))
                if menambah_stock < 0:
                    print("Stock tidak boleh negatif. Coba lagi")
                    create_menu()
                    return
                break
            except ValueError:
                print("Input harus angka, coba lagi.")
                create_menu()
                return


        menambah_supplier = input("Masukkan nama supplier: ")

        
        if menambah_stock > 0:
            menambah_status_stock = "tersedia"
        else:
            menambah_status_stock = "tidak tersedia"


        barang_baru = {
        'Id Barang': menambah_id_barang,
        'Nama Barang' : menambah_nama_barang,
        'Kategori': kategori,
        'Harga': menambah_harga,
        'Stock': menambah_stock,
        'Supplier': menambah_supplier,
        'Lokasi_Rak': lokasi_penyimpanan,
        'Status': menambah_status_stock
        }
        
        while True:
            simpan_barang = input("Simpan data? (ya/tidak)").strip().lower()
            if simpan_barang == 'ya':
                daftar_gudang_electroHub.append(barang_baru)
                print(f"Barang {menambah_nama_barang} berhasil ditambahkan")
                create_menu()
                return
            elif simpan_barang == 'tidak':
                break
            else:
                print("Input tidak valid. mohon ketik ulang (ya/tidak)")
        break 


#====================================================================================================

def menghapus_daftar_gudang():
    while True:         
    
        id_barang = input("Masukkan id barang yang ingin dihapus: ").strip().lower()
        for item in daftar_gudang_electroHub:
            if item['Id Barang'].lower() == id_barang:
                hapus_data = input("Apakah anda yakin ingin menghapus data? (ya/tidak)").strip().lower()
                if hapus_data == 'ya':
                    daftar_gudang_electroHub.remove(item)
                    print(f"\n ~~~ Barang dengan id ({id_barang}) berhasil dihapus ~~~")
                    delete_menu()
                    return
                elif hapus_data == 'tidak':
                    print("\n~~~ Hapus barang dibatalkan ~~~")
                    break
                else:
                    print("Input tidak valid. mohon ketik ulang (ya/tidak)")
                    delete_menu()
                    return 
        
        print("Id barang tidak valid.")
        delete_menu()
        return

#====================================================================================================

def update_daftar_gudang():
    while True:
        update_id_barang = input("Masukkan id barang: ").strip().lower()
        for item in daftar_gudang_electroHub:
            if item['Id Barang'].lower() == update_id_barang:
                data_sebelum_update = item.copy()
                print("Data barang saat ini: ")
                print(f"{item['Id Barang']} - {item['Nama Barang']} - {item['Kategori']} - (Rp.{item['Harga']}) - {item['Stock']} - {item['Supplier']} - {item['Lokasi_Rak']} - {item['Status']}")
            
                penawaran_lanjut = input("Lanjutkan Update? (ya/tidak)").strip().lower()
                if penawaran_lanjut == 'ya':

                        print("\nKolom yang dapat diupdate: Nama Barang, Kategori, Harga, Stock, Supplier, Lokasi_Rak.")
                        pilih_kolom = input("\nSilahkan pilih kolom yang ingin di update: ").strip().lower()

                        if pilih_kolom == 'nama barang':
                            item['Nama Barang'] = input("Masukkan nama barang yang baru: ")
    
                        elif pilih_kolom == 'kategori':
                            print("\nKategori yang dapat diupdate: Smartphone, Laptop & PC, Aksesoris, Peralatan Kantor, TV & Audio, Elektronik Rumah")
                            
                            kategori_baru = input("\nMasukkan kategori yang baru: ").split()
                            if item['Kategori'] in ['Smartphone','Laptop & PC', 'Aksesoris', 'Peralatan Kantor', 'TV & Audio', 'Elektronik Rumah']:
                                print("Pilih kategori yang tersedia")
                                update_menu()
                                return
                            else:
                                item['Kategori'] = kategori_baru
                                print(f"Kategori baru berhasil ditambahkan ({item['Kategori']})")
                        
                        elif pilih_kolom == 'Lokasi_Rak':
                            item['Lokasi_Rak'] = input("Masukkan kategori yang baru: ")

                        elif pilih_kolom == 'harga':
                            while True:
                                try:
                                    item['Harga'] = int(input("Masukkan harga barang yang baru: "))
                                    if item['Harga'] < 0:
                                        print("Harga tidak boleh negatif. Coba lagi")
                                    else:
                                        break
                                except ValueError:
                                    print("Harga harus berupa angka. Coba lagi.")
                        
                        elif pilih_kolom == 'stock':
                            while True:
                                try:
                                    item['Stock'] = int(input("Masukkan jumlah stock barang yang baru: "))
                                    if item['Stock'] < 0:
                                        print("Stock tidak boleh negatif. Coba lagi")
                                    else:
                                        break
                                except ValueError:
                                    print("Stock harus berupa angka. Coba lagi.")

                        elif pilih_kolom == 'supplier':    
                            item['Supplier'] = input("Masukkan nama supplier yang baru: ")
                    
                            if item['Stock'] > 0:
                                item['Status'] = "tersedia"
                            else:
                                item['Status'] = "tidak tersedia"
                        else:
                            print("Input tidak valid. Kolom yang dapat diupdate: Nama Barang, Kategori, Harga, Stock, Supplier, Lokasi_Rak.")
                            break

                        simpan_update = input("Simpan data yang di update? (ya/tidak)").strip().lower()
                        if simpan_update == 'ya':
                            print("~~~ Data berhasil diperbarui ~~~")
                            create_menu()
                            return
                        elif simpan_update == 'tidak':
                            for key, value in data_sebelum_update.items():
                                item[key] = value
                            print("~~~ Update dibatalkan ~~~")
                            create_menu()
                            return
                        else:
                            for key, value in data_sebelum_update.items():
                                item[key] = value
                            print("Input tidak valid. Mohon ketik ulang (ya/tidak).")       
                    
                elif penawaran_lanjut == 'tidak':
                    print("Anda tidak jadi update data gudang")
                    update_menu()
                    return
                else:
                    print("Input tidak valid. Mohon ketik ulang (ya/tidak).")
                update_menu()
                return
        
        print("Id barang tidak ditemukan.")
        return
#====================================================================================================

def read_menu():
        global filter_id
        print("\n=== Pilihan Read Menu ===")
        print("1. Menampilkan data gudang")
        print("2. Cari berdasarkan id")
        print("3. Filter data")
        print("4. Menu Utama")
        try:
            pilihan_menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
            if pilihan_menu == 1:
                menampilkan_daftar_gudang()
                read_menu()
                return

            elif pilihan_menu == 2:
                filter_id = input("Masukkan Id Barang: ").strip()
                hasil_filter_id_dalam_list = list(filter(cari_id_barang, daftar_gudang_electroHub))
    
                if hasil_filter_id_dalam_list:
                    print("Hasil filter berdasarkan Id Barang: ")
                    for item in hasil_filter_id_dalam_list:
                        print(f"{item['Id Barang']} - {item['Nama Barang']} - {item['Kategori']} - ({item['Harga']}) - {item['Stock']} - {item['Supplier']} - {item['Lokasi_Rak']} - {item['Status']}")
                        read_menu()
                        return
                else:
                    print("Id tidak tersedia. Masukkan id barang sesuai list tertera.")
                    read_menu()
                    return

            elif pilihan_menu == 3:
                menu_filter()
            elif pilihan_menu == 4:
                return
            else:
                print("Input tidak valid, masukkan angka 1/2/3/4/5")
        except ValueError:
            print("Masukkan angka yang valid")
            read_menu()
            return

#====================================================================================================

def create_menu():
        print("\n=== Pilihan Create Menu ===")
        print("1. Menambahkan data gudang")
        print("2. Menu Utama")
        try:
            pilihan_menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
            if pilihan_menu == 1:
                menambah_daftar_gudang()
            elif pilihan_menu == 2:
                return
            else:
                print("Input tidak valid, masukkan angka 1/2")
        except ValueError:
            print("Masukkan angka yang valid")
            create_menu()
            return

#====================================================================================================

def update_menu():
        print("\n=== Pilihan Update Menu ===")
        print("1. Update data gudang")
        print("2. Menu Utama")
        try:
            pilihan_menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
            if pilihan_menu == 1:
                update_daftar_gudang()
            elif pilihan_menu == 2:
                return
            else:
                print("Input tidak valid, masukkan angka 1/2")
        except ValueError:
            print("Masukkan angka yang valid")
            update_menu()
            return

#====================================================================================================

def delete_menu():
        print("\n=== Pilihan Delete Menu ===")
        print("1. Hapus data gudang")
        print("2. Menu Utama")
        try:
            pilihan_menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
            if pilihan_menu == 1:
                menghapus_daftar_gudang()
            elif pilihan_menu == 2:
                return
            else:
                print("Input tidak valid, masukkan angka 1/2")
        except ValueError:
            print("Masukkan angka yang valid")
            return

#====================================================================================================

def menu_utama():
    while True:
        print("\nSelamat Datang di electroHub")

        print("\nMenu Utama =")
        print("1. Read Menu")
        print("2. Create Menu")
        print("3. Update Menu")
        print("4. Delete Menu")
        print("5. Exit Program")
        try:
            pilihan_menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
            if pilihan_menu == 1:
                read_menu()
            elif pilihan_menu == 2:
                create_menu()
            elif pilihan_menu == 3:
                update_menu()
            elif pilihan_menu == 4:
                delete_menu()
            elif pilihan_menu == 5:
                print("\n~~~ Program Dimatikan ~~~")
                break
            else:
                print("Input tidak valid, masukkan angka 1/2/3/4/5")
        except ValueError:
            print("Masukkan angka yang valid")
menu_utama()
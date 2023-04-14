#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = ""
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE db_V3922040")


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "db_V3922040"
)

cursorObject = dataBase.cursor()

DataBarang   =  """CREATE TABLE `DATA STOK BARANG` (
                   Id_Barang VARCHAR(14) PRIMARY KEY,
                   `Nama Barang` VARCHAR(50),
                   `Harga Barang` INT,
                   `Stok Awal` INT,
                   `Barang Masuk` INT,
                   `Barang Keluar` INT,
                   `Stok Akhir` INT
                   )"""

cursorObject.execute(DataBarang)
dataBase.close()


# In[4]:


import mysql.connector

#Koneksi ke database
dataBase = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'db_V3922040'
)

cursorObject = dataBase.cursor()

# Tambah Data

def insert_data( Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir ):
    sql = "INSERT INTO `DATA STOK BARANG` (`Id_Barang`, `Nama Barang`, `Harga Barang`, `Stok Awal`, `Barang Masuk`, `Barang Keluar`, `Stok Akhir`)            VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")
    
# Melihat Data

def show_data():
    query = "SELECT * FROM `DATA STOK BARANG`"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")
    
# Edit Data

def update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir):
    sql = "UPDATE `DATA STOK BARANG` SET `Nama Barang` = %s, `Harga Barang` = %s, `Stok Awal` = %s, `Barang Masuk` = %s, `Barang Keluar` = %s, `Stok Akhir` = %s WHERE `Id_Barang` = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

# Hapus Data

def delete_data(Id_Barang):
    sql = "DELETE FROM `DATA STOK BARANG` WHERE `Id_Barang` = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")
    
# Mencari Data

def search_data(id_barang):
    sql = "SELECT * FROM `DATA STOK BARANG` WHERE `Id_Barang` = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    
    myresult = cursorObject.fetchall()
    
    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil dicari")
    
while True:
    print(" ")
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Cari data")
    print("6. Keluar")
    print("-------------------")
    menu = input("Pilih menu> ") #input untuk pilihan menu yang akan dicari
    print(" ")
    
    if menu == "1":
            Id_Barang = input("Masukkan Id Barang : ")
            Nama_Barang = input("Masukkan Nama Barang : ")
            Harga_Barang = int(input("Masukkan Harga Barang : "))
            Stok_Awal = int(input("Masukkan Stok Awal : "))
            Barang_Masuk = int(input("Masukkan Barang Masuk : "))
            Barang_Keluar = int(input("Masukkan Barang Keluar : "))

            #Rumus untuk mencari stok_akhir
            Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar

            #mencetak Stok_Akhir dari rumus sebelumnya
            print("Stok Akhir : ", Stok_Akhir)

            insert_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    elif menu == "2":
            show_data()

    #pilihan 3 "update data"
    elif menu == "3":
        Id_Barang = input("Masukkan Id Barang yang akan diupdate : ")
        Nama_Barang = input("Masukkan Nama Barang baru : ")
        Harga_Barang = int(input("Masukkan Harga Barang baru : "))
        Stok_Awal = int(input("Masukkan Stok Awal baru : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk baru : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar baru : "))
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        print("Stok Akhir setelah diupdate : ", Stok_Akhir)
        
        update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

         #pilihan 4 "hapus data"
    elif menu == "4":
        Id_Barang = input("Masukkan Id Barang yang ingin dihapus : ")
        
        delete_data(Id_Barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        Id_Barang = input("Masukkan Id Barang yang ingin dicari : ")
        
        search_data(Id_Barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Terimakasih, SEMOGA ANDA TIDAK PUSING :) ")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilihan anda tidak valid, Mohon coba lagi dan pilihlah dengan benar")


# In[ ]:





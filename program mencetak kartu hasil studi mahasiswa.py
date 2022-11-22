#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:01:41 2022

Program mencetak kartu hasil studi mahasiswa
@author: sonyaridesia
"""


def Matkul():
        nama = input("Nama mahasiswa: ")
        while True: #nim
            nim = input("NIM: ")
            if nim == "":
                print("Nim tidak boleh kosong")
                continue
            elif not nim.isnumeric():
                print("Masukan nomor saja")
                continue
            else:
                break

        SKS = {
            'IKL201 Algoritma dan Pemrograman': 2,
            'IUM203 Aljabar Linier': 2,
            'UBN200 Bahasa Indonesia': 2,
            'UBA200 Bahasa Inggris': 2,
            'IUC201 Computational Thinking': 2,
            'IUM201 Kalkulus Dasar': 2,
            'IKH301 Organisasi Komputer': 3,
            'IKB207 Pengantar Teknologi Informasi': 2,
            'IUM306 Struktur Diskrit': 3
            }
        Bobot = {
            'A': 4.0,
            'A-': 3.75,
            'B+': 3.5,
            'B': 3.0,
            'B-': 2.75,
            'C+': 2.5,
            'C': 2.0,
            'D': 1.0,
            'E': 0.0
            }

        jumlah_sks = 0
        jumlah_bobot = 0
        for matkul, sks in SKS.items():
            while True:
                nilai = input(f'Masukkan nilai huruf {matkul}: ').upper()
                if nilai in Bobot:
                    break
                else:
                    print('Masukkan nilai huruf A, A-, B+, B, B-, C+, C, D, atau E')
            jumlah_sks += sks
            jumlah_bobot += sks * Bobot[nilai]
        ips = jumlah_bobot / jumlah_sks
        print(f'\n{nama} ({nim}) memiliki IPS {ips:.2f}\n')
Matkul()

def end():
    end = input("Apakah masih ada data yang akan dihitung [Y/T]? ").upper()        
    if (end == "T"):
        print()
        print("Terima kasih telah menggunakan program mencetak kartu hasil studi mahasiswa.")
        return 0

    elif (end == "Y"):
        print()
        Matkul()

    else:
        print("Mohon dijawab dengan Y atau T")
        return end()
end()
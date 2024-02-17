import os

# Inisialisasi variabel
uang_masuk = []
uang_keluar = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_list_uang_masuk():
    print("\n=== List Uang Masuk ===")
    for transaksi in uang_masuk:
        print(f"{transaksi}")

def tampilkan_list_uang_keluar():
    print("\n=== List Uang Keluar ===")
    for transaksi in uang_keluar:
        print(f"{transaksi}")

def tampilkan_jumlah_uang_masuk():
    total_uang_masuk = sum(uang_masuk)
    print(f"\nJumlah Uang Masuk: {total_uang_masuk}")

def tampilkan_jumlah_uang_keluar():
    total_uang_keluar = sum(uang_keluar)
    print(f"\nJumlah Uang Keluar: {total_uang_keluar}")

def tampilkan_selisih_uang_masuk_keluar():
    total_uang_masuk = sum(uang_masuk)
    total_uang_keluar = sum(uang_keluar)
    selisih = total_uang_masuk - total_uang_keluar
    print(f"\nUang Masuk - Uang Keluar: {selisih}")

# Loop utama
while True:

    # Menampilkan menu
    print("=== Aplikasi Pencatatan Keuangan ===")
    print("1. Catat Uang Masuk")
    print("2. Catat Uang Keluar")
    print("3. Tampilkan List Uang Masuk")
    print("4. Tampilkan List Uang Keluar")
    print("5. Tampilkan Jumlah Uang Masuk")
    print("6. Tampilkan Jumlah Uang Keluar")
    print("7. Tampilkan Uang Masuk - Uang Keluar")
    print("8. Keluar")

    # Input pilihan
    pilihan = input("Masukkan pilihan (1-8): ")

    # Proses pilihan
    if pilihan == '1':
        jumlah = float(input("Masukkan jumlah uang masuk: "))
        uang_masuk.append(jumlah)
    elif pilihan == '2':
        jumlah = float(input("Masukkan jumlah uang keluar: "))
        uang_keluar.append(jumlah)
    elif pilihan == '3':
        tampilkan_list_uang_masuk()
    elif pilihan == '4':
        tampilkan_list_uang_keluar()
    elif pilihan == '5':
        tampilkan_jumlah_uang_masuk()
    elif pilihan == '6':
        tampilkan_jumlah_uang_keluar()
    elif pilihan == '7':
        tampilkan_selisih_uang_masuk_keluar()
    elif pilihan == '8':
        print("Terima kasih, sampai jumpa!")
        break
    else:
        input("Pilihan tidak valid. Tekan Enter untuk melanjutkan...")

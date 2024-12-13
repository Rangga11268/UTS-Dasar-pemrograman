# Daftar bus dan kategori
bus_list = [  # List
    ("Bus J99 Gundam", "Dream Class", 450000, 21, "07:30"),  # Tuple
    ("Bus J99 Woody", "Dream Coach", 350000, 18, "15:00"),  # Tuple
    ("Bus J99 Shinchan", "Private Class", 750000, 11, "14:30"),  # Tuple
    ("Bus J99 Tweety", "Dream Class", 350000, 24, "14:30"),  # Tuple
    ("Bus J99 Aladdin", "Private Class", 450000, 11, "07:30"),  # Tuple
]

# Menampilkan informasi awal
print("+" + "=" * 95 + "+")  # String, Operator
print("|                   <-----------Selamat datang di PO Juragan 99----------->     \t\t|")  # String
print("|  Rute: Malang ke Jakarta                                                      \t\t|")  # String
print("|  Jarak: 750 km                                                                \t\t|")  # String, Bilangan
print("|  Waktu Perjalanan: 15 jam                                                     \t\t|")  # String, Bilangan
print("+" + "=" * 95 + "+")  # String, Operator
print("| Daftar Bus:                                                                                  \t|")  # String
print("+" + "=" * 95 + "+")  # String, Operator
print("| No  | Nama Bus 🚍       | Kategori 📃    | Harga 🎫    | Kursi 💺 \t| Jam Keberangkatan ⏰\t|")  # String
print("+" + "=" * 95 + "+")  # String, Operator

# Menampilkan daftar bus dalam format tabel
index = 1  # Bilangan
for bus in bus_list:  # Perulangan
    nama_bus, kategori, harga, kursi, jam_keberangkatan = bus  # Tuple
    print("|", f"{index:<3}|", f"{nama_bus:<15}|", f"{kategori:<15}| Rp", f"{harga:<9}\t|", f"{kursi:<9}\t|", f"{jam_keberangkatan:<20}\t|")  # String, Operator
    index += 1  # Operator

print("+" + "=" * 95 + "+")  # String, Operator

# Memilih bus
valid_input = False  # Boolean
while not valid_input:  # Percabangan, Perulangan
    pilihan_bus_input = input("\nPilih bus (1-5) atau ketik 0 untuk keluar: ")  # String
    if len(pilihan_bus_input) > 0:  # Percabangan
        pilihan_bus = 0  # Bilangan
        for char in pilihan_bus_input:  # Perulangan
            if char < '0' or char > '9':  # Percabangan
                pilihan_bus = -1  # Bilangan
                break  # Break
        if pilihan_bus == 0:  # Percabangan
            pilihan_bus = int(pilihan_bus_input)  # Operator, Bilangan
            if 0 <= pilihan_bus <= len(bus_list):  # Percabangan
                valid_input = True  # Boolean
            else:
                print("Pilihan tidak valid, silakan coba lagi.")  # String
        else:
            print("Input tidak valid, silakan masukkan angka.")  # String
    else:
        print("Input tidak valid, silakan coba lagi.")  # String

if pilihan_bus == 0:  # Percabangan
    print("Terima kasih telah menggunakan layanan kami!")  # String
else:
    bus_terpilih, kategori_terpilih, harga_per_tiket, jumlah_kursi, jam_keberangkatan = bus_list[pilihan_bus - 1]  # Tuple, List

    # Memilih jumlah tiket
    valid_input = False  # Boolean
    while not valid_input:  # Percabangan, Perulangan
        jumlah_tiket_input = input("Masukkan jumlah tiket yang ingin dibeli (maksimal " + str(jumlah_kursi) + "): ")  # String, Bilangan
        if len(jumlah_tiket_input) > 0:  # Percabangan
            jumlah_tiket = 0  # Bilangan
            for char in jumlah_tiket_input:  # Perulangan
                if char < '0' or char > '9':  # Percabangan
                    jumlah_tiket = -1  # Bilangan
                    break  # Break
            if jumlah_tiket == 0:  # Percabangan
                jumlah_tiket = int(jumlah_tiket_input)  # Operator, Bilangan
                if 1 <= jumlah_tiket <= jumlah_kursi:  # Percabangan
                    valid_input = True  # Boolean
                else:
                    print("Jumlah tiket tidak valid, silakan coba lagi.")  # String
            else:
                print("Input tidak valid, silakan masukkan angka.")  # String
        else:
            print("Input tidak valid, silakan coba lagi.")  # String

    # Memilih nama
    nama_pembeli = input("Masukkan nama Anda: ")  # String

    # Memilih metode pembayaran
    metode_pembayaran = ""  # String
    while metode_pembayaran not in ["1", "2"]:  # Percabangan, Perulangan
        metode_pembayaran = input("Pilih metode pembayaran (1. Tunai💵 / 2. Kartu Kredit💳): ")  # String

    # Memilih diskon (hanya untuk tiket lebih dari 3)
    diskon = 0  # Bilangan
    if jumlah_tiket > 3:  # Percabangan
        diskon = 0.1  # Bilangan, Operator

    # Menghitung total harga
    total_harga = harga_per_tiket * jumlah_tiket  # Operator, Bilangan
    if diskon > 0:  # Percabangan
        total_harga -= total_harga * diskon  # Operator, Bilangan

    # Memilih kursi
    kursi_list = ["Kursi " + str(i) for i in range(1, jumlah_kursi + 1)]  # List, Bilangan
    print("\nDaftar Kursi:")  # String
    print("+" + "=" * 72 + "+")  # String, Operator
    for i in range(len(kursi_list)):  # Perulangan
        print("|", f"{kursi_list[i]:<69} |")  # String, Operator
    print("+" + "=" * 72 + "+")  # String, Operator

    kursi_terpilih = []  # List
for i in range(jumlah_tiket):  # Perulangan
    valid_kursi = False  # Boolean
    while not valid_kursi:  # Percabangan, Perulangan
        kursi = input("Pilih kursi untuk tiket " + str(i + 1) + ": ")  # String
        if kursi in kursi_list and kursi not in kursi_terpilih:  # Percabangan
            valid_kursi = True  # Boolean
            kursi_terpilih.append(kursi)  # List
        else:
            print("Kursi tidak valid atau sudah dipilih, silakan coba lagi.")  # String
            continue  # Skip ke iterasi berikutnya dari loop untuk meminta input kursi yang baru


# Struk tiket

print("\n" + "+" + "=" * 72 + "+")  # String, Operator
print("|                         🎟️ STRUK TIKET 🎟️                                |")  # String
print("+" + "=" * 72 + "+")  # String, Operator
print(f"| Nama Pembeli       : {nama_pembeli:<50}  \b\b|")  # String, Operator
print(f"| Nama Bus           : {bus_terpilih:<50}  \b\b|")  # String, Operator
print(f"| Kategori           : {kategori_terpilih:<50}|")  # String, Operator
print(f"| Jumlah Tiket       : {jumlah_tiket:<50}  \b\b|")  # String, Operator

kursi_str = ""  # String
for i in range(len(kursi_terpilih)):  # Perulangan
    kursi_str += kursi_terpilih[i]  # String, Operator
    if i < len(kursi_terpilih) - 1:  # Percabangan
        kursi_str += ", "  # String
print(f"| Kursi yang Dipilih : {kursi_str:<50} \b|")  # String, Operator

print(f"| Harga per Tiket    : Rp {harga_per_tiket:<47} \b\b |")  # String, Operator
if diskon > 0:  # Percabangan
    print(f"| Diskon             : {diskon * 100}% {'':<43} \b |") # String, Operator
print(f"| Jam Keberangkatan  : {jam_keberangkatan:<50}  \b\b\b |")  # String, Operator
print(f"| Total Harga        : Rp {total_harga:<45}   \b\b |")  # String, Operator
print(f"| Jarak Tempuh       : 750 km                           \t\t |")  # String, Bilangan
print(f"| Perkiraan Waktu    : 15 jam                           \t\t |")  # String, Bilangan
print("+" + "=" * 72 + "+")  # String, Operator
print("|   Terima kasih telah membeli tiket di PO Juragan 99!🎉                 |")  # String
print("+" + "=" * 72 + "+")  # String, Operator 
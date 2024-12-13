# Daftar bus dan kategori
bus_list = [  # List
    ("Bus J99 Gundam", "Dream Class", 450000, 21, "07:30"),  # Tuple
    ("Bus J99 Woody", "Dream Coach", 350000, 18, "15:00"),  # Tuple
    ("Bus J99 Shinchan", "Private Class", 750000, 11, "14:30"),  # Tuple
    ("Bus J99 Tweety", "Dream Class", 450000, 24, "14:30"),  # Tuple
    ("Bus J99 Aladdin", "Private Class", 750000, 11, "07:30"),  # Tuple
]

# Menampilkan informasi awal
print("+" + "=" * 95 + "+")  # String
print("|                   <-----------Selamat datang di PO Juragan 99----------->     \t\t|")  # String
print("|  Rute: Malang ke Jakarta                                                      \t\t|")  # String
print("|  Jarak: 750 km                                                                \t\t|")  # String, Bilangan
print("|  Waktu Perjalanan: 15 jam                                                     \t\t|")  # String, Bilangan
print("+" + "=" * 95 + "+")  # String
print("| Daftar Bus:                                                                                  \t|")  # String
print("+" + "=" * 95 + "+")  # String, 
print("| No  | Nama Bus 🚍       | Kategori 📃    | Harga 🎫    | Kursi 💺 \t| Jam Keberangkatan ⏰\t|")  # String
print("+" + "=" * 95 + "+")  # String

# Menampilkan daftar bus dalam format tabel
index = 1  # Bilangan
for bus in bus_list:  # Perulangan
    nama_bus, kategori, harga, kursi, jam_keberangkatan = bus  # Tuple
    print("|", f"{index:<3}|", f"{nama_bus:<15}|", f"{kategori:<15}| Rp", f"{harga:<9}\t|", f"{kursi:<9}\t|", f"{jam_keberangkatan:<20}\t|")  # String, Operator
    index += 1  # Bilangan, Operator

print("+" + "=" * 95 + "+")  # String, Operator

# Memilih bus
valid_input = False  # Boolean
while not valid_input:  # Percabangan, Perulangan
    pilihan_bus_input = input("\nPilih bus (1-5) atau ketik 0 untuk keluar: ")  # String
    pilihan_bus = 0  # Bilangan
    if len(pilihan_bus_input) > 0:  # Percabangan
        pilihan_bus = 0  # Bilangan
        for char in pilihan_bus_input:  # Perulangan
            if char < '0' or char > '9':  # Percabangan
                pilihan_bus = -1  # Bilangan
                break  # Break
        if pilihan_bus != -1:  # Percabangan
            pilihan_bus = int(pilihan_bus_input)  # Bilangan, Operator
            if 0 <= pilihan_bus <= len(bus_list):  # Percabangan
                valid_input = True  # Boolean
            else:
                print("Pilihan tidak valid, silakan coba lagi.")  # String
                continue  # Continue
        else:
            print("Input tidak valid, silakan masukkan angka.")  # String
            continue  # Continue
    else:
        print("Input tidak valid, silakan coba lagi.")  # String
        continue  # Continue

if pilihan_bus == 0:  # Percabangan
    print("Terima kasih telah menggunakan layanan kami!")  # String
else:
    bus_terpilih, kategori_terpilih, harga_per_tiket, jumlah_kursi, jam_keberangkatan = bus_list[pilihan_bus - 1]  # Tuple, List

    # Memilih jumlah tiket
    valid_input = False  # Boolean
    while not valid_input:  # Perulangan, Percabangan
        jumlah_tiket_input = input("Masukkan jumlah tiket yang ingin dibeli (maksimal " + str(jumlah_kursi) + "): ")  # String, Bilangan
        jumlah_tiket = 0  # Bilangan
        if len(jumlah_tiket_input) > 0:  # Percabangan
            jumlah_tiket = 0  # Bilangan
            for char in jumlah_tiket_input:  # Perulangan
                if char < '0' or char > '9':  # Percabangan
                    jumlah_tiket = -1  # Bilangan
                    break  # Break
            if jumlah_tiket != -1:  # Percabangan
                jumlah_tiket = int(jumlah_tiket_input)  # Bilangan, Operator
                if 1 <= jumlah_tiket <= jumlah_kursi:  # Percabangan
                    valid_input = True  # Boolean
                else:
                    print("Jumlah tiket tidak valid, silakan coba lagi.")  # String
                    continue  # Continue
            else:
                print("Input tidak valid, silakan masukkan angka.")  # String
                continue  # Continue
        else:
            print("Input tidak valid, silakan coba lagi.")  # String
            continue  # Continue

    # Memilih nama
    nama_pembeli = input("Masukkan nama Anda: ")  # String

    # Memilih kursi
    kursi_list = ["Kursi " + str(i) for i in range(1, jumlah_kursi + 1)]  # List, Bilangan
    print("\nDaftar Kursi:")  # String
    print("+" + "=" * 72 + "+")  # String
    for i in range(len(kursi_list)):  # Perulangan
        print(f"| {kursi_list[i]:<69} |")  # String, Operator
    print("+" + "=" * 72 + "+")  # String

    kursi_terpilih = []  # List
    for i in range(jumlah_tiket):  # Perulangan
        valid_kursi = False  # Boolean
        while not valid_kursi:  # Perulangan, Percabangan
            kursi = input("Pilih kursi untuk tiket " + str(i + 1) + ": ")  # String, Bilangan
            if kursi in kursi_list and kursi not in kursi_terpilih:  # Percabangan
                valid_kursi = True  # Boolean
                kursi_terpilih.append(kursi)  # List
            else:
                print("Kursi tidak valid atau sudah dipilih, silakan coba lagi.")  # String
                continue  # Continue

    # Menghitung total harga sebelum dan setelah diskon
    diskon = 0  # Bilangan
    if jumlah_tiket > 3:  # Percabangan
        diskon = 0.1  # Bilangan, Operator

    total_sebelum_diskon = harga_per_tiket * jumlah_tiket  # Operator, Bilangan
    total_harga = total_sebelum_diskon  # Bilangan
    if diskon > 0:  # Percabangan
        total_harga -= total_harga * diskon  # Operator, Bilangan

    # Menampilkan header tabel
    print("=" * 72 + "+")  # String
    print(f"| Total harga sebelum diskon: Rp {total_sebelum_diskon:<38} |")  # String, Operator
    print(f"| Total harga setelah diskon: Rp {total_harga:<38} |")  # String, Operator
    print(f"| Total yang harus dibayar: Rp {total_harga:<40} |")  # String, Operator
    print("=" * 72 + "+")  # String

    # Memilih metode pembayaran
    metode_pembayaran = input("Masukkan metode pembayaran (1 untuk tunai💵, 2 untuk kartu kredit💳): ")  # String

    if metode_pembayaran == "1":  # Percabangan
        print("=" * 72 + "+")  # String
        print("| Metode Pembayaran: Tunai " + " " * (45) + "|")  # String, Operator
        print("=" * 72 + "+")  # String
        while True:  # Perulangan
            uang_tunai = float(input("Masukkan jumlah uang tunai: "))  # Input dari pengguna, Bilangan
            if uang_tunai < total_harga:  # Percabangan
                print("Uang tunai tidak mencukupi. Sisa pembayaran: " + str(total_harga - uang_tunai) + " rupiah")  # String, Bilangan
            else:
                kembalian = uang_tunai - total_harga  # Operator, Bilangan
                print("=" * 72 + "+")  # String
                print(f"| Jumlah Pembayaran: Rp {uang_tunai:<47} |")  # String, Operator
                print(f"| Kembalian: Rp {kembalian:<55} |")  # String, Operator
                print("=" * 72 + "+")  # String
                print("Transaksi selesai.")  # String
                if kembalian > 0:  # Percabangan
                    print("Berikut adalah kembalian yang diberikan:")  # String
                print(str(kembalian) + " rupiah")  # String, Bilangan
                break  # Break

    else:  # Percabangan
        print("=" * 72 + "+")  # String
        print("| Metode Pembayaran: Kartu Kredit " + " " * (38) + "|")  # String, Operator
        print("=" * 72 + "+")  # String
        pin_kartu_kredit = input("Masukkan pin kartu kredit: ")  # String
        while True:  # Perulangan
            harga_kartu_kredit = float(input("Masukkan jumlah yang dibayarkan menggunakan kartu kredit: "))  # Input dari pengguna, Bilangan
            if harga_kartu_kredit < total_harga:  # Percabangan
                print("Pembayaran menggunakan kartu kredit tidak mencukupi. Sisa pembayaran: " + str(total_harga - harga_kartu_kredit) + " rupiah")  # String, Bilangan
            else:
                kembalian = harga_kartu_kredit - total_harga  # Operator, Bilangan
                print("=" * 72 + "+")  # String
                print(f"| Jumlah Pembayaran: Rp {harga_kartu_kredit:<47} |")  # String, Operator
                print(f"| Kembalian: Rp {kembalian:<55} |")  # String, Operator
                print("=" * 72 + "+")  # String
                print("Transaksi selesai.")  # String
                if kembalian > 0:  # Percabangan
                    print("Berikut adalah kembalian yang diberikan:")  # String
                print(str(kembalian) + " rupiah")  # String, Bilangan
                break  # Break

    print("=" * 72 + "+")  # String

    # Struk tiket
    print("\n" + "+" + "=" * 72 + "+")  # String
    print("|                         🎟️ STRUK TIKET 🎟️                                |")  # String
    print("+" + "=" * 72 + "+")  # String, Operator
    print(f"| Nama Pembeli       : {nama_pembeli:<50}  \b\b|")  # String, Operator
    print(f"| Nama Bus           : {bus_terpilih:<50}  \b\b|")  # String, Operator
    print(f"| Kategori           : {kategori_terpilih:<50}|")  # String, Operator
    print(f"| Jumlah Tiket       : {jumlah_tiket:<50}  \b\b|")  # String, Operator

    kursi_str = ", ".join(kursi_terpilih)  # String, Operator, List
    print(f"| Kursi yang Dipilih : {kursi_str:<50} \b|")  # String, Operator
    print(f"| Harga per Tiket    : Rp {harga_per_tiket:<47} \b\b |")  # String, Operator
    if diskon > 0:  # Percabangan
        print(f"| Diskon             : {diskon * 100}% {'':<43} \b |")  # String, Operator
    print(f"| Jam Keberangkatan  : {jam_keberangkatan:<50}  \b\b\b |")  # String, Operator
    print(f"| Total Harga        : Rp {total_harga:<45}   \b\b |")  # String, Operator
    print(f"| Jarak Tempuh       : 750 km                           \t\t |")  # String, Bilangan
    print(f"| Perkiraan Waktu    : 15 jam                           \t\t |")  # String, Bilangan
    print("+" + "=" * 72 + "+")  # String, Operator
    print("|   Terima kasih telah membeli tiket di PO Juragan 99!🎉                 |")  # String
    print("+" + "=" * 72 + "+")  # String, Operator

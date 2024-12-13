import sys

# Daftar kendaraan dan kategori
kendaraan_list = [
    ("Elf 12 Seat", "Elf", 600000, 12, "08:00"),
    ("Elf 16 Seat", "Elf", 800000, 16, "09:00"),
    ("Bus Medium 30 Seat", "Medium Bus", 1200000, 30, "10:00"),
    ("Bus Besar 50 Seat", "Big Bus", 2000000, 50, "11:00"),
]

def tampilkan_informasi():
    print("+" + "=" * 95 + "+")
    print("|                   <----- Selamat datang di PO Sewa Mobil ----->     \t\t|")
    print("|  Rute: Jakarta ke Bandung                                                      \t\t|")
    print("|  Jarak: 150 km                                                                \t\t|")
    print("|  Waktu Perjalanan: 3 jam                                                       \t\t|")
    print("+" + "=" * 95 + "+")
    print("| Daftar Kendaraan:                                                             \t|")
    print("+" + "=" * 95 + "+")
    print("| No  | Nama Kendaraan 🚗   | Kategori 📃    | Harga 🎫    | Kursi 💺 \t| Jam Keberangkatan ⏰\t|")
    print("+" + "=" * 95 + "+")

    # Menampilkan daftar kendaraan dalam format tabel
    for index, kendaraan in enumerate(kendaraan_list, start=1):
        nama_kendaraan, kategori, harga, kursi, jam_keberangkatan = kendaraan
        print("|", f"{index:<3}|", f"{nama_kendaraan:<15}|", f"{kategori:<15}| Rp", f"{harga:<9}\t|", f"{kursi:<9}\t|", f"{jam_keberangkatan:<20}\t|")
    
    print("+" + "=" * 95 + "+")

def pilih_kendaraan():
    while True:
        try:
            pilihan_kendaraan_input = input("\nPilih kendaraan (1-4) atau ketik 0 untuk keluar: ")
            pilihan_kendaraan = int(pilihan_kendaraan_input)
            if 0 <= pilihan_kendaraan <= len(kendaraan_list):
                return pilihan_kendaraan
            else:
                print("Pilihan tidak valid, silakan coba lagi.")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")

def pilih_jumlah_tiket(jumlah_kursi):
    while True:
        try:
            jumlah_tiket_input = input("Masukkan jumlah tiket yang ingin dibeli (maksimal " + str(jumlah_kursi) + "): ")
            jumlah_tiket = int(jumlah_tiket_input)
            if 1 <= jumlah_tiket <= jumlah_kursi:
                return jumlah_tiket
            else:
                print("Jumlah tiket tidak valid, silakan coba lagi.")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")

def pilih_kursi(jumlah_kursi, jumlah_tiket):
    kursi_list = ["Kursi " + str(i) for i in range(1, jumlah_kursi + 1)]
    print("\nDaftar Kursi:")
    print("+" + "=" * 72 + "+")
    for kursi in kursi_list:
        print(f"| {kursi:<69} |")
    print("+" + "=" * 72 + "+")

    kursi_terpilih = []
    for i in range(jumlah_tiket):
        while True:
            kursi = input("Pilih kursi untuk tiket " + str(i + 1) + ": ")
            if kursi in kursi_list and kursi not in kursi_terpilih:
                kursi_terpilih.append(kursi)
                break
            else:
                print("Kursi tidak valid atau sudah dipilih, silakan coba lagi.")
    return kursi_terpilih

def hitung_total_harga(harga_per_tiket, jumlah_tiket):
    diskon = 0
    if jumlah_tiket > 3:
        diskon = 0.1

    total_sebelum_diskon = harga_per_tiket * jumlah_tiket
    total_harga = total_sebelum_diskon * (1 - diskon)
    return total_sebelum_diskon, total_harga, diskon

def metode_pembayaran(total_harga):
    while True:
        metode = input ("Masukkan metode pembayaran (1 untuk tunai💵, 2 untuk kartu kredit💳): ")
        if metode == "1":
            while True:
                try:
                    uang_tunai = float(input("Masukkan jumlah uang tunai: "))
                    if uang_tunai < total_harga:
                        print("Uang tunai tidak mencukupi. Sisa pembayaran: " + str(total_harga - uang_tunai) + " rupiah")
                    else:
                        kembalian = uang_tunai - total_harga
                        print("=" * 72 + "+")
                        print(f"| Jumlah Pembayaran: Rp {uang_tunai:<47} |")
                        print(f"| Kembalian: Rp {kembalian:<55} |")
                        print("=" * 72 + "+")
                        print("Transaksi selesai.")
                        if kembalian > 0:
                            print("Berikut adalah kembalian yang diberikan:")
                        print(str(kembalian) + " rupiah")
                        return
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka.")
        elif metode == "2":
            pin_kartu_kredit = input("Masukkan pin kartu kredit: ")
            while True:
                try:
                    harga_kartu_kredit = float(input("Masukkan jumlah yang dibayarkan menggunakan kartu kredit: "))
                    if harga_kartu_kredit < total_harga:
                        print("Pembayaran menggunakan kartu kredit tidak mencukupi. Sisa pembayaran: " + str(total_harga - harga_kartu_kredit) + " rupiah")
                    else:
                        kembalian = harga_kartu_kredit - total_harga
                        print("=" * 72 + "+")
                        print(f"| Jumlah Pembayaran: Rp {harga_kartu_kredit:<47} |")
                        print(f"| Kembalian: Rp {kembalian:<55} |")
                        print("=" * 72 + "+")
                        print("Transaksi selesai.")
                        if kembalian > 0:
                            print("Berikut adalah kembalian yang diberikan:")
                        print(str(kembalian) + " rupiah")
                        return
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka.")

def struk_tiket(nama_pembeli, kendaraan_terpilih, kategori_terpilih, jumlah_tiket, kursi_terpilih, harga_per_tiket, total_harga, jam_keberangkatan, diskon):
    print("\n" + "+" + "=" * 72 + "+")
    print("|                         🎟️ STRUK TIKET 🎟️                                |")
    print("+" + "=" * 72 + "+")
    print(f"| Nama Pembeli       : {nama_pembeli:<50}  \b\b|")
    print(f"| Nama Kendaraan     : {kendaraan_terpilih:<50}  \b\b|")
    print(f"| Kategori           : {kategori_terpilih:<50}|")
    print(f"| Jumlah Tiket       : {jumlah_tiket:<50}  \b\b|")
    kursi_str = ", ".join(kursi_terpilih)
    print(f"| Kursi yang Dipilih : {kursi_str:<50} \b|")
    print(f"| Harga per Tiket    : Rp {harga_per_tiket:<47} \b\b |")
    if diskon > 0:
        print(f"| Diskon             : {diskon * 100}% {'':<43} \b |")
    print(f"| Jam Keberangkatan  : {jam_keberangkatan:<50}  \b\b\b |")
    print(f"| Total Harga        : Rp {total_harga:<45}   \b\b |")
    print(f"| Jarak Tempuh       : 150 km                           \t\t |")
    print(f"| Perkiraan Waktu    : 3 jam                            \t\t |")
    print("+" + "=" * 72 + "+")
    print("|   Terima kasih telah menyewa kendaraan di PO Sewa Mobil!🎉                 |")
    print("+" + "=" * 72 + "+")

def main():
    tampilkan_informasi()
    pilihan_kendaraan = pilih_kendaraan()
    if pilihan_kendaraan == 0:
        print("Terima kasih telah menggunakan layanan kami!")
        sys.exit()

    kendaraan_terpilih, kategori_terpilih, harga_per_tiket, jumlah_kursi, jam_keberangkatan = kendaraan_list[pilihan_kendaraan - 1]
    jumlah_tiket = pilih_jumlah_tiket(jumlah_kursi)
    nama_pembeli = input("Masukkan nama Anda: ")
    kursi_terpilih = pilih_kursi(jumlah_kursi, jumlah_tiket)

    total_sebelum_diskon, total_harga, diskon = hitung_total_harga(harga_per_tiket, jumlah_tiket)

    print("=" * 72 + "+")
    print(f"| Total harga sebelum diskon: Rp {total_sebelum_diskon:<38} |")
    print(f"| Total harga setelah diskon: Rp {total_harga:<38} |")
    print(f"| Total yang harus dibayar: Rp {total_harga:<40} |")
    print("=" * 72 + "+")

    metode_pembayaran(total_harga)

    struk_tiket(nama_pembeli, kendaraan_terpilih, kategori_terpilih, jumlah_tiket, kursi_terpilih, harga_per_tiket, total_harga, jam_keberangkatan, diskon)

if __name__ == "__main__":
    main()
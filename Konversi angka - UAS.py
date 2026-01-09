def terbilang(n):

    angka = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", 
             "Delapan", "Sembilan", "Sepuluh", "Sebelas"]
    

    if n < 0:
        return "Minus " + terbilang(-n)
    

    elif n == 0:
        return "Nol"
    

    elif n < 12:
        return angka[n]
    

    elif n < 20:
        if n == 12:
            return "Dua Belas"
        elif n == 13:
            return "Tiga Belas"
        else:
            return terbilang(n - 10) + " Belas"
    

    elif n < 100:
        puluhan = n // 10
        satuan = n % 10
        

        if puluhan == 1:
            return "Sepuluh" + (" " + terbilang(satuan) if satuan > 0 else "")
        else:
            puluhan_teks = terbilang(puluhan) + " Puluh"
            if satuan > 0:
                return puluhan_teks + " " + terbilang(satuan)
            else:
                return puluhan_teks
    

    elif n < 200:
        sisa = n % 100
        if sisa > 0:
            return "Seratus " + terbilang(sisa)
        else:
            return "Seratus"
    

    elif n < 1000:
        ratusan = n // 100
        sisa = n % 100
        
        if ratusan == 1:
            ratusan_teks = "Seratus"
        else:
            ratusan_teks = terbilang(ratusan) + " Ratus"
        
        if sisa > 0:
            return ratusan_teks + " " + terbilang(sisa)
        else:
            return ratusan_teks
    

    elif n < 2000:
        sisa = n - 1000
        if sisa > 0:
            return "Seribu " + terbilang(sisa)
        else:
            return "Seribu"
    

    elif n < 1000000:
        ribuan = n // 1000
        sisa = n % 1000
        
        ribuan_teks = terbilang(ribuan) + " Ribu"
        
        if sisa > 0:
            return ribuan_teks + " " + terbilang(sisa)
        else:
            return ribuan_teks
    

    elif n < 1000000000:
        jutaan = n // 1000000
        sisa = n % 1000000
        
        jutaan_teks = terbilang(jutaan) + " Juta"
        
        if sisa > 0:
            return jutaan_teks + " " + terbilang(sisa)
        else:
            return jutaan_teks
    

    else:
        milyaran = n // 1000000000
        sisa = n % 1000000000
        
        milyaran_teks = terbilang(milyaran) + " Milyar"
        
        if sisa > 0:
            return milyaran_teks + " " + terbilang(sisa)
        else:
            return milyaran_teks

def jalankan_terbilang():
    print("=== PROGRAM FUNGSI TERBILANG ===")
    print("Mengubah bilangan menjadi teks (Bahasa Indonesia)")
    print("Contoh: 123 -> 'Seratus Dua Puluh Tiga'")
    print()
    
    try:
        try:
            bilangan_str = raw_input("Masukkan bilangan (0 hingga milyar): ").strip()
        except NameError:
            bilangan_str = input("Masukkan bilangan (0 hingga milyar): ").strip()
        

        bilangan_str = bilangan_str.replace('.', '').replace(',', '')
        
        bilangan = int(bilangan_str)
        
        if bilangan < 0:
            print("ERROR: Hanya mendukung bilangan positif.")
            return
            
        if bilangan > 1000000000:
            print("ERROR: Bilangan terlalu besar (maksimal 1.000.000.000).")
            return
            
        hasil = terbilang(bilangan)
        

        bil_str = str(bilangan)
        if len(bil_str) > 3:
            parts = []
            while bil_str:
                parts.append(bil_str[-3:])
                bil_str = bil_str[:-3]
            bil_formatted = ".".join(reversed(parts))
        else:
            bil_formatted = bil_str
        
        print("\n" + "="*50)
        print("Bilangan  : " + bil_formatted)
        print("Terbilang : " + hasil)
        print("="*50)
        
    except ValueError:
        print("ERROR: Input tidak valid! Harap masukkan bilangan bulat.")
    except Exception as e:
        print("ERROR: Terjadi kesalahan - %s" % str(e))

def main():
    while True:
        jalankan_terbilang()
        print()
        
        while True:  
            try:
                try:
                    ulangi = raw_input("\nCoba bilangan lain? (y/n): ").lower().strip()
                except NameError:
                    ulangi = input("\nCoba bilangan lain? (y/n): ").lower().strip()
                
                if ulangi == 'y' or ulangi == 'ya' or ulangi == 'yes':
                    print("\n" + "="*50)
                    break  
                elif ulangi == 'n' or ulangi == 't' or ulangi == 'tidak' or ulangi == 'no':
                    print("\nTerima kasih telah menggunakan program!")
                    return  
                else:
                    print("Input tidak valid! Ketik 'y' untuk Ya atau 'n' untuk Tidak.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram dihentikan.")
                return

if __name__ == "__main__":
    main()
# File : T01B_2272008.py
# Penulis : Elmosius Suli
# Tujuan : Program akan menerima N buah bilangan lalu menampilkan
# bilangan pertama, terakhir, dan di tengah. Jika N genap,
# akan menampilkan kedua bilangan di tengah.

## Program Utama ##
# Kamus lokal
# n : var. input jumlah isi array (int)
# arr_bil : var. array (Array)
# i : var. parameter for (int)
# tngh : var. nilai tengah (int)

def main():
    # Input
    n = int(input("N: "))
    
    # Inisialisasi
    arr_bil = [None] * n
        
    for i in range(n):
        arr_bil[i] = int(input
    (f"Masukkan bilangan ke- {i + 1} : "))

    # Proses
    if (n % 2 == 0):
        tngh = (n // 2 - 1)
    else:
        tngh = (n // 2)

    # Hasil
    print("Pertama:", arr_bil[0])
    print("Terakhir:", arr_bil[-1])

    if (n % 2 == 0):
        print("Tengah:", arr_bil[tngh], arr_bil[tngh+1])
    else:
        print("Tengah:", arr_bil[tngh])
   
        
if __name__ == "__main__":
    main()
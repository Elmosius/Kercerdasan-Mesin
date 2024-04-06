# File : T01A_2272008.py
# Penulis : Elmosius Suli
# Tujuan : Program akan menerima masukan N bilangan bulat lalu
# akan menampilkan N bilangan secara terbaik, jumlah total, dan 
# rata-ratanya.

## Program Utama ##
# Kamus lokal
# n : var. input jumlah isi array (int)
# arr_bil : var. array (Array)
# jmlh_tot : var. jumlah total dari isi array (int)
# rata-rata : var. rata-rata dari isi array (float)
# i : var. parameter (int)

# Notes :
# Menggunakan method python menambahkan array dgn sum()
def main():
    
    # Input
    n = int(input(
    "Masukkan jumlah bilangan: "))
    
    # Inisialisasi
    arr_bil = [None] * n
        
    for i in range(n):
        arr_bil[i] = int(input
    (f"Masukkan bilangan ke- {i + 1} : "))

    # Proses
    jmlh_tot = sum(arr_bil)
    rata_rata = sum(arr_bil) / n
    
    # Tampilan
    print("Bilangan secara terbalik:", end=" ")
    for i in range(n - 1, -1, -1):
        print(arr_bil[i], end=" ")

    print()
    print("Total: ", jmlh_tot)
    print(f"Rata-rata: {rata_rata:.2f}")
    
if __name__ == "__main__":
    main()
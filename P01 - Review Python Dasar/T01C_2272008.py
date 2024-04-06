# File : T01C_2272008.py
# Penulis : Elmosius Suli
# Tujuan : Program aplikasi Xmart dimana akan digunakan 
# untuk mendata barang. Lalu Bisa menampilkan barang 
# dengan disorting berdasarkan harga/ stok.

## Program Utama ##
# Kamus lokal
# n : var. ukuran array matriks (int)
# arr_brg : var. array matriks (Array)
# i : var. parameter(int)
# kode_brg : var. input kode barang(str)
# sort_brg : var. input sorting berdasarlah pilihan(str)

# Notes :
# Memakai method python yang sudah ada pada sorting
# dimana Penggunaan functional programming pada matkul PBO

def main():
    # Inisialisasi
    n = 4
    arr_brg = [None] * n
    for i in range(n):
        arr_brg[i] = n*[None]
    
    # Input
    print("Silahkan Data Barang")
    for i in range(0,n,1):
        kode_brg = str(
            input("Kode Barang: "))
        for k in range(i):
            while(kode_brg == arr_brg[k][0]):
                print("Kode Barang tidak bole ada yang \
sama, silahkan masukan kembali.")
                kode_brg = str(input("Kode Barang: "))
        arr_brg[i][0] = kode_brg
        arr_brg[i][1] = str(
            input("Nama Barang: "))
        arr_brg[i][2] = int(
            input("Stok: "))
        arr_brg[i][3] = int(
            input("Harga: "))
        print("===============================")
        
    # Tampil
    print("List Barang yang dimiliki:")
    for i in range(n):
        print(f'{arr_brg[i][0]} - \
{arr_brg[i][1]} - {arr_brg[i][2]} - Rp {arr_brg[i][3]}')
    print("===============================")
    
    # Proses sort
    # Penggunaan functional programming pada matkul PBO
    sort_brg = str(input('Sort Berdasarkan (Harga/Stok) :'))
    if (sort_brg.lower() == "harga"):
        arr_brg = sorted(arr_brg, key=lambda x: x[3])
    elif (sort_brg.lower() == "stok"):
        arr_brg = sorted(arr_brg, key=lambda x: x[2])
    else:
        print("Pilihan hanya berdasarkan (Harga/Stok)")
        
    # Hasil
    print(f"List barang yang telah disortir \
berdasarkan {sort_brg.lower()}")
    
    for i in range(n):
        print(f'{arr_brg[i][0]} - \
{arr_brg[i][1]} - {arr_brg[i][2]} - Rp {arr_brg[i][3]}')
    print("==============================")
        
            
            
            
        
        
        
        
        
if __name__ == "__main__":
    main()
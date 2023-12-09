# Solusinya pakai Algoritma Kadane
def MaxSumSubarray(arr):
    #inisiasi dulu curr_sum dan max_sum dgn elemen pertama array
    curr_sum = arr[0]
    max_sum = arr[0]

    for i in arr[1:]:
        # Update curr_sum buat cari jumlah max subarray berurutan
        curr_sum = max(i, curr_sum + i)
        # Update max_sum jika curr_sum lebih besar
        max_sum = max(max_sum, curr_sum)

    return max_sum

if __name__ == "__main__":
    # Input dari user (sesuai batasan)
    while True:
        N = int(input("Masukkan nilai N (1 <= N <= 100): "))
        if 1 <= N <= 100:
            break
        else:
            print("Nilai N tidak sesuai batasan. Coba lagi.")

    array = list(map(int, input(f"Masukkan {N} elemen array, dipisahkan oleh spasi: ").split()))

    # Cek panjang array sesuai dengan N
    if len(array) != N:
        print(f"Panjang array tidak sesuai dengan N. Harap masukkan {N} elemen.")
    else:
        result = MaxSumSubarray(array)
        print(f"Output: Maximum Sum: {result}")

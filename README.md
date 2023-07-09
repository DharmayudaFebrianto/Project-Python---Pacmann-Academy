# sistem-kasir-self-service

## Deskripsi
Repository ini berisi implementasi program Python untuk sistem kasir self-service di supermarket. Program ini memungkinkan pelanggan untuk membuat transaksi pembelian secara mandiri dan menyediakan fitur-fitur seperti menambah, mengubah, menghapus, dan memeriksa item dalam transaksi. Selain itu, program juga menghitung total harga transaksi dengan mempertimbangkan diskon yang berlaku.

## Fitur-fitur:

  - Membuat transaksi baru dengan mengatur ID transaksi.
  - Menambahkan item pembelian dengan memasukkan nama item, jumlah item, dan harga per item.
  - Mengubah nama item, jumlah item, atau harga item dalam transaksi.
  - Menghapus item dari transaksi.
  - Menghapus semua item dan mereset transaksi.
  - Memeriksa pesanan untuk mendeteksi kesalahan input data.
  - Menghitung total harga transaksi dengan mempertimbangkan diskon berdasarkan aturan yang ditentukan.
  - Menampilkan daftar transaksi beserta total harga setelah diskon.

## Intruksi Penggunaan: 
1. Clone repository ini ke lokal Anda.
2. Jalankan file kasir_self_service.py untuk menjalankan program.
3. kuti instruksi yang ada pada program untuk melakukan transaksi dan menggunakan fitur-fitur yang disediakan.
4. Sesuaikan program jika diperlukan atau tambahkan fitur tambahan sesuai kebutuhan.

Repository ini berguna bagi para pemilik supermarket atau pengembang yang tertarik untuk mengimplementasikan sistem kasir self-service di toko mereka. Dengan menggunakan repository ini, mereka dapat dengan mudah mengintegrasikan fitur-fitur yang diperlukan dan menyesuaikan program sesuai dengan kebutuhan spesifik mereka.

Catatan: Repository ini hanya berisi implementasi program Python untuk sistem kasir self-service. Tidak termasuk antarmuka pengguna (UI) yang lengkap atau fitur-fitur lainnya yang mungkin diperlukan dalam implementasi nyata.


## Alur Program
1. Program dimulai dengan membuat objek transaksi baru menggunakan class Transaction.

2. Pengguna memasukkan item yang ingin dibeli ke dalam transaksi dengan menggunakan metode add_item pada objek transaksi. Item tersebut berisi nama item, jumlah item, dan harga per item. 
3. Pengguna memiliki opsi untuk melakukan pembaruan pada transaksi, yaitu:

  - Mengubah nama item dengan menggunakan metode update_item_name.
  - Mengubah jumlah item dengan menggunakan metode update_item_qty.
  - Mengubah harga item dengan menggunakan metode update_item_price.

4. Jika pengguna ingin menghapus salah satu item dari transaksi, pengguna dapat menggunakan metode delete_item.
5. Jika pengguna ingin menghapus semua item atau mereset transaksi, pengguna dapat menggunakan metode reset_transaction.

6. Pengguna dapat melakukan pengecekan pesanan dengan menggunakan metode check_order. Metode ini akan memeriksa apakah ada kesalahan input data dalam transaksi. Jika tidak ada kesalahan, program akan mengeluarkan pesan "Pemesanan sudah benar" dan menampilkan daftar transaksi. Jika terdapat kesalahan, program akan mengeluarkan pesan "Terjadi kesalahan input data".

7. Program akan menghitung total harga transaksi dengan menggunakan metode total_price. Jika total belanja memenuhi syarat diskon, program akan mengurangi total harga sesuai dengan diskon yang berlaku.

8. Program akan mencetak daftar transaksi beserta total harga setelah diskon.

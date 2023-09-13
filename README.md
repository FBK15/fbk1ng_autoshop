PERTANYAAN
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

JAWABAN
1. a. Membuat proyek django baru --> untuk membuat sebuah proyek django baru, saya mengaktifkan virtual environment dahulu. Kemudian saya       membuat file baru seperti requirements.txt yang dibutuhkan untuk bisa memulai sebuah proyek django baru dan menginstallnya terlebih dahulu. Setelah itu, saya membuat projek baru dengan nama gudang_mobil. 

   b. Membuat aplikasi dengan nama 'main' pada proyek gudang_mobil --> saya menggunakan command "python manage.py startapp (nama aplikasi)" pada direktori terluar saya yaitu fbk1ng_autshop untuk membuat aplikasi dengan nama 'main'. Kemudian saya memasukkan aplikasi 'main' ke dalam proyek gudang_mobil dengan cara menuliskan 'main' pada variabel "INSTALLED_APP" dalam file settings.py di direktori proyek gudang_mobil.

   c. Routing proyek agar dapat menjalankan aplikasi main --> Di dalam file 'urls.py' pada direktori proyek gudang_mobil, saya menambahkan sebuah path yang meng-include atau menyambungkan seperti "sebuah jalan" antara proyek gudang_mobil dengan aplikasi 'main' sehingga dari proyek gundang_mobil, aplikasi 'main' bisa diakses.

   d.  Membuat sebuah fungsi dalam views.py yang berisikan data diri dan nama toko --> saya membuat fungsi dengan nama 'developer' yang berisikan sebuah list bernama 'self_identity' yang berisikan variabel 'developer_name' dan 'Class'. 

   e. Routing urls.py pada direktori aplikasi 'main' untuk memetakan fungsi dalam views.py --> agar semua fungsi di views.py yang telah saya buat dapat diakses, saya mengimpor terlebih dahulu fungsi 'stocks' dan 'developer' dari views.py ke dalam urls.py. Kemudian saya membuat dua buah path yaitu '' dan 'developer' dimana dalam path '' menggunakan variabel yang terdapat dalam fungsi 'stocks' sedangkan path 'developer' menggunakan variabel yang terdapat dalam fungsi 'developer'. Variabel-variabel yang ada dalam kedua fungsi tersebut kemudian menggantikan variabel yang ada dalam html masing-masing.

   f. Deployment Adaptable --> Saya nge push terlebih dahulu semua perubahan yang saya lakukan terhadap direktori fbk1ng_autoshop ke dalam repo yang ada di github. Kemudian saya membuat app pada Adaptable dengan menggunakan repositori 'fbk1ng_autoshop' yang menjadi basis app Adaptablenya. Saya menyetting app Adaptable denga menggunakan Python App Template dan PostgreSQL. Versi python yang saya gunakan adalah 3.10 dengan start command "python manage.py migrate && gunicorn gudang_mobil.wsgi" dimana 'gudang_mobil' merupakan direktori proyek saya yang terdapat dalam direktori repositori 'fbk1ng_autoshop'. Untuk finishing, saya men-deploy appnya.

2. 

3. Virtual Environment digunakan agar memungkinkan kita membuat proyek-proyek dan memiliki versi yang berbeda dari proyek tersebut tanpa bertabrakan versi satu dengan yang lainnya. Hal tersebut dapat memudahkan kita saat ingin memperbaiki, manambahkan, dan menguji coba sesuatu dalam proyeknya. Walaupun begitu, tetap memungkinkan untuk membuat sebuah aplikasi django tanpa menggunakan virtual environment.

4. MVC --> MVC View, Controller. 
   MVT --> Model, View, Template. 
   MVVM --> Model, View, ViewModel. 

   Model : Tugas model dalam semua pola bisa dibilang mirip antara satu sama lain. Model memiliki tugas untuk mendapatkan data-data dari sebuah database yang kemudian digunakan untuk menjalankan sebuah aplikasi atau perangkat lunak

   View : View dalam pola MVC bertugas 
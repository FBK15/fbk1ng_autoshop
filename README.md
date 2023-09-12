PERTANYAAN
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

JAWABAN
1. a. Membuat proyek django baru: untuk membuat sebuah proyek django baru, saya mengaktifkan virtual environment dahulu. Kemudian saya membuat file baru seperti requirements.txt yang dibutuhkan untuk bisa memulai sebuah proyek django baru dan menginstallnya terlebih dahulu. Setelah itu, saya membuat projek baru dengan nama gudang_mobil. 
   b. Membuat aplikasi dengan nama 'main' pada proyek gudang_mobil = saya menggunakan command "python manage.py startapp (nama aplikasi)" pada direktori terluar saya yaitu fbk1ng_autshop untuk membuat aplikasi dengan nama 'main'. Kemudian saya memasukkan aplikasi 'main' ke dalam proyek gudang_mobil dengan cara menuliskan 'main' pada variabel "INSTALLED_APP" dalam file settings.py di direktori proyek gudang_mobil.

2. 

3. Virtual Environment digunakan agar memungkinkan kita membuat proyek-proyek dan memiliki versi yang berbeda dari proyek tersebut tanpa bertabrakan versi satu dengan yang lainnya. Hal tersebut dapat memudahkan kita saat ingin memperbaiki, manambahkan, dan menguji coba sesuatu dalam proyeknya. Walaupun begitu, tetap memungkinkan untuk membuat sebuah aplikasi django tanpa menggunakan virtual environment.

4. MVC --> MVC terbagi menjadi tiga komponen, yaitu Model-View-Controller. Model bertugas 
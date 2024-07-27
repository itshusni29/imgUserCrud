C:\dev\python\portalnewstructure\portalHrd\
│
├── portalHrd/                # Folder pengaturan proyek utama Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/                     # Folder untuk semua aplikasi Django
│   ├── main/                 # Aplikasi untuk halaman utama
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── main/
│   │           ├── beranda.html
│   │           ├── team_kami.html
│   │           ├── prosedur.html
│   │           ├── aturan.html
│   │           └── kontak.html
│   │
│   ├── information/          # Aplikasi untuk halaman informasi
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── information/
│   │           ├── pengumuman.html
│   │           ├── informasi_kehadiran.html
│   │           ├── jadwal_training.html
│   │           ├── jadwal_bus.html
│   │           └── menu_kantin.html
│   │
│   ├── user/                 # Aplikasi untuk mengelola pengguna
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── user/
│   │           └── user_profile.html
│   │
│   ├── forms/                # Aplikasi untuk mengelola form permintaan
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permintaan_training/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── forms.py
│   │   ├── dinas_luar/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── forms.py
│   │   ├── sumbangan/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── forms.py
│
├── manage.py                 # File untuk perintah manajemen Django
│
├── static/                   # Folder untuk file statis seperti CSS, JS, gambar
│   ├── css/
│   │   └── style.css         # Contoh file CSS
│   ├── images/
│   │   └── logo.png          # Contoh file gambar
│   └── js/
│       └── script.js         # Contoh file JS
│
├── media/                    # Folder untuk file yang diunggah pengguna
│
└── templates/                # Folder untuk template HTML yang digunakan di seluruh aplikasi
    ├── base/                 # Folder untuk template dasar
    │   └── base.html         # Template dasar untuk seluruh aplikasi
    ├── main/                 # Folder untuk template aplikasi utama
    ├── forms/                # Folder untuk template aplikasi form
    ├── information/          # Folder untuk template aplikasi informasi
    └── user/                 # Folder untuk template aplikasi user

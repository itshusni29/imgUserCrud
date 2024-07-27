portalHrd/
│
├── portalHrd/  # Folder ini berisi pengaturan proyek dan file utama Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/  # Folder ini berisi aplikasi-aplikasi Django dalam proyek ini
│   ├── main/  # Aplikasi untuk halaman utama (beranda, tim kami, prosedur, aturan, kontak)
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
│   ├── forms/  # Aplikasi untuk mengelola berbagai form permintaan
│   │   ├── permintaan_training/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── forms.py
│   │   │   ├── urls.py
│   │   │   ├── templates/
│   │   │   │   └── permintaan_training/
│   │   │   │       ├── permintaan_training_form.html
│   │   │   │       └── permintaan_training_approval.html
│   │   │
│   │   ├── dinas_luar/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── forms.py
│   │   │   ├── urls.py
│   │   │   ├── templates/
│   │   │   │   └── dinas_luar/
│   │   │   │       ├── dinas_luar_form.html
│   │   │   │       └── dinas_luar_approval.html
│   │   │
│   │   ├── sumbangan/
│   │   │   ├── __init__.py
│   │   │   ├── views.py
│   │   │   ├── models.py
│   │   │   ├── forms.py
│   │   │   ├── urls.py
│   │   │   ├── templates/
│   │   │   │   └── sumbangan/
│   │   │   │       ├── sumbangan_form.html
│   │   │   │       └── sumbangan_approval.html
│   │
│   ├── information/  # Aplikasi untuk halaman informasi
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
│
├── manage.py  # File ini digunakan untuk berbagai perintah manajemen proyek Django
│
├── static/  # Folder ini berisi file-file statis seperti CSS, JS, gambar
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/  # Folder ini untuk file yang diunggah pengguna, seperti foto atau dokumen

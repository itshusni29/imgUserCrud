project_name/
│
├── project_name/
│   ├── __init__.py               # File inisialisasi untuk direktori proyek utama
│   ├── settings.py               # Pengaturan utama untuk proyek Django
│   ├── urls.py                   # File routing utama untuk proyek
│   ├── asgi.py                   # ASGI konfigurasi untuk penerapan asynchronous
│   ├── wsgi.py                   # WSGI konfigurasi untuk penerapan synchronous
│   ├── templates/                # Template global untuk seluruh aplikasi
│   │   ├── base.html             # Template dasar yang akan diwarisi oleh template lain
│   ├── static/                   # File statis global seperti CSS, JS, dan gambar
│       ├── css/                  # Folder untuk menyimpan file CSS
│       ├── js/                   # Folder untuk menyimpan file JavaScript
│       └── images/               # Folder untuk menyimpan gambar
│
├── apps/                         # Direktori untuk aplikasi Django individual
│   ├── core/                     # Aplikasi inti yang mencakup banyak fitur dasar
│   │   ├── __init__.py           # File inisialisasi untuk aplikasi core
│   │   ├── admin.py              # Konfigurasi admin untuk aplikasi core
│   │   ├── apps.py               # Konfigurasi aplikasi
│   │   ├── models.py             # Definisi model untuk aplikasi core
│   │   ├── tests.py              # Pengujian untuk aplikasi core
│   │   ├── urls.py               # File routing untuk aplikasi core
│   │   ├── views.py              # Logika tampilan untuk aplikasi core
│   │   ├── templates/            # Template spesifik untuk aplikasi core
│   │   │   └── core/
│   │   │       ├── home.html             # Template untuk halaman home
│   │   │       ├── team.html             # Template untuk halaman tim kami
│   │   │       ├── contact.html          # Template untuk halaman kontak
│   │   │       ├── rules.html            # Template untuk halaman aturan
│   │   │       ├── bus_schedule.html     # Template untuk halaman jadwal bus
│   │   │       ├── attendance_index.html # Template untuk halaman indeks kehadiran
│   │   │       ├── menu.html             # Template untuk halaman menu makan
│   │   │       ├── activities.html       # Template untuk halaman kegiatan
│   │   │       ├── training_request_form.html  # Template untuk formulir permintaan training
│   │   │       ├── leave_request_form.html     # Template untuk formulir permintaan cuti
│   │   │       ├── other_forms.html      # Template untuk formulir lainnya
│   │   └── static/                # File statis spesifik untuk aplikasi core
│   │       └── core/
│   │           ├── css/           # File CSS spesifik untuk aplikasi core
│   │           ├── js/            # File JavaScript spesifik untuk aplikasi core
│   │           └── images/        # Gambar spesifik untuk aplikasi core
│   │
│   ├── forms/                     # Aplikasi khusus untuk mengelola berbagai jenis formulir
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── forms/
│   │   │       ├── training_request_form.html
│   │   │       ├── leave_request_form.html
│   │   │       ├── other_forms.html
│   │   └── static/
│   │       └── forms/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── team/                      # Aplikasi untuk mengelola tim
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── team/
│   │   │       ├── index.html     # Template untuk daftar anggota tim
│   │   │       ├── detail.html    # Template untuk detail anggota tim
│   │   └── static/
│   │       └── team/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── contact/                   # Aplikasi untuk mengelola kontak
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── contact/
│   │   │       ├── index.html     # Template untuk halaman kontak
│   │   └── static/
│   │       └── contact/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── rules/                     # Aplikasi untuk mengelola aturan
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── rules/
│   │   │       ├── index.html     # Template untuk daftar aturan
│   │   │       ├── detail.html    # Template untuk detail aturan
│   │   └── static/
│   │       └── rules/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── bus_schedule/              # Aplikasi untuk mengelola jadwal bus
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── bus_schedule/
│   │   │       ├── index.html     # Template untuk daftar jadwal bus
│   │   │       ├── detail.html    # Template untuk detail jadwal bus
│   │   └── static/
│   │       └── bus_schedule/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── attendance/                # Aplikasi untuk mengelola kehadiran
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── attendance/
│   │   │       ├── index.html     # Template untuk daftar kehadiran
│   │   │       ├── detail.html    # Template untuk detail kehadiran
│   │   └── static/
│   │       └── attendance/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── menu/                      # Aplikasi untuk mengelola menu makan
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── menu/
│   │   │       ├── index.html     # Template untuk daftar menu makan
│   │   │       ├── detail.html    # Template untuk detail menu makan
│   │   └── static/
│   │       └── menu/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── activities/                # Aplikasi untuk mengelola kegiatan
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── activities/
│   │   │       ├── index.html     # Template untuk daftar kegiatan
│   │   │       ├── detail.html    # Template untuk detail kegiatan
│   │   └── static/
│   │       └── activities/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── training_request/          # Aplikasi untuk mengelola permintaan training
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── training_request/
│   │   │       ├── index.html     # Template untuk daftar permintaan training
│   │   │       ├── detail.html    # Template untuk detail permintaan training
│   │   └── static/
│   │       └── training_request/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── leave_request/             # Aplikasi untuk mengelola permintaan cuti
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   │   └── leave_request/
│   │   │       ├── index.html     # Template untuk daftar permintaan cuti
│   │   │       ├── detail.html    # Template untuk detail permintaan cuti
│   │   └── static/
│   │       └── leave_request/
│   │           ├── css/
│   │           ├── js/
│   │           └── images/
│   │
│   ├── other_forms/               # Aplikasi untuk mengelola formulir lainnya
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       ├── templates/
│       │   └── other_forms/
│       │       ├── index.html     # Template untuk daftar formulir lainnya
│       │       ├── detail.html    # Template untuk detail formulir lainnya
│       └── static/
│           └── other_forms/
│               ├── css/
│               ├── js/
│               └── images/
│
├── manage.py                     # File manajemen proyek Django
│
└── requirements.txt              # Daftar dependensi proyek

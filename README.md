my_project/
│
├── my_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── common/  # Aplikasi umum untuk shared utilities, mixins, etc.
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── utils.py
│   │   ├── mixins.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── common/
│   │
│   ├── core/  # Aplikasi utama untuk halaman dasar seperti home, about, contact
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── core/
│   │           └── home.html
│   │           └── contact.html
│   │           └── about.html
│   │
│   ├── team/  # Aplikasi khusus untuk informasi tim
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── team/
│   │           └── team.html
│   │           └── member_detail.html
│   │
│   ├── events/  # Aplikasi untuk mengelola acara
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── templates/
│   │       └── events/
│   │           └── event_list.html
│   │           └── event_detail.html
│   │
│   ├── information/  # Aplikasi untuk informasi khusus (bus, attendance, menu)
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
│   │           └── bus.html
│   │           └── attendance.html
│   │           └── menu.html
│   │
│   ├── forms/  # Aplikasi utama untuk semua form
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   ├── templates/
│   │   │   └── forms/
│   │   │       └── request_training.html
│   │   │       └── leave_request.html
│   │   │       └── salary_complaint.html
│   │   └── approvals/
│   │       ├── __init__.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       ├── templates/
│   │       │   └── approvals/
│   │       │       └── request_training_approval.html
│   │       │       └── leave_request_approval.html
│   │       │       └── salary_complaint_approval.html
│   │       └── static/
│   │           └── approvals/
│
├── manage.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/

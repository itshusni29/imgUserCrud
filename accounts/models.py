from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    class Occupation(models.TextChoices):
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'
        ENGINEER = 'engineer', 'Engineer'
        DOCTOR = 'doctor', 'Doctor'
        OTHER = 'other', 'Other'

    base_role = Role.USER
    role = models.CharField(max_length=5, choices=Role.choices, default=base_role)
    occupation = models.CharField(max_length=20, choices=Occupation.choices, default=Occupation.STUDENT)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

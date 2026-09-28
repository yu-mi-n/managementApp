from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  ROLE_CHOICES = [
    ('Manager', '管理者長'),
    ('staff', 'スタッフ'),
  ]

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, null=False, blank=False, default="staff")
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=False, blank=False)
  department = models.CharField(max_length=20)
  staff_id = models.CharField(max_length=20)
  is_active_on_field = models.BooleanField(default=True)


  

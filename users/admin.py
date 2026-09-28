# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # Adminの一覧画面で表示する項目（独自に追加したフィールドも表示）
    list_display = ['username', 'email', 'is_staff', 'is_active', 'is_active_on_field']
    
    # ユーザー詳細（編集）画面の下部に、独自フィールドを入力できるエリアを追加
    fieldsets = UserAdmin.fieldsets + (
        ('現地の稼働状況', {'fields': ('is_active_on_field',)}),
    )

admin.site.register(User, CustomUserAdmin)
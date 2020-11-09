from django.contrib import admin
from .models import CustomUser, Note
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Note)

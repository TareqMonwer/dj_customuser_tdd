from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreateForm
  form = CustomUserChangeForm
  model = CustomUser
  ordering = ('email', )

  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Permissions', {'fields': ('is_active', 'is_staff',)})
  )

  add_fieldsets = (
    (None, {
      'classes': ('wide', ),
      'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
    }),
  )



admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin

# Register your models here.
from login1.models import Test


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'password')


admin.site.register(Test,BookAdmin)

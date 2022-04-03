from django_neomodel import admin as neo_admin
from django.contrib import admin

# Register your models here.
from weavingPicture.models import Book, MyTeenRomanticComedy, Sport


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "status", "created")


class MyTeenRomanticComedyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "created", "birthday")


class SportAdmin(admin.ModelAdmin):
    list_display = ("uid", "id", "name", "category", "created")


neo_admin.register(Book, BookAdmin)
neo_admin.register(MyTeenRomanticComedy, MyTeenRomanticComedyAdmin)
neo_admin.register(Sport, SportAdmin)

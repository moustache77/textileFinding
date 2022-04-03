from django.contrib import admin

from weavingSearch.models import Periodicals


class PeriodicalsAdmin(admin.ModelAdmin):
    list_display = ("article_url", "category",
                    "title", "authors", "company_list", "keywords", "abstract", "id")


admin.site.register(Periodicals, PeriodicalsAdmin)

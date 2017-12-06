from django.contrib import admin

from django.db import models

# Register your models here.
from Read.models import reading
class readingAdmin(admin.ModelAdmin):
    list_display = ('Bookname','Author','ISBN','Category','Picture','Grade','Ranking','Price','Postage','Quantity','createTime')
admin.site.register(reading, readingAdmin)
#admin.site.register(models.reading)


from django.contrib import admin

from .models import Comment, Company
# Register your models here.
admin.site.register(Company)
admin.site.register(Comment)

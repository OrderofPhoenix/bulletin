from django.contrib import admin
from .models import Bulletin, Comment, Notice
# Register your models here.

admin.site.register(Notice)
admin.site.register(Comment)
admin.site.register(Bulletin)
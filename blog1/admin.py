from django.contrib import admin

from blog1.models import User,Article

# Register your models here.
admin.site.register(User)
admin.site.register(Article)
from django.contrib import admin
from .models import Main, About, Class, ClassImage, Blog, BlogImage

# Register your models here.

admin.site.register(Main)
admin.site.register(About)
admin.site.register(Class)
admin.site.register(ClassImage)
admin.site.register(Blog)
admin.site.register(BlogImage)

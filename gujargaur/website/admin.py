from django.contrib import admin
from .models import *


admin.site.register(WebPage)
admin.site.register(WebPageSection)
#admin.site.register(WebpageContent)

@admin.register(WebpageContent)
class WebpageContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'webpagesection', 'title', 'subtitle', 'description', 'author', 'image')


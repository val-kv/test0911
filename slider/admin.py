from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_thumbnail', 'title')

    def image_thumbnail(self, obj):
        return f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />'
    image_thumbnail.allow_tags = True

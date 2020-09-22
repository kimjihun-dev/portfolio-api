from django.contrib import admin
from .models import Api
from django_summernote.admin import SummernoteModelAdmin


class ApiAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Api, ApiAdmin)


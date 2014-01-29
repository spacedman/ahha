from django.contrib import admin
from models import DailyRecord

class DailyRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(DailyRecord, DailyRecordAdmin)


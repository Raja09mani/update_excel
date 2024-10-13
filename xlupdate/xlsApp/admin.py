from django.contrib import admin
from .models import StudDetail

class StudDetailAdmin(admin.ModelAdmin):
    list_display = ('sid', 'roll', 'sname', 'sclass', 'saddress','tamil', 'english', 'maths', 'science', 'socialscience')
    search_fields = ('sname', 'sclass')


admin.site.register(StudDetail, StudDetailAdmin)


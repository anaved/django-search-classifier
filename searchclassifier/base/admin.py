'''
Created on Aug 20, 2012

@author: Naved
'''
from django.contrib import admin

class BaseModelMinAdmin(admin.ModelAdmin):        
    list_filter = ['is_active', 'added', ]
    list_display = ['is_active', 'added', ]

class BaseModelAdmin(BaseModelMinAdmin):
    list_display = ['name', 'page_header', 'page_title', 'slug', ] + BaseModelMinAdmin.list_display
    search_fields = ['name', 'description', ]

class BaseGeoModelAdmin(BaseModelAdmin):
    pass  

class BaseImageModelAdmin(BaseModelMinAdmin):
    list_display = ['name', 'target_url'] + BaseModelMinAdmin.list_display

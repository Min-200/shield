from django.contrib import admin

# Register your models here.


from .models import Asset

class Example(admin.ModelAdmin):
	list_display = ('created_time','asset_name','asset_number','asset_source','asset_people','asset_application')

admin.site.register(Asset, Example)

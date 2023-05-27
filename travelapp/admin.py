from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Register_table)
admin.site.register(PackageDetails)
admin.site.register(Book)

admin.site.register(Feedback)
admin.site.register(Payment)
class BlogDetails(admin.ModelAdmin):
   fields = (
      'topic','description'
   )
 
   admin.site.register(Places)
   admin.site.register(Rating)
   admin.site.register(Blog)
admin.site.site_header="travello admin"


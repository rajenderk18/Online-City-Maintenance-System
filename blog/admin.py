from django.contrib import admin
from blog.models import Post, Comment, Catogery, Status

class PostAdmin(admin.ModelAdmin):
    list_filter = ['catogery', 'date_posted', 'status', 'zipcode']
    list_display = ['content','catogery', 'date_posted', 'status', 'zipcode']
    list_editable = ['status']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Catogery)
admin.site.register(Status)

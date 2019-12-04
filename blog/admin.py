from django.contrib import admin
from blog.models import Post, Comment, Catogery, Status

class PostAdmin(admin.ModelAdmin):
    list_filter = ['catogery', 'date_posted', 'status', 'zipcode']
    list_display = ['content','catogery', 'date_posted', 'status', 'zipcode']
    list_editable = ['status']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['content', 'date_posted', 'author']
    list_display = ['content', 'date_posted', 'author', 'post_connected']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Catogery)
admin.site.register(Status)

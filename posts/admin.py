from django.contrib import admin
from .models import Post, Comment

class Commentadmininline (admin.TabularInline):
    model = Comment
    fields = ['text',]
    extra = 0

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ['publish_date', 'created_time', 'updated_time']
    inlines = [Commentadmininline,]

# class Commentadmin(admin.ModelAdmin):
#     list_display = ['post','text','created_time']

# Register your models here.
# admin.site.register(Post,Postadmin)
# admin.site.register(Comment,Commentadmin)

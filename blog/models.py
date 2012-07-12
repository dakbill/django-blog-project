from django.db import models
from django.contrib import admin
import datetime
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def body_first_60(self):
      return self.body[:60]
    def __unicode__(self):
        return self.title
class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=60)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    post = models.ForeignKey(Post,related_name='post')
class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search=('title','body')
    list_filter=('title','created')
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','body','created','updated')
    list_filter=('author','created')
class CommentInline(admin.TabularInline):
    model=Comment
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

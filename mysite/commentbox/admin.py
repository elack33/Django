from django.contrib import admin

# Register your models here.
from commentbox.models import CommentBox, BlogPost


class CommentBoxAdmin(admin.ModelAdmin):
    pass
admin.site.register(CommentBox, CommentBoxAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)

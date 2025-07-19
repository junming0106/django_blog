from django.contrib import admin
from mysite.models import Post

# Register your models here.
# 在管理端顯示title跟slug還有上傳時間
class postAmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
admin.site.register(Post, postAmin)
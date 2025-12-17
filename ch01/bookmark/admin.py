from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# register() 함수를 사용하여 아래와 같이 작성도 가능!
# admin.site.register(Bookmark, BookmarkAdmin)
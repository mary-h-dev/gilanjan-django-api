from django.contrib import admin
from .models import Blog, BlogSection, Category, BlogLike, CommentsBlog

class BlogSectionInline(admin.StackedInline):
    model = BlogSection
    extra = 1
    verbose_name = 'بخش'
    verbose_name_plural = 'بخش‌ها'
    sortable_field_name = 'order'


class CommentsBlogInline(admin.TabularInline):
    model = CommentsBlog
    extra = 0
    verbose_name = 'کامنت'
    verbose_name_plural = 'کامنت‌ها'
    fields = ('user', 'text', 'is_active', 'created_at')
    readonly_fields = ('created_at',)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_date', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogSectionInline, CommentsBlogInline]
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('is_active', 'created_date', 'category')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(CommentsBlog)
class CommentsBlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__username', 'blog__title', 'text')

@admin.register(BlogLike)
class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'liked')
    list_filter = ('liked',)
    search_fields = ('user__username', 'blog__title')

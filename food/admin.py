from django.contrib import admin
from .models import Food, FoodSection, FoodCategory, FoodLike, FoodComment


class FoodSectionInline(admin.StackedInline):
    model = FoodSection
    extra = 1
    verbose_name = 'بخش'
    verbose_name_plural = 'بخش‌ها'
    sortable_field_name = 'order'



class FoodCommentInline(admin.TabularInline):
    model = FoodComment
    extra = 0
    verbose_name = 'نظر'
    verbose_name_plural = 'نظرات'
    fields = ('user', 'text', 'is_active', 'created_at')
    readonly_fields = ('created_at',)



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'created_date', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FoodSectionInline, FoodCommentInline]
    search_fields = ('name', 'author__username', 'category__name')
    list_filter = ('is_active', 'created_date', 'category')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)



@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(FoodComment)
class FoodCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__username', 'food__name', 'text')

@admin.register(FoodLike)
class FoodLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'liked')
    list_filter = ('liked',)
    search_fields = ('user__username', 'food__name')

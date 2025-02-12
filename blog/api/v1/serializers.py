from rest_framework import serializers
from blog.models import Blog, BlogSection, CommentsBlog, Category, BlogLike
from tag.models import Tag



class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = ['id', 'title', 'image', 'description', 'order']




class BlogSerializer(serializers.ModelSerializer):
    sections = BlogSectionSerializer(many=True, read_only=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'category', 'author',
            'meta_description', 'page_meta', 'canonical',
            'is_active', 'is_validated', 'tags',
            'created_date', 'updated_date', 'sections'
        ]



class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    sections = BlogSectionSerializer(many=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'slug', 'category',
            'meta_description', 'page_meta', 'canonical',
            'is_active', 'is_validated', 'tags',
            'sections'
        ]

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        tags_data = validated_data.pop('tags')
        blog = Blog.objects.create(author=self.context['request'].user, **validated_data)
        blog.tags.set(tags_data)
        for section_data in sections_data:
            BlogSection.objects.create(blog=blog, **section_data)
        return blog

    def update(self, instance, validated_data):
        sections_data = validated_data.pop('sections', None)
        tags_data = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            instance.tags.set(tags_data)

        if sections_data is not None:
            # حذف بخش‌های قدیمی
            instance.sections.all().delete()
            # اضافه کردن بخش‌های جدید
            for section_data in sections_data:
                BlogSection.objects.create(blog=instance, **section_data)

        return instance

class CommentsBlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = CommentsBlog
        fields = [
            'id', 'user', 'blog', 'text', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['is_active', 'created_at', 'updated_at']

class CommentsBlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsBlog
        fields = ['id', 'blog', 'text']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

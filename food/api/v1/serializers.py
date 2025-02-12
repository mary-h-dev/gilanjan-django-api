from rest_framework import serializers
from food.models import Food, FoodSection, FoodComment, FoodCategory, FoodLike
from tag.models import Tag





class FoodSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodSection
        fields = ['id', 'title', 'image', 'description', 'order']




class FoodSerializer(serializers.ModelSerializer):
    sections = FoodSectionSerializer(many=True, read_only=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        queryset=FoodCategory.objects.all(),
        slug_field='name'
    )
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Food
        fields = [
            'id', 'name', 'slug', 'category', 'author',
            'ingredients', 'recipe', 'image',
            'is_active', 'created_date', 'updated_date', 'sections', 'tags'
        ]





class FoodCreateUpdateSerializer(serializers.ModelSerializer):
    sections = FoodSectionSerializer(many=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        queryset=FoodCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Food
        fields = [
            'id', 'name', 'slug', 'category',
            'ingredients', 'recipe', 'image',
            'is_active', 'sections', 'tags'
        ]

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        tags_data = validated_data.pop('tags')
        food = Food.objects.create(author=self.context['request'].user, **validated_data)
        food.tags.set(tags_data)
        for section_data in sections_data:
            FoodSection.objects.create(food=food, **section_data)
        return food

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
                FoodSection.objects.create(food=instance, **section_data)

        return instance




class FoodCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())

    class Meta:
        model = FoodComment
        fields = [
            'id', 'user', 'food', 'text', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['is_active', 'created_at', 'updated_at']




class FoodCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ['id', 'food', 'text']





class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', 'name']

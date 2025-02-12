from rest_framework import serializers
from useraccount.models import User

class UserDetailSerializer(serializers.ModelSerializer):
    avatar_url = serializers.ReadOnlyField()  # صراحتاً مشخص کنید که avatar_url فقط خواندنی است

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'avatar_url')
        read_only_fields = ('id', 'avatar_url')  

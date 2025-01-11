from rest_framework.serializers import ModelSerializer
from .models import User, IPOInfo

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class IPOInfoSerializer(ModelSerializer):
    class Meta:
        model = IPOInfo
        fields = ['id', 'company_name', 'ipo_date', 'price']
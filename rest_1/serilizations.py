from rest_framework import serializers
from .models import book, temp


class book_s(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'


'''class book_s(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=10)
    auth = serializers.CharField(max_length=50, min_length=10)
'''


class temp_s(serializers.ModelSerializer):
    class Meta:
        model = temp
        fields = '__all__'

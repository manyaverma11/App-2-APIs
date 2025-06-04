from rest_framework import serializers
from .models import Name

class NameSerializer(serializers.ModelSerializer):
    education_degree = serializers.CharField(source='education.degree', read_only=True)
    
    class Meta:
        model = Name
        fields = ['id', 'first_name', 'last_name', 'education', 'education_degree']
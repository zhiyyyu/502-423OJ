from rest_framework import serializers
from problemlist.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Problem
        fields = [
            'id',
            'title',
            'created',
        ]

class ProblemDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Problem
        fields = '__all__'
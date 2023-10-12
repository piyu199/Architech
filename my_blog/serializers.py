from .models import BlogPost
from rest_framework import serializers

class BlogPost_serializers(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['pk','title','body']
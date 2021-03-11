from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('categr_id', 'category_name')


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # get_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True) 
    get_absolute_url = serializers.SerializerMethodField()    

    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url() 
    class Meta:
        model = Article
        fields = ('headline', 'get_absolute_url', 'picture', 'category', 'date_published', 'body', 'trending')



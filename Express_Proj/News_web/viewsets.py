from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Category, Article
from .serializers import  ArticleSerializer, CategorySerializer
from rest_framework import viewsets
from django_filters import rest_framework as filter
import django_filters
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import date

from django_filters.widgets import RangeWidget


class ArticleFilter(filter.FilterSet):
    # category = filter.CharFilter(lookup_expr='iexact')
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    print(today)
    latest_date = (
        (today,'Today'),#('Today', today) --- Will not work
        (yesterday, 'Yesterday')#('Yesterday', yesterday)
    )
    
    date_published = filter.ChoiceFilter(choices=latest_date)
    class Meta:
        model = Article
        fields = ['category', 'date_published', 'trending']
        
class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer
    filterset_class = ArticleFilter

    def newest(self, request):
        newest = self.get_queryset().order_by('date_published').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer


from django.shortcuts import render
from News_web.models import Article, Category, Author, SocialMedias
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
import time
# from rest_framework import viewsets
from .serializers import ArticleSerializer, CategorySerializer
# Create your views here.
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
#API REst
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import Http404
from django.db.models import ObjectDoesNotExist
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.decorators import login_required

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        if isinstance(o, ImageFieldFile):
            try:
                return o.url
            except ValueError:
                return ''
            raise TypeError(repr(o) + " is not JSON serializable")

        return super().default(o)

def index(request):
    return render(request, "News_web/index.html",{
    })
# def latest_getter():
#     day =1
#     list_article = []
#     if day <= 5: 
#         today = timezone.now()
#         yesterday = today - datetime.timedelta(days=day)
#         latest = Article.objects.filter(date_published__range=(yesterday, today))   
#         if len(latest) == 0:
#             day+=2
#             yesterday = today - datetime.timedelta(days=day)
#         for i in latest:
#             art = {}
#             art['head'] = i.headline
#             art['leads'] = i.body
#             art['image'] = i.picture.url
#             art['category'] = i.category
#             art['url'] = i.get_absolute_url()                
#             list_article.append(art)
#     return list_article

# def latest_article(request):
        
#     return JsonResponse({
#         'latest': latest_getter()
#     }, encoder=ExtendedEncoder, safe=True)
# Article View
def article_view(request, slug):
    
    try:
        article_list = Article.objects.get(slug=slug)
        email = article_list.author
        author_soc = SocialMedias.objects.get(user=email)
        creator = article_list.author.get_full_name()
        title = article_list.headline
        date = article_list.date_published
        content = article_list.body
        picture = article_list.picture
        catego = article_list.category.category_name

        user_fb = author_soc.soc_fb
        user_tw = author_soc.soc_tw
        user_ig = author_soc.soc_ig
        color = Category.objects.get(category_name=catego).category_color
        if slug == article_list.slug:
            
            return render(request, "News_web/article_view.html",{
                "title": title,
                "date":date,
                "content":content,
                "photo":picture,
                "author":creator,
                "category":catego,
                "user_fb": user_fb,
                "user_ig": user_ig,
                "user_tw": user_tw,
                "color":color
            })
        else:
            return render(request, "News_web/util/error.html",{
                "find":slug
            })
    except ObjectDoesNotExist:
        return render(request, "News_web/util/error.html",{
            "find":slug
        })
    

    


def about_us(request):
    return render(request,"News_web/about_n.html",{
    })

def terms(request):
    pass


@login_required(redirect_field_name='personel_log')
def dashboard_admin(request):
    author = request.user.get_short_name()
    return render(request, "News_web/admin-tem/dashboard_admin.html",{
        "name_full" : author
    })
@login_required(redirect_field_name='personel_log')
def profile_sett(request):
    return render(request, 'News_web/admin-tem/profile_settings.html',{})

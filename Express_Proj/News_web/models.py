from django.db import models
import uuid
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify 
from django.urls import reverse
from django.contrib import admin
from datetime import datetime, date, timedelta
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.




class Author(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=80, blank=False,null=False)
    last_name = models.CharField(max_length=80, blank=False)
    profile_picture = models.ImageField(blank=True,null=True,upload_to="News_web/static/images/admin_profiles", default="News_web/static/images/default-profile.png")
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name']

    objects = CustomUserManager()

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    def get_short_name(self):
        return self.first_name
    def __str__(self):
        return self.email
class Category(models.Model):
    categr_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=15)
    category_color = models.CharField(blank=False,max_length=20, default="#c63e40")

    def __str__(self):
        return self.category_name
    
class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    headline = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, unique=True, max_length=255, default='')
    body = models.TextField(null=False, blank=False)
    picture = models.ImageField(null=False, upload_to="artcle_thumb")
    video = models.FileField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name="category_id", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    trending = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('article_view', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline, self.article_id)
        super(Article, self).save(*args, **kwargs)
    def __str__(self):
        # template = self.headline, self.category,self.author,self.picture
        # return template.format(self)
        return self.headline
    
    def url(obj):
        try: 
            if isinstance(obj, ImageFieldFile):
                return obj.url
        except:
            url = ''
        return url

    # def latest_news_today(self):
    #     right_time = datetime.today()
    #     return cls.objects.filter(date_published__hour = right_time.hour, date_published__minute = right_time.minute,date_published__year = right_time.year, date_published__month = right_time.month, date_published__day=right_time.day)

    @property 
    def trending_article(self):
        trending_now = True
        trend=cls.objects.filter(trending=trending_now).order_by('-date_published')
        return trend

class SocialMedias(models.Model):
    user = models.OneToOneField(Author,related_name="user_email",on_delete=models.CASCADE,unique=True)
    soc_fb = models.CharField(null=True, max_length=60, default='@', verbose_name="Facebook")
    soc_tw = models.CharField(null=True,max_length=60, default='@', verbose_name="Twitter")
    soc_ig = models.CharField(null=True,max_length=60, default='@', verbose_name="Instagram")
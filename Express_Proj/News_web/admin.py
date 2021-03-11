from django.contrib import admin

# Register your models here.
from .models import Article, Author, Category, SocialMedias
from .forms_LR import AuthorCreationForm, AuthorChangeForm
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User


class SocialMInline(admin.TabularInline):
    SocialMedia = SocialMedias
    model = SocialMedia
    fieldsets = [
        ('Social Media',{'fields':('soc_fb','soc_tw','soc_ig')})
    ]

class AuthorAdmin(UserAdmin):
    add_form = AuthorCreationForm
    form = AuthorChangeForm
    model = Author
    list_display = ('email','first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('first_name', 'last_name','email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name', 'last_name', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','email', 'password1', 'password2', 'profile_picture','is_staff', 'is_active', 'is_superuser')}
        ),
    )
    inlines = [SocialMInline]
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['headline', 'author', 'date_published', 'category',]
    prepopulated_fields = {'slug': ('headline',)} 
admin.site.register(Article, ArticleAdmin)

class SocialMAdmin(admin.ModelAdmin):
    model = SocialMedias
    list_display=['user','soc_fb','soc_tw','soc_ig']

admin.site.register(SocialMedias,SocialMAdmin)

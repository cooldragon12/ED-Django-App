from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, reverse
from News_web.models import Author, Article,Category
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets 

class Create_articleForm(forms.ModelForm):
    date_published = forms.DateTimeField(input_formats=["%Y/%m/%d %I:%m %p"])
    class Meta:
        model = Article
        fields = ['headline', 'body', 'category']
        
    # def __init__(self, *args, **kwargs):
    #     super(Create_articleForm, self).__init__(*args, **kwargs)
        
        # self.fields['date_published'].widget.attrs.update({"class":"datetimepicker"})
class Edit_articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'body', 'category', 'picture']       

class AuthorChangeForm(UserChangeForm):
    class Meta:
        model = Author
        fields = ('email','password', 'first_name', 'last_name','profile_picture')

class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Author
        fields = ('email','password', 'first_name', 'last_name', 'profile_picture')
def login_per(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/account/')
                else:
                    er = "Invalid Username or Password. Try again"
                    return render(request, "News_web/Log1n_us3r.html",{
                        "form": form,
                            "error" : er})
            else:
                er = "Invalid Username or Password. Try again"
                return render(request, "News_web/Log1n_us3r.html",{
                        "form": form,
                        "error" : er})

        form = AuthenticationForm()
        return render(request,
            template_name = "News_web/Log1n_us3r.html",
            context={"form":form})
@login_required(redirect_field_name='personel_log')
def create_form(request):
    if request.user.is_authenticated:
        uthor = request.user
        if request.method == 'POST':
            form = Create_articleForm(request.POST)
            if form.is_valid():
                headline = form.cleaned_data.get('id_headline')
                body = form.cleaned_data.get('id_body')
                category = form.cleaned_data.get('id_category')
                picture_media = request.POST.get('fileElem')
                date_published = form.cleaned_data.get('date_published')
                exist_head = Article.objects.get(headline)
                if headline not in exist_head:
                    obj = Article.objects.create(
                        headline=headline,
                        body=body,
                        category=category,
                        author=uthor,
                        picture=picture_media,
                        date_published=date_published
                    )
                    obj.save()
                    return HttpResponse('Createed Successfully')
                else:
                    pass
        else:
            form = Create_articleForm()
        form = Create_articleForm()
        author = request.user.get_short_name()
        return render(request, "News_web/admin-tem/cr3ate_f0rm.html", {
            "form" : form,
            "name_full":author
        }) 
    else:
        return HttpResponseRedirect(reverse(login_per('GET')))


def logoutview(request):

    logout(request)
    return redirect('/')

from django.test import TestCase, LiveServerTestCase, Client
from django import test
from News_web.models import Article, Category, Author, SocialMedias
from django.utils import timezone 
from django.contrib.auth import get_user_model
from selenium import webdriver
from django.db.models import ObjectDoesNotExist
# Create your tests here.
# Query to test
c1 = Category(category_name='News')
c2 = Category(category_name='Entertainment')
c3 = Category(category_name='Sports')
c4 = Category(category_name='Opinion')
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.fields.files import ImageFieldFile

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


# Test Cases
class AddNewEntries(TestCase):
    def setUp(self):
        Category.objects.create(category_name=c1, category_color="#c63e40")
        Category.objects.create(category_name=c2, category_color="#c63e40")
        
        Author.objects.create(email="sample@gmail.com",password="samplepass", first_name="John", last_name="Doe")
        
    def test_create_author(self):
        newAuthor = Author.objects.create(email="dla2@gmail.com",password="samplepass", first_name="John2", last_name="Doe2")
        self.assertEqual(newAuthor.email, 'dla2@gmail.com')
        self.assertTrue(newAuthor.is_active)
        self.assertFalse(newAuthor.is_staff)
        self.assertFalse(newAuthor.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(Author.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            Author.objects.create_user()
        with self.assertRaises(TypeError):
            Author.objects.create_user(email='')
        with self.assertRaises(ValueError):
            Author.objects.create_user(email='', password="foo", first_name="john")
    def test_create_category(self):
        Category.objects.create(category_name=c3, category_color="#c63e40")
        Category.objects.create(category_name=c4, category_color="#c63e40")
    def test_create_article(self):
        # newAuthor = Author.objects.create(email="sample@gmail.com",password="samplepass", first_name="John", last_name="Doe")
        # cat1 = Category.objects.create(category_name=c1, category_color="#c63e40")
        # cat2 = Category.objects.create(category_name=c2, category_color="#c63e40")
        auth = Author.objects.get(email="sample@gmail.com").pk
        ca1 = Category.objects.get(category_name="News").pk
        ca2 = Category.objects.get(category_name="Entertainment").pk

        article = Article.objects.create(headline="Try ko kung gagana", body="This random paragraph", category=Category(ca1),date_published=timezone.now(), author=Author(auth))
        article1 = Article.objects.create(headline="Try ko kung gagana1", body="This random paragraph1", category=Category(ca2),date_published=timezone.now(), author=Author(auth))

class ViewResponse(TestCase):
    def setUp(self):
        Category.objects.create(category_name=c1, category_color="#c63e40")
        Category.objects.create(category_name=c2, category_color="#c63e40")
        
        Author.objects.create(email="sample@gmail.com",password="samplepass", first_name="John", last_name="Doe")
        auth = Author.objects.get(email="sample@gmail.com").pk
        ca1 = Category.objects.get(category_name="News").pk
        ca2 = Category.objects.get(category_name="Entertainment").pk
        SocialMedias.objects.create(user=Author(auth), soc_fb="@johnD", soc_tw="@johnD",soc_ig="@johnD")
        Article.objects.create(headline="Try ko kung gagana", body="This random paragraph ABC", category=Category(ca1),date_published=timezone.now(), author=Author(auth), trending=True, picture="News_web/static/images/admin_profiles/default-profile.png")
        Article.objects.create(headline="Try ko kung gagana Ito pa isa", body="This random paragraph 123", category=Category(ca2),date_published=timezone.now(), author=Author(auth), trending=True, picture="News_web/static/images/admin_profiles/default-profile.png")
        
    # Article View
    def test_article_view(self):
        sample_article = Article.objects.get(headline="Try ko kung gagana").slug
        response = self.client.get(f'/article/{sample_article}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'News_web/article_view.html')
    def test_article_view_404(self):
        sample_article = "saip-sa"
        response = self.client.get(f'/article/{sample_article}', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'News_web/util/error.html')
    def test_call_login_deny_anonymous(self):
        response = self.client.get('/account/', follow=True)
        self.assertRedirects(response, '/account/login_colleage/?personel_log=/account/')
    def test_login_faild(self):
        passwo = Author.objects.get(email="sample@gmail.com").password
        self.client.login(username="sample@gmail.com", password=f"{passwo}")
        response = self.client.get("/account/", follow=True)
        self.assertTemplateUsed(response, 'News_web/Log1n_us3r.html')


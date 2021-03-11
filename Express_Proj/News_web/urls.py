from django.urls import include ,path
from . import views, forms_LR
from django.conf import settings

urlpatterns = [
    #Index/Home/ Article View
    path("", views.index, name="index"),
    # path("latest/", views.latest_article, name="latest"),
    path("article/<slug:slug>/", views.article_view, name="article_view"),
    #About Website url
    path("terms_conditions/", views.terms, name="term_condition"),
    path("about/", views.about_us, name="about"),
    #Login/ Portal
    path("account/login_colleage/", forms_LR.login_per, name='personel_log'),
    # DashBoards
    path("account/", views.dashboard_admin, name='dashboard'),
    path("account/create_new/", forms_LR.create_form, name='create_new'),
    path("account/logout/", forms_LR.logoutview, name='logout_view'),
    path("account/account_settings/", forms_LR.create_form, name='acc_settings'),
] 

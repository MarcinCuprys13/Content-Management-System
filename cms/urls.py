from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from ibicms.views import business_creator, choose_cms_template, home, newsletter_creator, portfolio_creator
from django.urls import path, include

urlpatterns = [
    path("", home, name="home"), 
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path('home/', home, name='home'),
    
    path('choose-template/', choose_cms_template, name='choose_cms_template'),
    path('portfolio-creator/', portfolio_creator, name='portfolio_creator'),
    path('newsletter-creator/', newsletter_creator, name='newsletter_creator'),
    path('business-creator/', business_creator, name='business_creator'),


    
]

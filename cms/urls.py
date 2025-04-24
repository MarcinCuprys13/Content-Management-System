from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.urls import path
from ibicms.views import business_creator, choose_cms_template, edit_card, edit_newsletter, edit_portfolio, home, newsletter_creator, portfolio_creator, portfolio_preview, delete_portfolio, delete_card, delete_newsletter, newsletter_preview, card_preview
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

    path('portfolio/<int:id>/', portfolio_preview, name='portfolio_page'),
    path('newsletter/<int:id>/', newsletter_preview, name='newsletter_page'),
    path("card/<int:id>/", card_preview, name="card_page"),


    path('portfolio/<int:id>/delete/', delete_portfolio, name='delete_portfolio'),
    path('newsletter/<int:id>/delete/', delete_newsletter, name='delete_newsletter'),
    path('card/<int:id>/delete/', delete_card, name='delete_card'),

    #edit
    path('portfolio/edit/<int:id>/', edit_portfolio, name='edit_portfolio'),
    path('card/edit/<int:id>/', edit_card, name='edit_card'),
    path('newsletter/edit/<int:id>/', edit_newsletter, name='edit_newsletter'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

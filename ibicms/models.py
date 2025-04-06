from django.contrib.auth.models import User
from django.db import models


class ProfilePortfolio(models.Model):
    title = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    hero_text = models.TextField() 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    project_text = models.TextField() 
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    user_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  
    website_photo = models.ImageField(upload_to='website_photos/', blank=True, null=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProfileNewsletter(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    promo_text = models.TextField()
    head_color = models.CharField(max_length=7)
    project_text = models.TextField()
    body_color = models.CharField(max_length=7)
    footer_color = models.CharField(max_length=7)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    user_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    website_photo = models.ImageField(upload_to='website_photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProfileCard(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=20)
    person_text = models.TextField() 
    linkedin_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)  
    mypage_url = models.URLField(max_length=200)
    body_color = models.CharField(max_length=7)  
    footer_color = models.CharField(max_length=7)  
    actual_company = models.CharField(max_length=20)
    user_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import ProfilePortfolio, ProfileCard
from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def home(request):
    user_portfolios = list(ProfilePortfolio.objects.filter(user=request.user))
    user_card = list(ProfileCard.objects.filter(user=request.user))
    print("uytwkonik zalogowany")
    print(user_portfolios)
    print(user_card)
    return render(request, 'home.html', {'user_profiles': user_portfolios + user_card})

@login_required(login_url='/accounts/login/')
def choose_cms_template(request):
    return render(request, 'choose_template.html')

@login_required(login_url='/accounts/login/')
def newsletter_creator(request):
    return render(request, 'choose_template.html')

@login_required(login_url='/accounts/login/')
def portfolio_creator(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        hero_title = request.POST.get('hero_title')
        hero_text = request.POST.get('hero_text')
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        project_text = request.POST.get('project_text')
        user_photo = request.FILES.get('user_photo')
        website_photo = request.FILES.get('website_photo')

        ProfilePortfolio.objects.create(
            user=request.user,
            title=title,
            hero_title=hero_title,
            hero_text=hero_text,
            # first_name=first_name,
            # last_name=last_name,
            phone=phone,
            email=email,
            project_text=project_text,
            user_photo=user_photo,
            website_photo=website_photo
        )
        return redirect('home')

    return render(request, 'creators/portfolio_creator.html')

@login_required(login_url='/accounts/login/')
def business_creator(request):
    return render(request, 'choose_template.html')

# @login_required(login_url='/accounts/login/') 
# def page_creator(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         first_name = request.POST.get('firstName')
#         last_name = request.POST.get('lastName')
#         person_text = request.POST.get("personText")
#         head_color = request.POST.get('headColor')
#         project_text = request.POST.get("projectText")
#         body_color = request.POST.get('bodyColor')
#         footer_color = request.POST.get('footerColor')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         user_photo = request.FILES.get('user_photo')
#         website_photo = request.FILES.get('website_photo')

#         profile = Profile(
#             title=title,
#             first_name=first_name,
#             last_name=last_name,
#             person_text=person_text,
#             head_color=head_color,
#             project_text=project_text,
#             body_color=body_color,
#             footer_color=footer_color,
#             phone=phone,
#             email=email,
#             user_photo=user_photo,
#             website_photo=website_photo,
#             user=request.user  
#         )
#         profile.save()
#         return redirect('home')
#     else:
#         return render(request, 'page_creator.html')
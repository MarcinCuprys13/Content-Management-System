from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import ProfilePortfolio, ProfileCard, ProfileNewsletter
from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html', {
        'portfolios': ProfilePortfolio.objects.filter(user=request.user),
        'newsletters': ProfileNewsletter.objects.filter(user=request.user),
        'cards': ProfileCard.objects.filter(user=request.user),
    })

@login_required(login_url='/accounts/login/')
def choose_cms_template(request):
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
    if request.method == 'POST':
        ProfileCard.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            title=request.POST.get('title'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            country=request.POST.get('country'),
            person_text=request.POST.get('person_text'),
            linkedin_url=request.POST.get('linkedin_url'),
            github_url=request.POST.get('github_url'),
            mypage_url=request.POST.get('mypage_url'),
            body_color=request.POST.get('body_color'),
            footer_color=request.POST.get('footer_color'),
            user_photo=request.FILES.get('user_photo')
        )
        return redirect('home')

    return render(request, 'creators/card_creator.html')

@login_required(login_url='/accounts/login/')
def newsletter_creator(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        email = request.POST.get('email')
        project_text = request.POST.get('project_text')
        image = request.FILES.get('image')
        head_color = request.POST.get('head_color')
        body_color = request.POST.get('body_color')
        footer_color = request.POST.get('footer_color')

        ProfileNewsletter.objects.create(
            user=request.user,
            title=title,
            subtitle=subtitle,
            email=email,
            project_text=project_text,
            image=image,
            head_color=head_color,
            body_color=body_color,
            footer_color=footer_color
        )

        return redirect('home')

    return render(request, 'creators/newsletter_creator.html')
    pass

@login_required(login_url="/accounts/login/")
def portfolio_preview(request, id):
    profile = get_object_or_404(ProfilePortfolio, pk=id)
    return render(request, 'portfolio_template.html', {
        'ProfilePortfolio': profile
    })
@login_required(login_url="/accounts/login/")
def newsletter_preview(request, id):
    item = get_object_or_404(ProfileNewsletter, id=id, user=request.user)
    return render(request, 'newsletter_template.html', {'item': item})

@login_required(login_url="/accounts/login/")
def card_preview(request, id):
    item = get_object_or_404(ProfileCard, id=id, user=request.user)
    return render(request, "card_template.html", {"item": item})

def delete_portfolio(request, id):
    if request.method == "POST":
        item = get_object_or_404(ProfilePortfolio, id=id, user=request.user)
        item.delete()
    return redirect('home')

def delete_newsletter(request, id):
    if request.method == "POST":
        item = get_object_or_404(ProfileNewsletter, id=id, user=request.user)
        item.delete()
    return redirect('home')

def delete_card(request, id):
    if request.method == "POST":
        item = get_object_or_404(ProfileCard, id=id, user=request.user)
        item.delete()
    return redirect('home')



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
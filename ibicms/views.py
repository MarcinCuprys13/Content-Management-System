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

#CREATORS
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
        content = request.POST.get('content')
        email = request.POST.get('email')
        project_text = request.POST.get('project_text')
        image = request.FILES.get('image')
        footer_color = request.POST.get('footer_color')

        ProfileNewsletter.objects.create(
            user=request.user,
            title=title,
            content=content,
            email=email,
            image=image,
            footer_color=footer_color
        )

        return redirect('home')

    return render(request, 'creators/newsletter_creator.html')

#EDITORS
@login_required(login_url='/accounts/login/')
def edit_newsletter(request, id):
    newsletter = get_object_or_404(ProfileNewsletter, id=id, user=request.user)

    if request.method == 'POST':
        newsletter.title = request.POST.get('title')
        newsletter.content = request.POST.get('content')
        newsletter.email = request.POST.get('email')
        # newsletter.project_text = request.POST.get('project_text')
        # newsletter.head_color = request.POST.get('head_color')
        # newsletter.body_color = request.POST.get('body_color')
        newsletter.footer_color = request.POST.get('footer_color')

        if 'image' in request.FILES:
            newsletter.image = request.FILES.get('image')

        newsletter.save()
        return redirect('home')

    return render(request, 'editors/newsletter_editor.html', {
        'newsletter': newsletter
    })

@login_required(login_url='/accounts/login/')
def edit_portfolio(request, id):
    portfolio = get_object_or_404(ProfilePortfolio, id=id, user=request.user)

    if request.method == 'POST':
        portfolio.title = request.POST.get('title')
        portfolio.hero_title = request.POST.get('hero_title')
        portfolio.hero_text = request.POST.get('hero_text')
        portfolio.phone = request.POST.get('phone')
        portfolio.email = request.POST.get('email')
        portfolio.project_text = request.POST.get('project_text')

        if 'user_photo' in request.FILES:
            portfolio.user_photo = request.FILES.get('user_photo')
        if 'website_photo' in request.FILES:
            portfolio.website_photo = request.FILES.get('website_photo')

        portfolio.save()
        return redirect('home')

    return render(request, 'editors/portfolio_editor.html', {
        'portfolio': portfolio
    })

@login_required(login_url='/accounts/login/')
def edit_card(request, id):
    card = get_object_or_404(ProfileCard, id=id, user=request.user)

    if request.method == 'POST':
        card.first_name = request.POST.get('first_name')
        card.last_name = request.POST.get('last_name')
        card.title = request.POST.get('title')
        card.phone = request.POST.get('phone')
        card.email = request.POST.get('email')
        card.country = request.POST.get('country')
        card.person_text = request.POST.get('person_text')
        card.linkedin_url = request.POST.get('linkedin_url')
        card.github_url = request.POST.get('github_url')
        card.mypage_url = request.POST.get('mypage_url')
        card.body_color = request.POST.get('body_color')
        card.footer_color = request.POST.get('footer_color')

        if 'user_photo' in request.FILES:
            card.user_photo = request.FILES.get('user_photo')

        card.save()
        return redirect('home')

    return render(request, 'editors/card_editor.html', {
        'card': card
    })


#PREVIEWS
@login_required(login_url="/accounts/login/")
def portfolio_preview(request, id):
    profile = get_object_or_404(ProfilePortfolio, pk=id)
    return render(request, 'portfolio_template.html', {
        'ProfilePortfolio': profile
    })

@login_required(login_url="/accounts/login/")
def newsletter_preview(request, id):
    item = get_object_or_404(ProfileNewsletter, id=id, user=request.user)
    return render(request, 'newsletter_template.html', {'ProfileNewsletter': item})

@login_required(login_url="/accounts/login/")
def card_preview(request, id):
    item = get_object_or_404(ProfileCard, id=id, user=request.user)
    return render(request, "card_template.html", {"item": item})

#DELETES
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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfilePortfolio, ProfileCard
from django.shortcuts import render
from .forms import ProfileNewsletterForm

@login_required(login_url='/accounts/login/') 
def home(request):
    if request.user.is_authenticated:
        user_portfolios = ProfilePortfolio.objects.filter(user=request.user)
        user_card = ProfileCard.objects.filter(user=request.user)
        return render(request, 'home.html', {'user_pages': user_portfolios + user_card})
    else:
        return render(request, 'base.html')

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

@login_required
def create_newsletter(request):
    if request.method == 'POST':
        form = ProfileNewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.user = request.user
            newsletter.save()
            return redirect('newsletter_success')
    else:
        form = ProfileNewsletterForm()
    return render(request, 'creators/create_newsletter.html', {'form': form})
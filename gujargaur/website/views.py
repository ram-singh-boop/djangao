from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.models import User
from .models import WebpageContent, WebPage
from blog.models import Post

def get_menu():
    menu = WebPage.objects.all()
    #print(menu)
    return menu


# Create your views here.
def home(request):
    #menu = get_menu()
   # print(menu)
    all_posts = Post.objects.all()

    #print(all_posts)
    homepage = {
    'silder_image': WebpageContent.objects.filter(webpagesection__title="silder"),
    'welcome_to_our': WebpageContent.objects.filter(webpagesection__title="Welcome to our"),
    'welcome_to_our_image': WebpageContent.objects.filter(webpagesection__title="Welcome to our", title__startswith="Welcome to our").first().image.url,
    'service_content': WebpageContent.objects.filter(webpagesection__title="service"),
    'team_members': WebpageContent.objects.filter(webpagesection__title="Our Team Members"),
    'team_members_decription': WebpageContent.objects.filter(webpagesection__title="Our Team Members description"),
    'get_a_free_mobile_app': WebpageContent.objects.filter(webpagesection__title="Get a free mobile app"),
    'get_a_free_mobile_app_image': WebpageContent.objects.filter(webpagesection__title="Get a free mobile app", title="Get a free mobile app").first().image.url,

    }


    return render(request, 'website/home.html', {'homepage': homepage,'menus':get_menu(), 'posts': all_posts})


def aboutus(request):
    context = {
        'why_us': WebpageContent.objects.filter(webpagesection__title="Why Choose Us"),
        'why_us_image': WebpageContent.objects.filter(webpagesection__title="Why Choose Us", title="Section Image").first().image.url,
        'welcome_to_our': WebpageContent.objects.filter(webpagesection__title="Welcome to our"),
        'welcome_to_our_image': WebpageContent.objects.filter(webpagesection__title="Welcome to our", title__startswith="Welcome to our").first().image.url,
        'top_content': WebpageContent.objects.filter(webpagesection__title="Top Content"),
        'customerssay': WebpageContent.objects.filter(webpagesection__title="Customers Say"),
        'get_a_free_mobile_app': WebpageContent.objects.filter(webpagesection__title="Get a free mobile app"),
        'get_a_free_mobile_app_image': WebpageContent.objects.filter(webpagesection__title="Get a free mobile app",  title="Get a free mobile app").first().image.url,


    }
    #print(context['welcome_to_our_image'])
    return render(request, 'website/aboutus.html', {'context': context,'menus':get_menu()})

def blogsingle(request):
    return render(request, 'website/blogsingle.html', {'title': 'blogsingle'})


def blog(request):

    return render(request, 'blog/home.html', {'title': 'blog','menus':get_menu()})

def contact(request):
    contactpage = {
        'contact_heading': WebpageContent.objects.filter(webpagesection__title="Contact Subheadings"),
        'maps_google': WebpageContent.objects.filter(webpagesection__title="google map iframe", title="gool map"),

    }
    return render(request, 'website/contact.html', {'contactpage': contactpage,'menus':get_menu()})

def faq(request):
    faqspage = {
        'faqs_accordions': WebpageContent.objects.filter(webpagesection__title="Faqs accordions"),
        'faqs_accordions_image': WebpageContent.objects.filter(webpagesection__title="Faqs accordions", title="Faqs accordions").first().image.url,
        'faqs_quesrtions': WebpageContent.objects.filter(webpagesection__title="Top 10 Frequently asked questions"),

    }
    return render(request, 'website/faq.html', {'faqspage': faqspage,'menus':get_menu()})

def gallery(request):
    gallerybulk = {
      # 'galley_title': WebpageContent.objects.filter(webpagesection__title="Our Gallery"),
        'galley_image': WebpageContent.objects.filter(webpagesection__title="Our Gallery", title="Latest Gallery"),

    }
  #  print(gallerybulk['galley_image'])
    return render(request, 'website/gallery.html', {'gallerybulk': gallerybulk,'menus':get_menu()})

def login(request):
    return render(request, 'website/login.html', {'title': 'login'})

def portfolio(request):
    return render(request, 'website/portfolio.html', {'title': 'portfolio'})

def searchresults(request):
    return render(request, 'website/searchresults.html', {'title': 'searchresults'})

def services(request):
    return render(request, 'website/services.html', {'title': 'services'})

def signup(request):
    return render(request, 'website/signup.html', {'title': 'signup'})

def teamsingle(request):
    return render(request, 'website/teamsingle.html', {'title': 'teamsingle'})

def team(request):
    return render(request, 'website/team.html', {'title': 'team'})


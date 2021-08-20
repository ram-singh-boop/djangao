from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name="website-home"),
    path('aboutus', views.aboutus, name="website-aboutus"),
    path('blogsingle', views.blogsingle, name="website-blogsingle"),
    path('blog', views.blog, name="website-blog"),
    path('contact', views.contact, name="website-contact"),
    path('faq', views.faq, name="website-faq"),
    path('gallery', views.gallery, name="website-gallery"),
    path('login', views.login, name="website-login"),
    path('portfolio', views.portfolio, name="website-portfolio"),
    path('searchresults', views.searchresults, name="website-searchresults"),
    path('services', views.services, name="website-services"),
    path('signup', views.signup, name="website-signup"),
    path('teamsingle', views.teamsingle, name="website-teamsingle"),
    path('team', views.team, name="website-team"),
    #path('404', views.404, name="website-404"),

]
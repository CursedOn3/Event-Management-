from django.contrib import admin
from django.urls import path
from home import views
# In your urls.py
from django.conf import settings
from django.conf.urls.static import static
from .views import register
    


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("gallery", views.gallery, name='gallery'),
    path("contact", views.contact, name='contact'),
    path("login", views.login_user, name='login'),
    path("register", views.register, name='register'),
    path("profile", views.profile, name='profile'),
    path("seed", views.seed_data, name='seed'),

    path("events", views.list_event, name='list_events'),
    path("events/my", views.list_my_events, name='list_my_events'),
    path("events/book", views.book_events, name='book_events'),

    path("logout", views.logout_user, name='logout'),
    ] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
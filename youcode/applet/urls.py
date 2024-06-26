# accounts/urls.py
from django.urls import path
from .views import SignUpView,  upload_event, home, event_display
from .views import prize_list
from django.urls import path, include  # new
from .views import about_us


urlpatterns = [
     path("", home, name="home"),
     path("signup/", SignUpView.as_view(), name="signup"),
     path('upload-event/', upload_event, name='upload_event'),
     path("prizes/", prize_list, name='prize_list'),
     path("login/", include("django.contrib.auth.urls"), name = "login"),
     path("aboutus/", about_us, name='about_us'),
     path('event_display/', event_display , name = 'event_display'), 

]
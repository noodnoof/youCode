from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Prize
from .models import Event, UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import EventSearchForm


def home(request):
    return render(request, template_name='home2.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def upload_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to event list page
    else:
        form = EventForm()
    return render(request, 'upload.html', {'form': form})

def prize_list(request):
    prizes = Prize.objects.all()
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return render(request, 'prize_list.html', {'prizes': prizes, 'userprofile': user_profile})

def about_us(request):
    return render(request, 'about_us.html')

def home(request):
    form = EventSearchForm(request.GET)
    events = Event.objects.all()
    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        events = events.filter(event_name__icontains=query)

    return render(request, 'home2.html', {'events': events})

def event_display(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, pk=event_id)
        # Now you have access to the 'event' object in your view
        return render(request, 'event.html', {'event': event})
    else:
        # Handle GET request (if needed)
        pass
    



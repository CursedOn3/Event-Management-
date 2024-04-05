from datetime import datetime

# import Nominatim as Nominatim
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact, UserProfile
from django.contrib import messages

from .Models.Events import Event
from .Models.Events_customer_ref import EventCustomerRef
from .forms import SignUpForm, LoginForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated
from django.contrib.auth.models import User
from django_seed import Seed
import random
from faker import Faker

# Create your views here.

def get_current_user(request):
    return request.user

def index(request):
    user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    return render(request, 'index.html',{"user_profile": user_profile})

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def profile(request):
    user_profile_form = UserProfileForm()
    if not request.user.is_authenticated:
        return redirect('login')

    user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    user = request.user
    if request.method == 'POST':
        if request.POST["first_name"]:
            user.first_name = request.POST["first_name"]
        if request.POST["last_name"]:
            user.last_name = request.POST["last_name"]
        o_password = request.POST["o_password"]
        n_password = request.POST["password"]
        if o_password and check_password(o_password, user.password):
            user.set_password(n_password)
            user.save()
        user.save()
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_profile_form.is_valid():
            user_profile_form.save()
            update_session_auth_hash(request, user)
        else:
            print(user_profile_form.errors)

    return render(request,'profile.html', {"user_profile_form":user_profile_form, "user":request.user,"up":user_profile})

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

    return render(request,'contactus.html')

#registration view
@user_not_authenticated
def register(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "New Account Created {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = SignUpForm()

    return render(
        request=request,
        template_name = "register.html",
        context={"form": form}
    )


#Login View
@user_not_authenticated
def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect("home")

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = LoginForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )

#Logout View
@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')


def add_event(request):
    if request.method == "GET":
        return render(request, 'events_add.html')

    if request.method == "POST":
        name = request.POST.get('name')
        venue = request.POST.get('venue')
        ticket_price = request.POST.get('ticket_price')
        event_date = request.POST.get('event_date')
        booked = request.POST.get('booked', False)  # Default value is False if not provided

        # Create Event object and save it to the database
        event = Event.objects.create(
            name=name,
            venue=venue,
            ticket_price=ticket_price,
            event_date=event_date,
            booked=booked
        )

        if event.id > 0:
            messages.success(request, "event was added succesfully")
        else:
            messages.error(request, "event was not added. try again")
        return redirect('list_events')


def list_event(request):
    if request.method == "GET":
        events = Event.objects.all()
        return render(request, 'events.html', {"events":events})

    if request.method == "POST":
        pass


def list_my_events(request):
    if get_current_user(request).is_authenticated:
        # Filter EventCustomerRef instances by customer_id (current user)
        user_event_refs = EventCustomerRef.objects.filter(customer_id=get_current_user(request))

        # Extract event IDs associated with the user
        event_ids = user_event_refs.values_list('event_id', flat=True)

        # Retrieve events associated with the filtered event IDs
        user_events = Event.objects.filter(pk__in=event_ids)
        return render(request, 'my-events.html', {"events":user_events})
    else:
        return redirect('login')


def view_my_event(request, e_id):
    event = Event.objects.get(id=e_id)
    return render(request, 'event_detail.html', {"event": event})


def book_events(request):
    if request.method == "GET":
        user = request.user
        event_id = request.GET["e_id"]
        # ref = EventCustomerRef.objects.create(
        #     customer_id=user, event_id = Event.objects.get(id=event_id)
        # )
        if request.user.is_authenticated:
            # Create a relationship between the user and the event
            ref = EventCustomerRef.objects.create(customer_id=request.user,
                                                                 event_id=Event.objects.get(id=event_id))
            # You can perform additional operations here if needed
            if ref.id > 0:
                messages.success(request, "event booked !!!")
                return redirect('list_events')
        else:
            return redirect('login')


def seed_data(request):
    fake = Faker()

    def generate_events(total):
        seeder = Seed.seeder()
        seeder.add_entity(Event, total, {
            'name': lambda x: fake.name(),
            'venue': lambda x: fake.address(),
            'ticket_price': lambda x: random.uniform(10, 100),
            'event_date': lambda x: fake.date_this_year(),
            'booked': False,
        })
        seeder.execute()
    generate_events(10)

#
# def get_geocode():
#
#     def convert_coordinates_to_address(latitude, longitude):
#         # Initialize Nominatim geocoder
#         geolocator = Nominatim(user_agent="geoapiExercises")
#
#         # Concatenate latitude and longitude into a single string
#         coordinates = f"{latitude}, {longitude}"
#
#         try:
#             # Get the address using reverse geocoding
#             location = geolocator.reverse(coordinates)
#             return location.address
#         except Exception as e:
#             return str(e)
#
#     # Example usage
#     latitude = 37.7749  # Example latitude
#     longitude = -122.4194  # Example longitude
#
#     address = convert_coordinates_to_address(latitude, longitude)
#     print("Address:", address)


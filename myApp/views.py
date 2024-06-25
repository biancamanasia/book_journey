from django.shortcuts import render
from django.core.paginator import Paginator
from account.models import Account
from accommodation.models import Accommodation, AccommodationImage
from django.template.defaulttags import register
from accommodation.forms import AccommodationForm, AccommodationImageFormSet
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404


@register.filter
def get_range(value):
    return range(value)

def home_screen_view(request):
    location = request.GET.get('location')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    num_rooms = request.GET.get('num_rooms')
    accommodations = Accommodation.objects.all()

    if location:
        accommodations = accommodations.filter(Q(city__icontains=location) | Q(country__icontains=location))
    if start_date and end_date:
        accommodations = accommodations.filter(availability_start__lte=start_date, availability_end__gte=end_date)
    if num_rooms:
        accommodations = accommodations.filter(Q(rooms__gte=num_rooms) | Q(apartments__gte=num_rooms))
    
    paginator = Paginator(accommodations, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    accommodations_with_images = []

    for accommodation in page_obj:
        images = AccommodationImage.objects.filter(accommodation=accommodation)
        accommodations_with_images.append({
            'accommodation': accommodation,
            'images': images
        })

    context = {
        "accommodations_with_images": accommodations_with_images,
        "accommodations": page_obj,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "num_rooms": num_rooms,
        
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "myApp/home.html", context) 

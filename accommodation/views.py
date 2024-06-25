from django.shortcuts import render, redirect, get_object_or_404
from .models import Accommodation, Room, Apartment, Reservation, Review, RoomImage, ApartmentImage
from .forms import AccommodationForm, AccommodationImageFormSet, RoomFormSet, ApartmentFormSet, RoomForm, ApartmentForm, ReservationForm, ReviewForm, RoomImageFormSet, ApartmentImageFormSet
from django.forms import inlineformset_factory
from django.contrib import messages
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.forms import formset_factory

RoomFormSet = formset_factory(RoomForm, extra=1)
ApartmentFormSet = formset_factory(ApartmentForm, extra=1)

@register.filter
def get_range(value):
    return range(value)


def upload_accommodation_view(request):
    if request.method == 'POST':
        form = AccommodationForm(request.POST, request.FILES)
        accommodation_image_formset = AccommodationImageFormSet(request.POST, request.FILES, prefix='accommodation_images')
        room_formset = RoomFormSet(request.POST, prefix='rooms')
        room_image_formset = RoomImageFormSet(request.POST, request.FILES, prefix='room_images')
        apartment_formset = ApartmentFormSet(request.POST, prefix='apartments')
        apartment_image_formset = ApartmentImageFormSet(request.POST, request.FILES, prefix='apartment_images')

        if form.is_valid() and accommodation_image_formset.is_valid() and room_formset.is_valid() and room_image_formset.is_valid() and apartment_formset.is_valid() and apartment_image_formset.is_valid():
            accommodation = form.save()
            
            images = accommodation_image_formset.save(commit=False)
            for image in images:
                image.accommodation = accommodation
                image.save()

            for room_form in room_formset:
                if room_form.cleaned_data:
                    room = room_form.save(commit=False)
                    room.accommodation = accommodation
                    room.save()

            room_images = room_image_formset.save(commit=False)
            for image in room_images:
                image.room = room
                image.save()

            for apartment_form in apartment_formset:
                if apartment_form.cleaned_data:
                    apartment = apartment_form.save(commit=False)
                    apartment.accommodation = accommodation
                    apartment.save()


            apartment_images = apartment_image_formset.save(commit=False)
            for image in apartment_images:
                image.apartment = apartment
                image.save()

        

            return redirect('upload_accommodation_success')
    else:
        form = AccommodationForm()
        accommodation_image_formset = AccommodationImageFormSet(prefix='accommodation_images')
        room_formset = RoomFormSet(prefix='rooms')
        room_image_formset = RoomImageFormSet(prefix='room_images')
        apartment_formset = ApartmentFormSet(prefix='apartments')
        apartment_image_formset = ApartmentImageFormSet(prefix='apartment_images')

    context = {
        'form': form,
        'accommodation_image_formset': accommodation_image_formset,
        'room_formset': room_formset,
        'room_image_formset': room_image_formset,
        'apartment_formset': apartment_formset,
        'apartment_image_formset': apartment_image_formset,
    }
    return render(request, 'accommodation/upload_accommodation.html', context)



def upload_accommodation_success_view(request):
    return render(request, 'accommodation/upload_accommodation_success.html')

def accommodation_detail_view(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, id=accommodation_id)
    rooms = accommodation.rooms.all()
    apartments = accommodation.apartments.all()
    reviews = accommodation.reviews.all()
    accommodation_images = accommodation.images.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to submit a review.')
            return redirect('login')

        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.accommodation = accommodation
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('accommodation_detail_id', accommodation_id=accommodation.id)
    else:
        review_form = ReviewForm()

    context = {
        'accommodation': accommodation,
        'rooms': rooms,
        'apartments': apartments,
        'reviews': reviews,
        'review_form': review_form,
        'accommodation_images': accommodation_images,
    }
    return render(request, 'accommodation/accommodation_detail.html', context)

@login_required
def add_review(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, id=accommodation_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.accommodation = accommodation
            review.save()
            return redirect('accommodation_detail', accommodation_id=accommodation.id)
    else:
        form = ReviewForm()
    return render(request, 'accommodation/add_review.html', {'form': form, 'accommodation': accommodation})

def reservation_view(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, id=accommodation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.accommodation = accommodation
            reservation.save()
            return redirect('reservation_success') 
    else:
        form = ReservationForm()
    return render(request, 'accommodation/reserve_accommodation.html', {'form': form, 'accommodation': accommodation})

def reservation_success_view(request):
    return render(request, 'accommodation/reservation_success.html')

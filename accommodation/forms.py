from django import forms
from accommodation.models import Accommodation, AccommodationImage, Room, Apartment, RoomImage, ApartmentImage, COUNTRY_CITY_CHOICES, Reservation, Review
from tempus_dominus.widgets import DatePicker
from django.forms import inlineformset_factory
from django.core.validators import EmailValidator
from django.forms import modelformset_factory




class AccommodationForm(forms.ModelForm):

    availability_start = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))
    availability_end = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))

    country = forms.ChoiceField(choices=[('', 'Select country')] + [(country, country) for country in COUNTRY_CITY_CHOICES.keys()])
    
    initial_country = list(COUNTRY_CITY_CHOICES.keys())[0]
    city = forms.CharField(widget=forms.TextInput(attrs={'list': 'city-list'}))  
    
    number_of_rooms = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])
    number_of_apartments = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])
    
    class Meta:
        model = Accommodation
        fields = ['name', 'description', 'star_rating','country', 'city','availability_start', 'availability_end', 'number_of_rooms', 'number_of_apartments', 'parking', 'breakfast', 'internet', 'accessibility', 'bar', 'restaurant', 'fitness_center', 'pets', 'outdoor_activities', 'reception']
    class Media:
        js = ('js/country_city_dropdown.js',)

class AccommodationImageForm(forms.ModelForm):
    class Meta:
        model = AccommodationImage
        fields = ['image']



class RoomForm(forms.ModelForm):
    availability_start = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))
    availability_end = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))

    room_type = forms.ChoiceField(choices=[('', 'Select room type')] + [('economic', 'Economic'), ('standard', 'Standard'), ('superior', 'Superior')])
    currency = forms.ChoiceField(choices=[('', 'Select currency')] + Accommodation.CURRENCY_CHOICES)

    class Meta:
        model = Room
        fields = ['room_type', 'price', 'currency', 'availability_start', 'availability_end']

class RoomImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = ['image']


class ApartmentForm(forms.ModelForm):
    availability_start = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))
    availability_end = forms.DateField(widget=forms.TextInput(attrs={'class': 'flatpickr'}))


    currency = forms.ChoiceField(choices=[('', 'Select currency')] + Accommodation.CURRENCY_CHOICES)

    class Meta:
        model = Apartment
        fields = ['number_of_rooms', 'price', 'currency', 'availability_start', 'availability_end']

class ApartmentImageForm(forms.ModelForm):
    class Meta:
        model = ApartmentImage
        fields = ['image']

class ReservationForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Enter a valid email address")],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'phone_number', 'check_in', 'check_out', 'number_of_rooms', 'number_of_apartments']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number_of_rooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of rooms'}),
            'number_of_apartments': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of apartments'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


AccommodationImageFormSet = inlineformset_factory(Accommodation, AccommodationImage, form=AccommodationImageForm, extra=3, can_delete=True)
RoomFormSet = inlineformset_factory(Accommodation, Room, form=RoomForm, extra=0, can_delete=True)
RoomImageFormSet = inlineformset_factory(Room, RoomImage, form=RoomImageForm, extra=3, can_delete=True)
ApartmentFormSet = inlineformset_factory(Accommodation, Apartment, form=ApartmentForm, extra=0, can_delete=True)
ApartmentImageFormSet = inlineformset_factory(Apartment, ApartmentImage, form=ApartmentImageForm, extra=3, can_delete=True)


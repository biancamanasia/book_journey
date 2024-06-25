from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def accommodation_image_upload_path(instance, filename):
    return f'accommodation_images/accommodation_{instance.accommodation.id}/{filename}'

def room_image_upload_path(instance, filename):
    return f'accommodation_images/accommodation_{instance.room.accommodation.id}/rooms/{instance.room.id}/{filename}'

def apartment_image_upload_path(instance, filename):
    return f'accommodation_images/accommodation_{instance.apartment.accommodation.id}/apartments/{instance.apartment.id}/{filename}'

COUNTRY_CITY_CHOICES = {
    'Romania': ['București', 'Cluj-Napoca', 'Timișoara', 'Iași', 'Constanța', 'Craiova', 'Brașov', 'Galați', 'Ploiești', 'Oradea', 'Brăila', 'Arad', 'Pitești', 'Sibiu', 'Bacău', 'Târgu Mureș', 'Baia Mare', 'Buzău', 'Botoșani', 'Satu Mare', 'Râmnicu Vâlcea', 'Târgu Jiu'],
    'Bulgaria': ["Sofia", "Plovdiv", "Varna", "Burgas"],
    'Cyprus': ["Nicosia", "Limassol", "Larnaca", "Paphos"],
    'Egypt': ["Cairo", "Alexandria", "Giza", "Luxor"],
    'Finland': ["Helsinki", "Espoo", "Tampere", "Oulu"],
    'Greece': ["Athens", "Thessaloniki", "Patras", "Heraklion"],
    'Italy': ["Rome", "Milan", "Naples", "Turin"],
    'Kenya': ["Nairobi", "Mombasa", "Kisumu", "Nakuru"],
    'Maldives': ["Malé", "Hulhumalé", "Fuvahmulah", "Addu City"],
    'Mauritius': ["Port Louis", "Beau Bassin-Rose Hill", "Vacoas-Phoenix", "Curepipe"],
    'Morocco': ["Casablanca", "Marrakesh", "Rabat", "Fes"],
    'Portugal': ["Lisbon", "Porto", "Braga", "Faro"],
    'Seychelles': ["Victoria", "Anse Boileau", "Beau Vallon", "Takamaka"],
    'Spain': ["Madrid", "Barcelona", "Valencia", "Seville"],
    'Switzerland': ["Zurich", "Geneva", "Basel", "Lausanne"],
    'Tunisia': ["Tunis", "Sfax", "Sousse", "Kairouan"],
    'Turkey': ["Istanbul", "Ankara", "Izmir", "Bursa"],
    'United Arab Emirates': ["Dubai", "Abu Dhabi", "Sharjah", "Al Ain"]
}

STAR_RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

COUNTRY_CHOICES = [(country, country) for country in COUNTRY_CITY_CHOICES.keys()]

class Accommodation(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RON', 'RON'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    star_rating = models.IntegerField(choices=STAR_RATING_CHOICES, default=3)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default='Romania')    
    city = models.CharField(max_length=100, default='București')
    availability_start = models.DateField(null=True, blank=True)
    availability_end = models.DateField(null=True, blank=True)
    number_of_rooms = models.IntegerField()
    number_of_apartments = models.IntegerField()
    parking = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    accessibility = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    fitness_center = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    outdoor_activities = models.BooleanField(default=False)
    reception = models.BooleanField(default=False)
    


    def __str__(self):
        return self.name
    
    @property
    def facilities(self):
        facilities_list = []
        if self.parking:
            facilities_list.append('Parking')
        if self.breakfast:
            facilities_list.append('Breakfast Included')
        if self.internet:
            facilities_list.append('Internet')
        if self.accessibility:
            facilities_list.append('Accessible')
        if self.bar:
            facilities_list.append('Bar')
        if self.restaurant:
            facilities_list.append('Restaurant')
        if self.fitness_center:
            facilities_list.append('Gym')
        if self.pets:
            facilities_list.append('Pets Allowed')
        if self.outdoor_activities:
            facilities_list.append('Outdoor Activities')
        if self.reception:
            facilities_list.append('Reception 24/7')
        return facilities_list



class AccommodationImage(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=accommodation_image_upload_path)
    
    def __str__(self):
        return f"Image for {self.accommodation.name}"

class Room(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=50, choices=[('economic', 'Economic'), ('standard', 'Standard'), ('superior', 'Superior')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Accommodation.CURRENCY_CHOICES)
    availability_start = models.DateField()
    availability_end = models.DateField()

    def __str__(self):
        return f"{self.room_type} Room in {self.accommodation.name}"

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image = models.ImageField(upload_to=room_image_upload_path)

    def __str__(self):
        return f"Image for {self.room.room_type} Room in {self.room.accommodation.name}"

class Apartment(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='apartments')
    number_of_rooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Accommodation.CURRENCY_CHOICES)
    availability_start = models.DateField()
    availability_end = models.DateField()

    def __str__(self):
        return f"{self.number_of_rooms}-Room Apartment in {self.accommodation.name}"

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_images')
    image = models.ImageField(upload_to=apartment_image_upload_path)

    def __str__(self):
        return f"Image for {self.apartment.number_of_rooms}-Room Apartment in {self.apartment.accommodation.name}"

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    number_of_rooms = models.PositiveIntegerField(default=1)
    number_of_apartments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Reservation for {self.first_name} {self.last_name} at {self.accommodation}"
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=STAR_RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.accommodation.name}"    
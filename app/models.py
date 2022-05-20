from django.db import models
import datetime

# Create your models here.
class checkin(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date_time=models.DateTimeField(auto_now_add=True)
    
class checkout(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date_time=models.DateTimeField(auto_now_add=True)

gender_choices = (
    ("male", "male"),
    ("female", "female"),
)

vehicle_type=(
    ("Twoheeler","Twowheeler"),
    ("FourWheeler","FourWheeler")
)
vehicle_name=(
    ('Bike','Bike'),
    ("MahindraThar","MahindraThar"),
    ("MahindraXUV700","MahindraXUV700"),
    ("Tata Nexon","Tata Nexon"),
    ("Hyundai Creta","Hyundai Creta"),
)

identification_type=(
    ("ADHAAR","ADHAAR"),
    ("PANCARD","PANCARD"),
    ("OTHER","OTHER"),
)

class registeremp(checkin):
    identification_type = models.CharField(max_length=100,choices=identification_type)
    identification = models.CharField(max_length=100,unique=True)
    gender = models.CharField(max_length=50, choices=gender_choices)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100,choices=vehicle_type)
    vehicle_name = models.CharField(max_length=100,choices=vehicle_name)

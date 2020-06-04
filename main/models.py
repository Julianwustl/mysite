from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import cities_light
class Department(models.Model):
    id = models.AutoField()
    kuerzel = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Marketdata(models.Model):
    project_id = models.AutoField(primary_key= True)
    business_CHOICES = (
        (0,'LRT'),
        (1,'Metro'),
        (2,'Monorail/ VAL'),
        (3,'Rail Hsp'),
        (4,'Rail ML/ Commuter'),
    )
    typ_of_business = models.IntegerField(choices= business_CHOICES, default=None)
    fy_award = models.DateField()
    oi_date = models.DateField()
    project_start_date = models.DateField()
    project_end_data = models.DateField()
    number_trains = models.IntegerField()
    number_cars_per_train = models.IntegerField()
    cars_per_project = models.IntegerField()
    Track_length = models.FloatField()
    number_of_stations = models.IntegerField()
    number_of_depots = models.IntegerField()
    realization_probability = models.FloatField() # Maybe change too something more fitting
    order_probability = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    oas_competion_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    oas_financial_attractivines = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    smo_Volume_EM_Real = models.FloatField()
    smo_Volume_EM = models.FloatField()
    total_project_Volume = models.FloatField()

    turnkey_projet_Name = models.CharField(max_length=200)
    turnkey_region_Choices = (
        (0,'North-America'),
        (1,'South-West-Europe'),
        (2,'North-East-Europa'),
        (3,'Latin-America'),
        (4,'Asis-Pacific'),
        (5,'China'),
        (6,'UK & Ireland'),
        (7,'Middle East & Africa'),

    )
    region = models.IntegerField(choices= turnkey_region_Choices, default=None)

    project_total_volume = models.DecimalField(max_digits=10,decimal_places= 4)

    money = models.IntegerField()
    cost_per_car = models.DecimalField(max_digits=10,decimal_places= 4)
    track_length = models.DecimalField(max_digits=10,decimal_places= 4)
    number_station = models.IntegerField()
    cost_station = models.DecimalField(max_digits=8,decimal_places= 4)
    cost_per_KM = models.DecimalField(max_digits=10,decimal_places= 4)
    country = models.TextField()
    project_end_date = models.DateTimeField()


    @staticmethod
    @property
    def name(self):
        if self.typ_of_business.choices[0] == 1 or 2:
            return self.smo_Volume_EM * 0.3
        else:
            return self.smo_Volume_EM * 0.4





    def __str__(self):
        return self.turnkey_projet_Name
# Create your models here.



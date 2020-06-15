from django.db import models
from django.db.models import F
from django_countries.fields import CountryField

#https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
class country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class city(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class department(models.Model):
    kuerzel = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class project(models.Model):
    listed_in_SAM = models.BooleanField(default=False,null=True)
    data_source = models.CharField(max_length=500,null=True)
    project_category = models.CharField(max_length=500,null=True)
    comment_region = models.CharField(max_length=500,null=True)
    winner_em = models.CharField(max_length=500,null=True)
    competitiveness = models.CharField(max_length=500,null=True)
    oas_competition_score = models.FloatField(null=True)
    oas_financial_attractiveness = models.FloatField(null=True)
    power = models.FloatField(null=True)
    news = models.CharField(max_length=500,null=True)
    name = models.CharField(max_length=500,null=True)
    REGION_CHOICES = (
        (0, 'North-East-Europe'),
        (1, 'South-West-Europe'),
        (2, 'Latin America'),
        (3, 'Asia-Pacific'),
        (4, 'Middle East & Africa'),
        (5, 'North America'),
        (6, 'China'),
        (7, 'UK & Ireland'),
    )
    #Map countries to regions, and cities to countries
    region = models.IntegerField(choices = REGION_CHOICES, default = None,null=True)
    country = CountryField(null=True)
    city = models.CharField(max_length=500,null=True)
    TYPE_OF_BUSINESS_CHOICES = (
        (0, 'LRT'),
        (1, 'Metro'),
        (2, 'Monorail/VAL'),
        (3, 'Rail HSP'),
        (4, 'Rail ML/Commuter'),
    )
    type_of_business = models.IntegerField(choices = TYPE_OF_BUSINESS_CHOICES, default = None,null=True)
    type_of_project = models.CharField(max_length=500,null=True)
    fy_of_award = models.FloatField(default=0.0,null=True)#models.DateField(null=True)
    oi_date = models.FloatField(default=0.0,null=True)#models.DateField(null=True)
    project_end_date = models.FloatField(default=0.0,null=True)#models.DateField(null=True)
    number_trains = models.PositiveIntegerField(default=0,null=True)
    number_cars_per_train = models.PositiveIntegerField(default=0,null=True)
    cost_per_car = models.FloatField(default=0.0,null=True)
    track_length = models.FloatField(default=0.0,null=True)
    number_station = models.PositiveIntegerField(default=0,null=True)
    number_depots = models.PositiveIntegerField(default=0,null=True)
    realization_probability = models.FloatField(null=True)
    order_probability = models.FloatField(null=True)
    total_project_volume = models.FloatField(null=True)
    source = models.CharField(max_length=500,null=True)
    no_stratigic_fit_not_mandated = models.BooleanField(default=False,null=True)
    no_bid_political_positioning = models.BooleanField(default=False,null=True)
    no_bid_consortium_incl_civil = models.BooleanField(default=False,null=True)
    no_bid_rolling_stock = models.BooleanField(default=False,null=True)
    no_bid_target_price = models.BooleanField(default=False,null=True)
    no_bid_risk_profile = models.BooleanField(default=False,null=True)
    comment_bid = models.CharField(max_length=1000,null=True)
    disqualified = models.BooleanField(default=False,null=True)
    lost = models.BooleanField(default=False,null=True)


    def __str__(self):
        return self.name

    #Metro and Monorail/VAL --> Total Project Volume * 0.3
    #LRT, Rail HSP, Rail Ml/Commuter --> Total Project Volume * 0.4
    @property
    def smo_volume(self):
        for i in self.TYPE_OF_BUSINESS_CHOICES:
            if i[0] == 1 or 2:
                return F(self.total_project_volume) * 0.3
            else:
                return F(self.total_project_volume) * 0.4

    @property
    def smo_volume_real(self):
        return F(self.smo_volume) * (F(self.realization_probability) / 100.0)

    @property
    def service_volume(self):
        return 0.5 * self.smo_volume

    @property
    def scope_siemens_TK(self):
        return self.smo_volume * 0.15



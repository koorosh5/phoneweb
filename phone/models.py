from django.db import models

class Phone(models.Model):
    brand_name = models.CharField(max_length=100, choices=[('samsung', 'Samsung'), ('apple', 'Apple'), ('xiaomi', 'Xiaomi')])
    brand_nationality = models.CharField(max_length=100, choices=[('korea', 'Korea'), ('usa', 'USA'), ('china', 'China')])
    model = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.FloatField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    country_of_manufacture = models.CharField(max_length=100, choices=[('korea', 'Korea'), ('china', 'China'), ('usa', 'USA')])

    def __str__(self):
        return self.model
    
class PhoneSearch(models.Model):
    brand_name = models.CharField(max_length=100, choices=[('samsung', 'Samsung'), ('apple', 'Apple'), ('xiaomi', 'Xiaomi')], blank=True, null=True)
    brand_nationality = models.CharField(max_length=100, choices=[('korea', 'Korea'), ('usa', 'USA'), ('china', 'China')], blank=True, null=True)
    model = models.CharField(max_length=100, unique=True, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    screen_size = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], blank=True, null=True)
    country_of_manufacture = models.CharField(max_length=100, choices=[('korea', 'Korea'), ('china', 'China'), ('usa', 'USA')], blank=True, null=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.model if self.model else ''

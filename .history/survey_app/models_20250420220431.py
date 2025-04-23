from django.db import models

# Create your models here.
from django.db import models

class Survey(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    telephone_number = models.CharField(max_length=15, blank=True)
    liked_most = models.CharField(max_length=100, blank=True)
    interest_source = models.CharField(max_length=100, blank=True)
    recommendation = models.CharField(max_length=100, blank=True)
    date_of_survey = models.DateField(auto_now_add=True)

    def __str__(self):
        return f\"{self.first_name} {self.last_name}\"

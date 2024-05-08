from django.db import models
from django.urls import reverse

TIME = (
    ('D', 'Day-time only, 7 AM - 3 PM'),
    ('N', 'Night-time only, 3 PM - 11 PM'),
    ('A', 'All-day, 7 AM - 11 PM')
)

class Option(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('options_detail', kwargs={'pk': self.id})

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    msrp = models.CharField(max_length=100)
    horsepower = models.CharField(max_length=100)
    madein = models.CharField(max_length=100, default='Unknown ')
    image = models.TextField(max_length=300, default='Copy Image URL')
    # Manu:Many relationship
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    
class Rental(models.Model):
    date = models.DateField('Available Rental Date')
    rental = models.CharField(
        max_length=1,
        choices=TIME,
        default=TIME[0][0],
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.get_rental_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'
    

class Participant(models.Model):
    email = models.EmailField(unique=True)
    # meetups = models.ManyToManyField(unique=True)
    def __str__(self):
        return self.email


# create a blueprint here and this class crete  the database 
class Meetup(models.Model):
    titele = models.CharField(max_length=200) #--> there is a tittel 
    organizer_email = models.EmailField()
    date =models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    Location = models.ForeignKey(Location , on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant , blank=True , null=True)



    def __str__(self):
        return f'{self.titele} - {self.slug}'

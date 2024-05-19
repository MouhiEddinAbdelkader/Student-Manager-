from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Poste(models.Model):
    image = models.ImageField( blank=True)
    # 'type' is a reserved keyword, let's use another name like 'post_type'
    # You can use choices to specify the options for the type field
    POST_TYPE_CHOICES = (
        (0, 'Offre'),
        (1, 'Demande'),
    )
    post_type = models.IntegerField(choices=POST_TYPE_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    no_of_likes = models.IntegerField(default=0)

class Recommandation(Poste):  # Inheriting from Poste
    recom = models.TextField() 
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# class Transport(Poste):
#     depart = models.TextField()
#     destination = models.TextField()
#     heureDep = models.DateTimeField()
    
class Logement(Poste):
    localisation = models.TextField()
    description = models.TextField()
    contactInfo = models.TextField()

class Stage(Poste):
    STAGE_TYPE_CHOICES = (
        (0, 'ouvrier'),
        (1, 'technicien'),
        (1, 'PFE'),
    )
    typeStage = models.IntegerField(choices=STAGE_TYPE_CHOICES)
    societe = models.TextField()
    duree = models.IntegerField()
    sujet = models.TextField()
    contactInfo = models.TextField()
    specialité = models.TextField()

class Evenement(Poste):
    intitulé = models.TextField()
    description = models.TextField()  
    lieu = models.TextField()
    contactInfo = models.TextField()
    
class EvenSocial(Evenement):
    prix = models.FloatField((""))

class EvenClub(Evenement):
    club = models.TextField()
    

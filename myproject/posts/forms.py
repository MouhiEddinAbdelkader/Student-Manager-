from django import forms 
from . import models 



        
class StageForm(forms.ModelForm):
    class Meta:
        model = models.Stage
        fields = ['image', 'post_type', 'date', 'author','typeStage', 'duree'  , 'societe', 'sujet', 'contactInfo', 'specialité'  ]  # List only the fields you want to display

class CreateLogment(forms.ModelForm):
    class Meta:
        model = models.Logement
        fields = '__all__'
        
class CreateEvenClub(forms.ModelForm):
    class Meta:
        model = models.EvenClub
        fields = ['image', 'post_type', 'author','intitulé', 'description', 'lieu', 'contactInfo', 'club'  ]  # List only the fields you want to display


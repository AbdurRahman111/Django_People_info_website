from django.forms import ModelForm
from .models import person_information



class add_person_info(ModelForm):
    class Meta:
        model = person_information
        fields = ['First_name', 'Last_name', 'Other_name', 'State_of_Origin', 'Sex', 'Spoken_languages', 'Complexion', 'image', 'Description']

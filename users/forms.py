from django.forms import ModelForm
from .models import UserProfile
class UserRegistration(ModelForm):

    class Meta:
        model= UserProfile
        fields= ('__all__')
        exclude= ['user']
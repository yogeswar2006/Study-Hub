from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude = ['host','participants']
        
        
class CustomUserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email']     
        
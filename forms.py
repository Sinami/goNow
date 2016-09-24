from django import forms
from .models import UserProfile, Trip

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'age', 'city', 'state',)

class TripSearchForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('trip_location','trip_start_date','trip_end_date',)
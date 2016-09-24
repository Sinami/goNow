from django import forms
from .models import UserProfile, Trip

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'age', 'city', 'state',)

class TripSearchForm(forms.Form):
    trip_location = forms.CharField(label='Where..',max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Where..'})),
    trip_start_date = forms.DateField(label='When..',widget=forms.TextInput(attrs={'placeholder': 'Search'})),
    #trip_end_date = forms.DateField()
    trip_budget = forms.IntegerField(label='Budget..')
    distance_from_you = forms.IntegerField(label='Area Range..')
    #class Meta:
    #    model = Trip
    #   fields = ('trip_location','trip_start_date','trip_end_date',)
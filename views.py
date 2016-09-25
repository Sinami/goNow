from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

from .forms import TripSearchForm, UserInfoForm
from .models import UserProfile, Trip


def index(request):
	if request.method == "POST":
		if request.POST:
			form = TripSearchForm(request.POST)
			if form.is_valid():
				trip_location = form.cleaned_data['trip_location']
				trip_start_date = form.cleaned_data['trip_start_date']
				trip_budget = form.cleaned_data['trip_budget']
				distance_from_you = form.cleaned_data['distance_from_you']
				TripSearchForm.objects.filter()
				return redirect('goNow:submitSearch')
	return render(request, 'goNow/home.html', {'form':form,})

def submitSearch(request,):
	post = get_object_or_404(Trip, pk=pk)
	return render(request, 'goNow/results.html', {'post':post})

def query_testing(self):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM 'goNow_trip' where id=%s", [self.id])
    row = cursor.fetchall()
    return row


##### OLD CODE MIGHT NEED ##################
	# elif 'delete' in request.POST:
	# 	searchStr = GroupInfoDeleteForm(request.POST)
	# 	if searchStr.is_valid():
	# 		#logger.error(searchStr)
	# 		l_name = searchStr.cleaned_data['last_name']
	# 		g_name = searchStr.cleaned_data['group_name']
	# 		GroupInfo.objects.filter(last_name=l_name).filter(group_name=g_name).delete()
	# 		return redirect('groupTracker:delete')
	# elif 'find' in request.POST:
	# 	searchStr = GroupInfoFindForm(request.POST)
	# 	if searchStr.is_valid():
	# 		c_name = searchStr.cleaned_data['class_name']
	# 		records = GroupInfo.objects.filter(class_name=c_name)
	# 		return redirect('groupTracker:details', records)
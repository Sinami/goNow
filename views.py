from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

from .forms import TripSearchForm, UserInfoForm, SubscribeForm
from .models import UserProfile, Trip, Subscribe


def index(request):
	#group = GroupInfo.objects.order_by('id')[:5]
	#context = {'group': group}
	#return render(request, 'groupTracker/index.html', context)
	if request.method == "POST":
		if 'submitSearch' in request.POST:
			form = TripSearchForm(request.POST)
			if form.is_valid():
				trip_location = form.cleaned_data['trip_location']
				trip_start_date = form.cleaned_data['trip_start_date']
				trip_budget = form.cleaned_data['trip_budget']
				distance_from_you = form.cleaned_data['distance_from_you']
				return redirect('goNow:submitSearch')
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
		elif 'subscribe' in request.POST:
			#data = {'name':
			#}
			
			return render(request, 'goNow/subscribe.html',)
	else:
		form = TripSearchForm()
		return render(request, 'goNow/home.html', {'form':form,})

def submitSearch(request,):
	post = get_object_or_404(Trip, pk=pk)
	return render(request, 'goNow/results.html', {'post':post})

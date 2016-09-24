from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)

from .forms import TripSearchForm, UserInfoForm
from .models import UserProfile, Trip


def index(request):
	#group = GroupInfo.objects.order_by('id')[:5]
	#context = {'group': group}
	#return render(request, 'groupTracker/index.html', context)
	if request.method == "POST":
		if 'submit' in request.POST:
			form = TripSearchForm(request.POST)
			if form.is_valid():
				post = form.save()
				return redirect('goNow:submitSearch',pk=post.pk)
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
	else:
		form = TripSearchForm()
	return render(request, 'groupTracker/index.html', {'form':form,})

def submitSearch(request, pk):
	post = get_object_or_404(Trip, pk=pk)
	return render(request, 'goNow/results.html', {'post':post})
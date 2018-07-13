from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path

#from horizon.models import get_user_timeline

import requests

def users(request,name):
	print(name)

	# Start and end to pass to API
	start = request.GET.get('start', 0)
	end = request.GET.get('end', 9)
	#results = get_user_timeline(name)

	# Call my twitter API (flask)
	response = requests.get('http://127.0.0.1:5000/users/' + name + '?count=100&start=' + str(start) + '&end=' + str(end))
	
	results = response.json()

	num_tweets = 100
	num_page = 10
	page = 1
	buttons = []
	# Make buttons for pagination
	for start in range(0,num_tweets,num_page):
		button = {
			"start": start,
			"end": start+num_page,
			"page": page
		}
		buttons.append(button)
		page += 1

	# buttons = [
	# 	{
	# 		'start':0,
	# 		'end':10,
	# 		'page':1
	# 	},
	# 	{
	# 		'start':10,
	# 		'end':20,
	# 		'page':2
	# 	}
	# ]

	# for tweet in results:
	# 	tweet['hashtags'] = [{'text':'one'},{'text':'two'},{'text':'three'},{'text':'four'}]

	# for tweet in results:
	# 		tweet['hashtags'] = tweet['hashtags'][:2]

	context = {
		"tweets": results,
		"start": start,
		"end": end,
		"buttons": buttons,
		"name": name,
		"mode": "user"

	}
	return render(request, 'horizon/index.html', context)


def hashtags(request,name):
	print(name)
	start = request.GET.get('start', 0)
	end = request.GET.get('end', 9)
	#results = get_user_timeline(name)

	# Call API
	response = requests.get('http://127.0.0.1:5000/hashtags/' + name + '?count=100&start=' + str(start) + '&end=' + str(end))
	
	results = response.json()

	num_tweets = 100
	num_page = 10
	page = 1
	buttons = []
	# Make buttons for pagination
	for start in range(0,num_tweets,num_page):
		button = {
			"start": start,
			"end": start+num_page,
			"page": page
		}
		buttons.append(button)
		page += 1

	context = {
		"tweets": results,
		"start": start,
		"end": end,
		"buttons": buttons,
		"name": name,
		"mode": "hashtag"

	}
	return render(request, 'horizon/index.html', context)


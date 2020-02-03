import requests

from django.shortcuts import render
from django.conf import settings

def index (request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part' : 'snippet',
        'q' : 'learn python',
        'key' : settings.YOUTUBE_DATA_API_KEY
    }

    r=requests.get(search_url,params=params)
    print(r.text)
    return render(request,  'search/index.html')

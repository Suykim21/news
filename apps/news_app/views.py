from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User
import requests
from datetime import datetime
import random


def index(request):
  print "*"*50
  images = []
  titles = []
  descriptions = []
  urls = []
  pub = []

  # Huffington Post API call
  responseH = requests.get('https://newsapi.org/v1/articles?source=the-huffington-post&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataH = responseH.json()
  Huff = dataH[u'articles']
  random.shuffle(Huff)

  #Entertainment Weekly API
  responseE = requests.get('https://newsapi.org/v1/articles?source=entertainment-weekly&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataE = responseE.json()
  EW = dataE[u'articles']
  random.shuffle(EW)

  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataT = responseT.json()
  Crunch = dataT[u'articles']
  random.shuffle(Crunch)

  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataF = responseF.json()
  Fox = dataF[u'articles']
  random.shuffle(Fox)

  #Brietbar API
  responseB = requests.get('https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataB = responseB.json()
  Brietbar = dataB[u'articles']
  random.shuffle(Brietbar)

  #MTV News API
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataM = responseM.json()
  MTV = dataM[u'articles']
  random.shuffle(MTV)

  #Recode API
  responseR = requests.get('https://newsapi.org/v1/articles?source=recode&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataR = responseR.json()
  Recode = dataR[u'articles']
  random.shuffle(Recode)

  #Sports Bible API
  responseS = requests.get('https://newsapi.org/v1/articles?source=the-sport-bible&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataS = responseS.json()
  sportsBible = dataS[u'articles']
  random.shuffle(sportsBible)

  context = {
    'sportsBible': sportsBible,
    'Recode': Recode,
    'MTV': MTV,
    'Briet': Brietbar,
    'Fox': Fox,
    'Crunch': Crunch,
    'EW': EW,
    'Huff': Huff,
  }
  return render(request, 'news_app/index.html', context)

def subscribe(request):
  User.objects.create(name=request.POST['name'], email=request.POST['email'])
  return redirect('home')

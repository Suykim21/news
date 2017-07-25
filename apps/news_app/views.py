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
  #Delete below
  a = len(dataH)
  b = random.randint(0,a)
  print (dataH)
  images.append(dataH[u'articles'][b][u'urlToImage'])
  titles.append(dataH[u'articles'][b][u'title'])
  descriptions.append(dataH[u'articles'][b][u'description'])
  urls.append(dataH[u'articles'][b][u'url'])
  pub.append(dataH[u'articles'][b][u'publishedAt'].split('T')[0])

  #Entertainment Weekly API
  responseE = requests.get('https://newsapi.org/v1/articles?source=entertainment-weekly&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataE = responseE.json()
  EW = dataE[u'articles']
  random.shuffle(EW)
  #Delete below
  a = len(dataE)
  b = random.randint(0,a)
  images.append(dataE[u'articles'][b][u'urlToImage'])
  titles.append(dataE[u'articles'][b][u'title'])
  descriptions.append(dataE[u'articles'][b][u'description'])
  urls.append(dataE[u'articles'][b][u'url'])
  pub.append(dataE[u'articles'][b][u'publishedAt'].split('T')[0])

  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataT = responseT.json()
  Crunch = dataT[u'articles']
  random.shuffle(Crunch)
  #Delete below
  a = len(dataT)
  b = random.randint(0,a)
  images.append(dataT[u'articles'][b][u'urlToImage'])
  titles.append(dataT[u'articles'][b][u'title'])
  descriptions.append(dataT[u'articles'][b][u'description'])
  urls.append(dataT[u'articles'][b][u'url'])
  pub.append(dataT[u'articles'][b][u'publishedAt'].split('T')[0])

  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataF = responseF.json()
  Fox = dataF[u'articles']
  random.shuffle(Fox)
  #Delete below
  a = len(dataF)
  b = random.randint(0,a)
  images.append(dataF[u'articles'][b][u'urlToImage'])
  titles.append(dataF[u'articles'][b][u'title'])
  descriptions.append(dataF[u'articles'][b][u'description'])
  urls.append(dataF[u'articles'][b][u'url'])
  pub.append(dataF[u'articles'][b][u'publishedAt'].split('T')[0])

  #Brietbar API
  responseB = requests.get('https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataB = responseB.json()
  Brietbar = dataB[u'articles']
  random.shuffle(Brietbar)
  #Delete below
  a = len(dataB)
  b = random.randint(0,a)
  images.append(dataB[u'articles'][b][u'urlToImage'])
  titles.append(dataB[u'articles'][b][u'title'])
  descriptions.append(dataB[u'articles'][b][u'description'])
  urls.append(dataB[u'articles'][b][u'url'])
  pub.append(dataB[u'articles'][b][u'publishedAt'].split('T')[0])

  #MTV News API
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataM = responseM.json()
  MTV = dataM[u'articles']
  random.shuffle(MTV)
  #Delete below
  a = len(dataM)
  b = random.randint(0,a)
  images.append(dataM[u'articles'][b][u'urlToImage'])
  titles.append(dataM[u'articles'][b][u'title'])
  descriptions.append(dataM[u'articles'][b][u'description'])
  urls.append(dataM[u'articles'][b][u'url'])
  pub.append(dataM[u'articles'][b][u'publishedAt'].split('T')[0])

  #Recode API
  responseR = requests.get('https://newsapi.org/v1/articles?source=recode&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataR = responseR.json()
  Recode = dataR[u'articles']
  random.shuffle(Recode)
  #Delete below
  a = len(dataR)
  b = random.randint(0,a)
  images.append(dataR[u'articles'][b][u'urlToImage'])
  titles.append(dataR[u'articles'][b][u'title'])
  descriptions.append(dataR[u'articles'][b][u'description'])
  urls.append(dataR[u'articles'][b][u'url'])
  pub.append(dataR[u'articles'][b][u'publishedAt'].split('T')[0])

  #Sports Bible API
  responseS = requests.get('https://newsapi.org/v1/articles?source=the-sport-bible&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  dataS = responseS.json()
  sportsBible = dataS[u'articles']
  random.shuffle(sportsBible)
  #Delete below
  a = len(dataS)
  b = random.randint(0,a)
  images.append(dataS[u'articles'][b][u'urlToImage'])
  titles.append(dataS[u'articles'][b][u'title'])
  descriptions.append(dataS[u'articles'][b][u'description'])
  urls.append(dataS[u'articles'][b][u'url'])
  pub.append(dataS[u'articles'][b][u'publishedAt'].split('T')[0])

  context = {
    'sportsBible': sportsBible,
    'Recode': Recode,
    'MTV': MTV,
    'Brietbar': Brietbar,
    'Fox': Fox,
    'Crunch': Crunch,
    'EW': EW,
    'Huff': Huff,
    #Delete below
    'images': images,
    'titles': titles,
    'descriptions': descriptions,
    'urls': urls,
    'pub': pub,
  }
  return render(request, 'news_app/index.html', context)

def subscribe(request):
  User.objects.create(name=request.POST['name'], email=request.POST['email'])
  return redirect('home')

from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
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
  #cached HuffPo data
  dataH = responseH.json()
  l = len(dataH)
  x = random.randint(0,l)
  images.append(dataH[u'articles'][x][u'urlToImage'])
  titles.append(dataH[u'articles'][x][u'title'])
  descriptions.append(dataH[u'articles'][x][u'description'])
  urls.append(dataH[u'articles'][x][u'url'])
  pub.append(dataH[u'articles'][x][u'publishedAt'])

  #Entertainment Weekly API
  responseE = requests.get('https://newsapi.org/v1/articles?source=entertainment-weekly&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached EW data
  dataE = responseE.json()
  l = len(dataE)
  x = random.randint(0,l)
  images.append(dataE[u'articles'][x][u'urlToImage'])
  titles.append(dataE[u'articles'][x][u'title'])
  descriptions.append(dataE[u'articles'][x][u'description'])
  urls.append(dataE[u'articles'][x][u'url'])
  pub.append(dataE[u'articles'][x][u'publishedAt'])

  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Tech Crunch data
  dataT = responseT.json()
  l = len(dataT)
  x = random.randint(0,l)
  images.append(dataT[u'articles'][x][u'urlToImage'])
  titles.append(dataT[u'articles'][x][u'title'])
  descriptions.append(dataT[u'articles'][x][u'description'])
  urls.append(dataT[u'articles'][x][u'url'])
  pub.append(dataT[u'articles'][x][u'publishedAt'])

  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Fox data
  dataF = responseF.json()
  l = len(dataF)
  x = random.randint(0,l)
  images.append(dataF[u'articles'][x][u'urlToImage'])
  titles.append(dataF[u'articles'][x][u'title'])
  descriptions.append(dataF[u'articles'][x][u'description'])
  urls.append(dataF[u'articles'][x][u'url'])
  pub.append(dataF[u'articles'][x][u'publishedAt'])

  #Brietbar API
  responseB = requests.get('https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Briet data
  dataB = responseB.json()
  l = len(dataB)
  x = random.randint(0,l)
  images.append(dataB[u'articles'][x][u'urlToImage'])
  titles.append(dataB[u'articles'][x][u'title'])
  descriptions.append(dataB[u'articles'][x][u'description'])
  urls.append(dataB[u'articles'][x][u'url'])
  pub.append(dataB[u'articles'][x][u'publishedAt'])

  #MTV News API
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached MTV data
  dataM = responseM.json()
  l = len(dataM)
  x = random.randint(0,l)
  images.append(dataM[u'articles'][x][u'urlToImage'])
  titles.append(dataM[u'articles'][x][u'title'])
  descriptions.append(dataM[u'articles'][x][u'description'])
  urls.append(dataM[u'articles'][x][u'url'])
  pub.append(dataM[u'articles'][x][u'publishedAt'])

  #Recode API
  responseR = requests.get('https://newsapi.org/v1/articles?source=recode&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Recode data
  dataR = responseR.json()
  l = len(dataR)
  x = random.randint(0,l)
  images.append(dataR[u'articles'][x][u'urlToImage'])
  titles.append(dataR[u'articles'][x][u'title'])
  descriptions.append(dataR[u'articles'][x][u'description'])
  urls.append(dataR[u'articles'][x][u'url'])
  pub.append(dataR[u'articles'][x][u'publishedAt'])

  #Sports Bible API
  responseS = requests.get('https://newsapi.org/v1/articles?source=the-sport-bible&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Sport Bible data
  dataS = responseS.json()
  l = len(dataS)
  x = random.randint(0,l)
  images.append(dataS[u'articles'][x][u'urlToImage'])
  titles.append(dataS[u'articles'][x][u'title'])
  descriptions.append(dataS[u'articles'][x][u'description'])
  urls.append(dataS[u'articles'][x][u'url'])
  pub.append(dataS[u'articles'][x][u'publishedAt'])
  context = {
    'images': images,
    'titles': titles,
    'descriptions': descriptions,
    'urls': urls,
    'pub': pub
  }
  return render(request, 'news_app/index.html', context)

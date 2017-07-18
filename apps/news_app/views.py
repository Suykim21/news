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
  a = len(dataH)
  b = random.randint(0,a)
  images.append(dataH[u'articles'][b][u'urlToImage'])
  titles.append(dataH[u'articles'][b][u'title'])
  descriptions.append(dataH[u'articles'][b][u'description'])
  urls.append(dataH[u'articles'][b][u'url'])
  pub.append(dataH[u'articles'][b][u'publishedAt'].split('T')[0])

  #Entertainment Weekly API
  responseE = requests.get('https://newsapi.org/v1/articles?source=entertainment-weekly&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached EW data
  dataE = responseE.json()
  c = len(dataE)
  d = random.randint(0,c)
  images.append(dataE[u'articles'][d][u'urlToImage'])
  titles.append(dataE[u'articles'][d][u'title'])
  descriptions.append(dataE[u'articles'][d][u'description'])
  urls.append(dataE[u'articles'][d][u'url'])
  pub.append(dataE[u'articles'][d][u'publishedAt'].split('T')[0])

  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Tech Crunch data
  dataT = responseT.json()
  e = len(dataT)
  print e
  f = random.randint(0,e)
  print f
  print dataT
  images.append(dataT[u'articles'][f][u'urlToImage'])
  titles.append(dataT[u'articles'][f][u'title'])
  descriptions.append(dataT[u'articles'][f][u'description'])
  urls.append(dataT[u'articles'][f][u'url'])
  pub.append(dataT[u'articles'][f][u'publishedAt'].split('T')[0])

  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Fox data
  dataF = responseF.json()
  g = len(dataF)
  h = random.randint(0,g)
  images.append(dataF[u'articles'][h][u'urlToImage'])
  titles.append(dataF[u'articles'][h][u'title'])
  descriptions.append(dataF[u'articles'][h][u'description'])
  urls.append(dataF[u'articles'][h][u'url'])
  pub.append(dataF[u'articles'][h][u'publishedAt'].split('T')[0])

  #Brietbar API
  responseB = requests.get('https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Briet data
  dataB = responseB.json()
  i = len(dataB)
  j = random.randint(0,i)
  images.append(dataB[u'articles'][j][u'urlToImage'])
  titles.append(dataB[u'articles'][j][u'title'])
  descriptions.append(dataB[u'articles'][j][u'description'])
  urls.append(dataB[u'articles'][j][u'url'])
  pub.append(dataB[u'articles'][j][u'publishedAt'].split('T')[0])

  #MTV News API
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached MTV data
  dataM = responseM.json()
  k = len(dataM)
  l = random.randint(0,k)
  images.append(dataM[u'articles'][l][u'urlToImage'])
  titles.append(dataM[u'articles'][l][u'title'])
  descriptions.append(dataM[u'articles'][l][u'description'])
  urls.append(dataM[u'articles'][l][u'url'])
  pub.append(dataM[u'articles'][l][u'publishedAt'].split('T')[0])

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
  pub.append(dataR[u'articles'][x][u'publishedAt'].split('T')[0])

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
  pub.append(dataS[u'articles'][x][u'publishedAt'].split('T')[0])
  context = {
    'images': images,
    'titles': titles,
    'descriptions': descriptions,
    'urls': urls,
    'pub': pub
  }
  return render(request, 'news_app/index.html', context)

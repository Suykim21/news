from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import requests


def index(request):
  print "*"*50
  images = []
  titles = []
  descriptions = []
  # Huffington Post API call
  responseH = requests.get('https://newsapi.org/v1/articles?source=the-huffington-post&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached HuffPo data
  dataH = responseH.json()
  print dataH
  images.append(dataH[u'articles'][0][u'urlToImage'])
  titles.append(dataH[u'articles'][0][u'title'])
  descriptions.append(dataH[u'articles'][0][u'description'])
  #Entertainment Weekly API
  responseE = requests.get('https://newsapi.org/v1/articles?source=entertainment-weekly&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached EW data
  dataE = responseE.json()
  images.append(dataE[u'articles'][0][u'urlToImage'])
  titles.append(dataE[u'articles'][0][u'title'])
  descriptions.append(dataE[u'articles'][0][u'description'])
  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Tech Crunch data
  dataT = responseT.json()
  images.append(dataT[u'articles'][0][u'urlToImage'])
  titles.append(dataT[u'articles'][0][u'title'])
  descriptions.append(dataT[u'articles'][0][u'description'])
  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539')
  #cached Fox data
  dataF = responseF.json()
  images.append(dataF[u'articles'][0][u'urlToImage'])
  titles.append(dataF[u'articles'][0][u'title'])
  descriptions.append(dataF[u'articles'][0][u'description'])
  context = {
    'images': images,
    'titles': titles,
    'descriptions': descriptions
  }
  return render(request, 'news_app/index.html', context)

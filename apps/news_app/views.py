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
  #Brietbar API
  responseB = requests.get('https://newsapi.org/v1/articles?source=breitbart-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached Briet data      
  dataB = responseB.json()
  images.append(dataB[u'articles'][0][u'urlToImage'])
  titles.append(dataB[u'articles'][0][u'title'])
  descriptions.append(dataB[u'articles'][0][u'description'])
  #MTV News API
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached MTV data      
  dataM = responseM.json()
  images.append(dataM[u'articles'][0][u'urlToImage'])
  titles.append(dataM[u'articles'][0][u'title'])
  descriptions.append(dataM[u'articles'][0][u'description'])
  #Recode API
  responseR = requests.get('https://newsapi.org/v1/articles?source=recode&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached Recode data      
  dataR = responseR.json()
  images.append(dataR[u'articles'][0][u'urlToImage'])
  titles.append(dataR[u'articles'][0][u'title'])
  descriptions.append(dataR[u'articles'][0][u'description'])
  #Sports Bible API
  responseS = requests.get('https://newsapi.org/v1/articles?source=the-sport-bible&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached Sport Bible data      
  dataS = responseS.json()
  images.append(dataS[u'articles'][0][u'urlToImage'])
  titles.append(dataS[u'articles'][0][u'title'])
  descriptions.append(dataS[u'articles'][0][u'description'])
  context = {
    'images': images,
    'titles': titles,
    'descriptions': descriptions
  }
  return render(request, 'news_app/index.html', context)

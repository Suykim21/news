from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import requests


def index(request):
  print "*"*50
  # Huffington Post API call
  responseH = requests.get('https://newsapi.org/v1/articles?source=the-huffington-post&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached HuffPo data
  dataH = responseH.json()
  car_one = dataH[u'articles'][0][u'urlToImage']
  #MTV News API call
  responseM = requests.get('https://newsapi.org/v1/articles?source=mtv-news&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached MTV data  
  dataM = responseM.json()
  car_two = dataM[u'articles'][0][u'urlToImage']
  #Tech Crunch API call
  responseT = requests.get('https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached Tech Crunch data
  dataT = responseT.json()
  car_three = dataT[u'articles'][0][u'urlToImage']
  #Fox Sports API call
  responseF = requests.get('https://newsapi.org/v1/articles?source=fox-sports&sortBy=top&apiKey=3b606a8547b24dfdbf43e72388b6f539') 
  #cached Fox data      
  dataF = responseF.json()
  car_four = dataF[u'articles'][0][u'urlToImage']  
  return render(request, 'news_app/index.html', {'car_one':car_one, 'car_two':car_two, 'car_three':car_three, 'car_four':car_four})

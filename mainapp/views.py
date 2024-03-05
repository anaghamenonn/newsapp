from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = "https://newsapi.org/v2/everything?q=wwe&from=2024-03-04&sortBy=popularity&apiKey=39d55bd6cbd14801b185de2c7f369ac6"
    
    
    cricket_news = requests.get(url).json()


    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(title, desc, img)
    context = {'mylist': mylist}

    return render(request,'index.html', context)

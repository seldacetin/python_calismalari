from django.shortcuts import render

kategoriler = ["Macera","Komedi","Bilim Kurgu"]
filmler = [
    {
        "id": 1,
        "film_adi" : "Film 1",
        "aciklama" : "Film 1 aciklama",
        "resim" : "1.jpeg",
        "anasayfa" : True
    },
    {
        "id": 2,
        "film_adi" : "Film 2",
        "aciklama" : "Film 2 aciklama",
        "resim" : "2.jpeg",
        "anasayfa" : False
    },
    {
        "id": 3,
        "film_adi" : "Film 3",
        "aciklama" : "Film 3 aciklama",
        "resim" : "3.jpeg",
        "anasayfa" : True
    },
    {
        "id": 4,
        "film_adi" : "Film 4",
        "aciklama" : "Film 4 aciklama",
        "resim" : "4.jpeg",
        "anasayfa" : False
    }

]

def home(request):
    data = {
        "Kategori" : kategoriler ,
        "Film" : filmler
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "Kategori" : kategoriler ,
        "Film" : filmler
    }
    return render(request, "movies.html", data)
    
def moviedetails(request, id):
    data = {
       "id" : id,
    }
    return render(request, "details.html", data)

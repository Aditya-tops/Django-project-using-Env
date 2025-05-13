from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    list = Movies.objects.all()

    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        # list = list.filter(name=movie_name)
        list = list.filter(name__icontains=movie_name)

    paginator = Paginator(list,3)
    page = request.GET.get('page')
    list = paginator.get_page(page)

    return render(request,'myapp/movie_list.html',{'list':list})


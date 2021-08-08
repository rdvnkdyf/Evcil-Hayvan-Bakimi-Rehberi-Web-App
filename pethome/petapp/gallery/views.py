# posts/views.py
from django.views.generic import ListView
from .models import Image


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render 

def ImageList(request):
    object_list = Image.objects.all()
    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'gallery.html',
                  {'page': page,
                   'post_list': post_list})
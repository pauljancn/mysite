from django.shortcuts import render
from suanpi.models import BlogPost
from django.template.context_processors import request

# Create your views here.
def suanpi_index(request):
    suanpi_list = BlogPost.objects.all()
    return render(request,'index.html',{'suanpi_list':suanpi_list})

def test(request):
    return render(request,'test.html')

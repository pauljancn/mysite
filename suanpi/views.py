from django.shortcuts import render
from suanpi.models import *
from django.template.context_processors import request
# Create your views here.
def fee_index(request):
    fee_list = Tblfee.objects.all()
    return render(request,'index.html',{'fee_list':fee_list})

#def test(request):
#    return render(request,'test.html')

# -*- coding: utf-8 -*-
from django.shortcuts import render
from suanpi.models import *
from django.template.context_processors import request
from django.conf import settings
# Create your views here.

def global_setting(request):
    return{
        'SITE_URL': settings.SITE_URL,
        'CUR_URL': request.get_host().split('.',1)[0],
        }

def fee_index(request):
    fee_list = Tblfee.objects.all()
    return render(request,'index.html',{'fee_list':fee_list})

#def test(request):
#    return render(request,'test.html')

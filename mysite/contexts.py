#!/bin/bash/python 
# -*- coding: utf-8 -*-
# ȫ�ֱ���

from django.conf import settings

def lang(request):
    return {'lang': settings.LANGUAGE_CODE}
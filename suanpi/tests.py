# -*- coding: utf-8 -*-
from django.test import TestCase
from alisms.demo_sms_send import *
import uuid
import os

# Create your tests here.

def hostname():
    sys = os.name
    if sys == 'nt':
        hostname = os.getenv('computername')
        return hostname
    elif sys == 'posix':
        host = os.popen('echo $HOSTNAME')
        try:
            hostname = host.read()
            return hostname
        finally:
            host.close()
    else:
        return 'UNKNOW HOSTNAME'
    
hostname()

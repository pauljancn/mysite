# -*- coding: utf-8 -*-
from django.test import TestCase
from alisms.demo_sms_send import *
import uuid

# Create your tests here.

__business_id = uuid.uuid1()
params = "{\"code\":\"1234\",\"product\":\"yifawang\"}"
print (send_sms(__business_id, '13331175692','易发网','SMS_143862335', params))
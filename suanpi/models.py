# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Forbitinfo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    charkey = models.CharField(db_column='charKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charrefurl = models.CharField(db_column='charRefURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=52, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ForbitInfo'


class Tbladuser(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtfrom = models.DateTimeField(db_column='dtFrom', blank=True, null=True)  # Field name made lowercase.
    dtto = models.DateTimeField(db_column='dtTo', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdUser'


class Tbladdress(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intareaid = models.IntegerField(db_column='intAreaID', blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chararea = models.CharField(db_column='charArea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charalias = models.CharField(db_column='charAlias', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAddress'


class Tbladmin(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charadmin = models.CharField(db_column='charAdmin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charpwd = models.CharField(db_column='charPwd', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intpower = models.SmallIntegerField(db_column='intPower', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAdmin'


class Tblarea(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intcityid = models.SmallIntegerField(db_column='intCityID', blank=True, null=True)  # Field name made lowercase.
    chararea = models.CharField(db_column='charArea', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charareapy = models.CharField(db_column='charAreaPY', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblArea'


class Tblareadict(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intparentid = models.IntegerField(db_column='intParentID', blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charpy = models.CharField(db_column='charPY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intjibie = models.SmallIntegerField(db_column='intJibie', blank=True, null=True)  # Field name made lowercase.
    charcityurl = models.CharField(db_column='charCityURL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAreaDict'


class Tblbadstr(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    charkey = models.CharField(db_column='charKey', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    charbtel = models.CharField(db_column='charBTel', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    charneedconfirmkey = models.CharField(db_column='charNeedConfirmKey', max_length=800, blank=True, null=True)  # Field name made lowercase.
    charlimitedtels = models.CharField(db_column='charLimitedTels', max_length=800, blank=True, null=True)  # Field name made lowercase.
    charfilterstr = models.CharField(db_column='charFilterStr', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBadStr'


class Tblbigclass(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charbigclass = models.CharField(db_column='charBigClass', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBigClass'


class Tblbless(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    chartoname = models.CharField(db_column='charToName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBless'


class Tblchat(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charnickname = models.CharField(db_column='charNickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charphoto = models.CharField(db_column='charPhoto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsg = models.CharField(db_column='charMsg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblChat'


class Tblcity(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charcitypy = models.CharField(db_column='charCityPY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charcityurl = models.CharField(db_column='charCityURL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    intarrstart = models.SmallIntegerField(db_column='intArrStart', blank=True, null=True)  # Field name made lowercase.
    intarrend = models.SmallIntegerField(db_column='intArrEnd', blank=True, null=True)  # Field name made lowercase.
    charcode = models.CharField(db_column='charCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chartq = models.CharField(db_column='charTQ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCity'


class Tblcolsdict(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intparentid = models.IntegerField(db_column='intParentID', blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charpy = models.CharField(db_column='charPY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intjibie = models.SmallIntegerField(db_column='intJibie', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charpy2 = models.CharField(db_column='charPY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartitle = models.CharField(db_column='charTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblColsDict'


class Tblconfirmcode(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcode = models.CharField(db_column='charCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblConfirmCode'


class Tbldelcode(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    charcode = models.CharField(db_column='charCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bitifdeleted = models.NullBooleanField(db_column='bitIfDeleted')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDelCode'


class Tbldeleteupdate(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDeleteUpdate'


class Tblerror(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=180, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblError'


class Tblfee(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intbalance = models.FloatField(db_column='intBalance', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFee'


class Tblfeeing(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intpayout = models.FloatField(db_column='intPayOut', blank=True, null=True)  # Field name made lowercase.
    intpaytype = models.IntegerField(db_column='intPayType', blank=True, null=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFeeing'


class Tblfileinfo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    chartype = models.CharField(db_column='charType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    intdeal = models.SmallIntegerField(db_column='intDeal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFileInfo'


class Tblforbitip(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblForbitIP'


class Tblfriend(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intfrienduserid = models.IntegerField(db_column='intFriendUserID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFriend'


class Tblfriendlink(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charpic = models.CharField(db_column='charPic', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFriendLink'


class TblfriendlinkFirst(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFriendLink_First'


class Tblguestbook(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    chartitle = models.CharField(db_column='charTitle', max_length=80, blank=True, null=True)  # Field name made lowercase.
    chardetail = models.CharField(db_column='charDetail', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    charsex = models.CharField(db_column='charSex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    charphone = models.CharField(db_column='charPhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charback = models.CharField(db_column='charBack', max_length=400, blank=True, null=True)  # Field name made lowercase.
    dtback = models.DateTimeField(db_column='dtBack', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGuestBook'


class Tblinfo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo'


class TblinfoAll(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All'


class TblinfoAllBj(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_bj'


class TblinfoAllCd(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_cd'


class TblinfoAllGz(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_gz'


class TblinfoAllHz(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_hz'


class TblinfoAllJn(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_jn'


class TblinfoAllNj(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_nj'


class TblinfoAllSh(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_sh'


class TblinfoAllSuzhou(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_suzhou'


class TblinfoAllSz(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_sz'


class TblinfoAllTj(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_tj'


class TblinfoAllWh(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_wh'


class TblinfoAllZz(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_All_zz'


class TblinfoHouseadd(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    charxiaoqu = models.CharField(db_column='charXiaoqu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charpeitao = models.CharField(db_column='charPeitao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    charrenttype = models.CharField(db_column='charRentType', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charceng1 = models.CharField(db_column='charCeng1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    charceng2 = models.CharField(db_column='charCeng2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    charniandai = models.CharField(db_column='charNiandai', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_HouseAdd'


class TblinfoHuochepiao(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charareafrom = models.CharField(db_column='charAreaFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charareato = models.CharField(db_column='charAreaTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartype = models.CharField(db_column='charType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtgotime = models.DateTimeField(db_column='dtGoTime', blank=True, null=True)  # Field name made lowercase.
    charcheci = models.CharField(db_column='charCheci', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intnum = models.IntegerField(db_column='intNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_Huochepiao'


class TblinfoIndex(models.Model):
    indexid = models.IntegerField(db_column='IndexID')  # Field name made lowercase.
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3080, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    timestamp = models.TextField(blank=True, null=True)  # This field type is a guess.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_Index'


class TblinfoNo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intsource = models.SmallIntegerField(db_column='intSource', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    intprice = models.FloatField(db_column='intPrice', blank=True, null=True)  # Field name made lowercase.
    intmianji = models.FloatField(db_column='intMianji', blank=True, null=True)  # Field name made lowercase.
    charhx1 = models.SmallIntegerField(db_column='charHX1', blank=True, null=True)  # Field name made lowercase.
    charhx2 = models.CharField(db_column='charHX2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx3 = models.CharField(db_column='charHX3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx4 = models.CharField(db_column='charHX4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charhx5 = models.SmallIntegerField(db_column='charHX5', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.SmallIntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    intstatus = models.SmallIntegerField(db_column='intStatus', blank=True, null=True)  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    intreview = models.IntegerField(db_column='intReview', blank=True, null=True)  # Field name made lowercase.
    charmaps = models.CharField(db_column='charMaps', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intforbit = models.SmallIntegerField(db_column='intForbit', blank=True, null=True)  # Field name made lowercase.
    intorder = models.IntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    bitimgtel = models.NullBooleanField(db_column='bitImgTel')  # Field name made lowercase.
    charkey = models.CharField(db_column='charKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_NO'


class TblinfoResend(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intrefresh = models.IntegerField(db_column='intRefresh', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_ReSend'


class TblinfoReview(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    charremark = models.CharField(db_column='charRemark', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charnickname = models.CharField(db_column='charNickName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charsex = models.CharField(db_column='charSex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_Review'


class TblinfoUp(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID')  # Field name made lowercase.
    dtfrom = models.DateTimeField(db_column='dtFrom', blank=True, null=True)  # Field name made lowercase.
    dtto = models.DateTimeField(db_column='dtTo', blank=True, null=True)  # Field name made lowercase.
    intbcid = models.IntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.IntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intorder = models.SmallIntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charscope = models.CharField(db_column='charScope', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bitiffirst = models.NullBooleanField(db_column='bitIfFirst')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_Up'


class TblinfoUpAlone(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID')  # Field name made lowercase.
    dtfrom = models.DateTimeField(db_column='dtFrom', blank=True, null=True)  # Field name made lowercase.
    dtto = models.DateTimeField(db_column='dtTo', blank=True, null=True)  # Field name made lowercase.
    intbcid = models.IntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.IntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.CharField(db_column='intSTCID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intorder = models.SmallIntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInfo_Up_Alone'


class Tbljoke(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    chartitle = models.CharField(db_column='charTitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charlaiyuan = models.CharField(db_column='charLaiyuan', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    dtnew = models.DateTimeField(db_column='dtNew', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblJoke'


class Tbljubao(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblJuBao'


class Tbllogininfo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charusername = models.CharField(db_column='charUserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=24, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intusertype = models.SmallIntegerField(db_column='intUserType', blank=True, null=True)  # Field name made lowercase.
    charpwd = models.CharField(db_column='charPwd', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charregip = models.CharField(db_column='charRegIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dtregist = models.DateTimeField(db_column='dtRegist', blank=True, null=True)  # Field name made lowercase.
    dtlastlogin = models.DateTimeField(db_column='dtLastLogin', blank=True, null=True)  # Field name made lowercase.
    intlogintimes = models.IntegerField(db_column='intLoginTimes', blank=True, null=True)  # Field name made lowercase.
    intpoint = models.IntegerField(db_column='intPoint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLoginInfo'


class Tbllooksystemmsg(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intmsgid = models.IntegerField(db_column='intMsgID', blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLookSystemMsg'


class Tblmessage(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chardetail = models.CharField(db_column='charDetail', max_length=600, blank=True, null=True)  # Field name made lowercase.
    bitiflooked = models.NullBooleanField(db_column='bitIfLooked')  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    intuseridfrom = models.IntegerField(db_column='intUserIDFrom', blank=True, null=True)  # Field name made lowercase.
    intuseridto = models.IntegerField(db_column='intUserIDTo', blank=True, null=True)  # Field name made lowercase.
    ifsystem = models.NullBooleanField(db_column='ifSystem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMessage'


class Tblmobile(models.Model):
    intstart = models.IntegerField(db_column='intStart', blank=True, null=True)  # Field name made lowercase.
    intend = models.IntegerField(db_column='intEnd', blank=True, null=True)  # Field name made lowercase.
    charprov = models.CharField(db_column='charProv', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grade = models.IntegerField(blank=True, null=True)
    thank = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblMobile'

class TblmobileNew(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charnum = models.CharField(db_column='charNum', max_length=11, blank=True, null=True)  # Field name made lowercase.
    chararea = models.CharField(db_column='charArea', max_length=30, blank=True, null=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMobile_New'


class Tblnavsource(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charrealip = models.CharField(db_column='charRealIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charsource = models.CharField(db_column='charSource', max_length=200, blank=True, null=True)  # Field name made lowercase.
    charboturl = models.CharField(db_column='charBotURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNavSource'


class Tblonline(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charnickname = models.CharField(db_column='charNickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtlogintime = models.DateTimeField(db_column='dtLoginTime', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblOnline'


class Tblsfz(models.Model):
    bm = models.IntegerField(db_column='BM', blank=True, null=True)  # Field name made lowercase.
    dq = models.CharField(db_column='DQ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSFZ'


class Tblsearchlog(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charser = models.CharField(db_column='charSer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intser = models.IntegerField(db_column='intSer', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtser = models.DateTimeField(db_column='dtSer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSearchLog'


class Tblshoucang(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=120, blank=True, null=True)  # Field name made lowercase.
    chartitle = models.CharField(db_column='charTitle', max_length=80, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intfolderid = models.IntegerField(db_column='intFolderID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblShoucang'


class Tblsmallcols(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intbigcolsid = models.SmallIntegerField(db_column='intBigColsID', blank=True, null=True)  # Field name made lowercase.
    charsmallcols = models.CharField(db_column='charSmallCols', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charfolder = models.CharField(db_column='charFolder', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charalias = models.CharField(db_column='charAlias', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSmallCols'


class Tblsmallestcols(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intsmallcols = models.IntegerField(db_column='intSmallCols', blank=True, null=True)  # Field name made lowercase.
    charsmallestcols = models.CharField(db_column='charSmallestCols', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charalias = models.CharField(db_column='charAlias', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSmallestCols'


class Tblstat(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charreferer = models.CharField(db_column='charReferer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    chartitle = models.CharField(db_column='charTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intlevel = models.SmallIntegerField(db_column='intLevel', blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStat'


class Tbltags(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    chartag = models.CharField(db_column='charTag', max_length=20)  # Field name made lowercase.
    intinfoid = models.IntegerField(db_column='intInfoID')  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intzid = models.SmallIntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTags'


class Tbltagstop(models.Model):
    chartag = models.CharField(db_column='charTag', max_length=20, blank=True, null=True)  # Field name made lowercase.
    intcount = models.IntegerField(db_column='intCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTagsTop'


class Tbltrain(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    checi = models.CharField(db_column='Checi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    station = models.CharField(db_column='Station', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s_no = models.SmallIntegerField(db_column='S_No', blank=True, null=True)  # Field name made lowercase.
    daynum = models.SmallIntegerField(db_column='DayNum', blank=True, null=True)  # Field name made lowercase.
    a_time = models.CharField(db_column='A_Time', max_length=20, blank=True, null=True)  # Field name made lowercase.
    d_time = models.CharField(db_column='D_Time', max_length=20, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(db_column='Distance', blank=True, null=True)  # Field name made lowercase.
    p1 = models.CharField(db_column='P1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    p2 = models.CharField(db_column='P2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    p3 = models.CharField(db_column='P3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    p4 = models.CharField(db_column='P4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    endstation = models.CharField(db_column='EndStation', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTrain'


class Tblupalone(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intbcid = models.IntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.IntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.IntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtfrom = models.DateTimeField(db_column='dtFrom', blank=True, null=True)  # Field name made lowercase.
    dtto = models.DateTimeField(db_column='dtTo', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUpAlone'


class Tbluser(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charusername = models.CharField(db_column='charUserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charnickname = models.CharField(db_column='charNickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charsex = models.CharField(db_column='charSex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bitdistel = models.NullBooleanField(db_column='bitDisTel')  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=24, blank=True, null=True)  # Field name made lowercase.
    bitdismobile = models.NullBooleanField(db_column='bitDisMobile')  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bitdisemail = models.NullBooleanField(db_column='bitDisEmail')  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bitdisqq = models.NullBooleanField(db_column='bitDisQQ')  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bitdismsn = models.NullBooleanField(db_column='bitDisMSN')  # Field name made lowercase.
    charquestion = models.CharField(db_column='charQuestion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charanswer = models.CharField(db_column='charAnswer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    charprov = models.CharField(db_column='charProv', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=30, blank=True, null=True)  # Field name made lowercase.
    charblogurl = models.CharField(db_column='charBlogURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    charphoto = models.CharField(db_column='charPhoto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charsign = models.CharField(db_column='charSign', max_length=400, blank=True, null=True)  # Field name made lowercase.
    intpoint = models.IntegerField(db_column='intPoint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUser'


class Tbluserproduct(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtstart = models.DateTimeField(db_column='dtStart', blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUserProduct'


class Tblwebsite(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    intlevel = models.SmallIntegerField(db_column='intLevel', blank=True, null=True)  # Field name made lowercase.
    charhouzhui = models.CharField(db_column='charHouzhui', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtend = models.DateTimeField(db_column='dtEnd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblWebSite'


class Tblxiaoqu(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    intareaid = models.IntegerField(db_column='intAreaID', blank=True, null=True)  # Field name made lowercase.
    intaddressid = models.IntegerField(db_column='intAddressID', blank=True, null=True)  # Field name made lowercase.
    inttype = models.SmallIntegerField(db_column='intType', blank=True, null=True)  # Field name made lowercase.
    charsourceurl = models.CharField(db_column='charSourceURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.
    firstpy = models.CharField(db_column='FirstPY', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblXiaoqu'


class Tblyellowpage(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charsimname = models.CharField(db_column='charSimName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    charcontactor = models.CharField(db_column='charContactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chartel = models.CharField(db_column='charTel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charaddress = models.CharField(db_column='charAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    charmobile = models.CharField(db_column='charMobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charqq = models.CharField(db_column='charQQ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charmsn = models.CharField(db_column='charMSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charemail = models.CharField(db_column='charEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charurl = models.CharField(db_column='charURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intbcid = models.IntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.CharField(db_column='intSCID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intzid = models.IntegerField(db_column='intZID', blank=True, null=True)  # Field name made lowercase.
    intaid = models.IntegerField(db_column='intAID', blank=True, null=True)  # Field name made lowercase.
    bitifconfirm = models.NullBooleanField(db_column='bitIfConfirm')  # Field name made lowercase.
    intdot = models.IntegerField(db_column='intDot', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charkey = models.CharField(db_column='charKey', max_length=80, blank=True, null=True)  # Field name made lowercase.
    chardis = models.CharField(db_column='charDis', max_length=200, blank=True, null=True)  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblYellowPage'


class TblyellowpageItemprice(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intypid = models.IntegerField(db_column='intYPID', blank=True, null=True)  # Field name made lowercase.
    intcityid = models.SmallIntegerField(db_column='intCityID', blank=True, null=True)  # Field name made lowercase.
    intbcid = models.SmallIntegerField(db_column='intBCID', blank=True, null=True)  # Field name made lowercase.
    intscid = models.SmallIntegerField(db_column='intSCID', blank=True, null=True)  # Field name made lowercase.
    intstcid = models.SmallIntegerField(db_column='intSTCID', blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chardemo = models.CharField(db_column='charDemo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    intuserid = models.IntegerField(db_column='intUserID', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    dtupdate = models.DateTimeField(db_column='dtUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblYellowPage_ItemPrice'


class TblyellowpageItems(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    intypid = models.IntegerField(db_column='intYPID', blank=True, null=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    intfileid = models.IntegerField(db_column='intFileID', blank=True, null=True)  # Field name made lowercase.
    intfileid2 = models.IntegerField(db_column='intFileID2', blank=True, null=True)  # Field name made lowercase.
    intfileid3 = models.IntegerField(db_column='intFileID3', blank=True, null=True)  # Field name made lowercase.
    dtadd = models.DateTimeField(db_column='dtAdd', blank=True, null=True)  # Field name made lowercase.
    intorder = models.SmallIntegerField(db_column='intOrder', blank=True, null=True)  # Field name made lowercase.
    charext1 = models.CharField(db_column='charExt1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext2 = models.CharField(db_column='charExt2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    charext3 = models.CharField(db_column='charExt3', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblYellowPage_Items'


class Tblybqh(models.Model):
    id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    charcity = models.CharField(db_column='charCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charprovince = models.CharField(db_column='charProvince', max_length=50, blank=True, null=True)  # Field name made lowercase.
    charpostcode = models.CharField(db_column='charPostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    charphonecode = models.CharField(db_column='charPhoneCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chararea = models.CharField(db_column='charArea', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intexhibitionid = models.IntegerField(db_column='intExhibitionid', blank=True, null=True)  # Field name made lowercase.
    intactorid = models.IntegerField(db_column='intActorid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblybqh'


class Tmpfileinfo(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    charip = models.CharField(db_column='charIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charmemo = models.CharField(db_column='charMemo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpFileInfo'

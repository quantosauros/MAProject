# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class EtfCategory(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETF_CATEGORY'


class EtfData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45)  # Field name made lowercase.
    price_close = models.FloatField(db_column='PRICE_CLOSE', blank=True, null=True)  # Field name made lowercase.
    price_open = models.FloatField(db_column='PRICE_OPEN', blank=True, null=True)  # Field name made lowercase.
    price_high = models.FloatField(db_column='PRICE_HIGH', blank=True, null=True)  # Field name made lowercase.
    price_low = models.FloatField(db_column='PRICE_LOW', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETF_DATA'
        unique_together = (('DT', 'TICKER'),)


class EtfInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category_code = models.CharField(db_column='CATEGORY_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fund_family = models.CharField(db_column='FUND_FAMILY', max_length=90, blank=True, null=True)  # Field name made lowercase.
    exchange = models.CharField(db_column='EXCHANGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccy_cd = models.CharField(db_column='CCY_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETF_INFO'
        
class FuturesData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    overnight_cd = models.CharField(db_column='OVERNIGHT_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    close_price = models.FloatField(db_column='CLOSE_PRICE', blank=True, null=True)  # Field name made lowercase.
    open_price = models.FloatField(db_column='OPEN_PRICE', blank=True, null=True)  # Field name made lowercase.
    high_price = models.FloatField(db_column='HIGH_PRICE', blank=True, null=True)  # Field name made lowercase.
    low_price = models.FloatField(db_column='LOW_PRICE', blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    settlement_price = models.FloatField(db_column='SETTLEMENT_PRICE', blank=True, null=True)  # Field name made lowercase.
    spot_price = models.FloatField(db_column='SPOT_PRICE', blank=True, null=True)  # Field name made lowercase.
    outstanding_volume = models.IntegerField(db_column='OUTSTANDING_VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUTURES_DATA'
        unique_together = (('DT', 'TICKER', 'OVERNIGHT_CD'),)


class FuturesInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    short_ticker = models.CharField(db_column='SHORT_TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    expire_dt = models.CharField(db_column='EXPIRE_DT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    spread_type = models.CharField(db_column='SPREAD_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    type_cd = models.CharField(db_column='TYPE_CD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUTURES_INFO'
        
class FuturesInvestor(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    overnight_cd = models.CharField(db_column='OVERNIGHT_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    investor_cd = models.CharField(db_column='INVESTOR_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    buy_amount = models.FloatField(db_column='BUY_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    buy_volume = models.FloatField(db_column='BUY_VOLUME', blank=True, null=True)  # Field name made lowercase.
    sell_amount = models.FloatField(db_column='SELL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    sell_volume = models.FloatField(db_column='SELL_VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUTURES_INVESTOR'
        unique_together = (('DT', 'TICKER', 'OVERNIGHT_CD', 'INVESTOR_CD'),)


class FxData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price_close = models.FloatField(db_column='PRICE_CLOSE', blank=True, null=True)  # Field name made lowercase.
    price_open = models.FloatField(db_column='PRICE_OPEN', blank=True, null=True)  # Field name made lowercase.
    price_high = models.FloatField(db_column='PRICE_HIGH', blank=True, null=True)  # Field name made lowercase.
    price_low = models.FloatField(db_column='PRICE_LOW', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FX_DATA'
        unique_together = (('DT', 'TICKER'),)


class FxInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ccy1 = models.CharField(db_column='CCY1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccy2 = models.CharField(db_column='CCY2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FX_INFO'


class IndexData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price_close = models.FloatField(db_column='PRICE_CLOSE', blank=True, null=True)  # Field name made lowercase.
    price_open = models.FloatField(db_column='PRICE_OPEN', blank=True, null=True)  # Field name made lowercase.
    price_high = models.FloatField(db_column='PRICE_HIGH', blank=True, null=True)  # Field name made lowercase.
    price_low = models.FloatField(db_column='PRICE_LOW', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INDEX_DATA'
        unique_together = (('DT', 'TICKER'),)


class IndexInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    exchange = models.CharField(db_column='EXCHANGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INDEX_INFO'

class IrData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    value1 = models.FloatField(db_column='VALUE1', blank=True, null=True)  # Field name made lowercase.
    value2 = models.FloatField(db_column='VALUE2', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IR_DATA'
        unique_together = (('DT', 'TICKER'),)


class IrInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    irc_cd = models.CharField(db_column='IRC_CD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mrty_cd = models.CharField(db_column='MRTY_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IR_INFO'




class StockData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45)  # Field name made lowercase.
    price_close = models.FloatField(db_column='PRICE_CLOSE', blank=True, null=True)  # Field name made lowercase.
    price_open = models.FloatField(db_column='PRICE_OPEN', blank=True, null=True)  # Field name made lowercase.
    price_high = models.FloatField(db_column='PRICE_HIGH', blank=True, null=True)  # Field name made lowercase.
    price_low = models.FloatField(db_column='PRICE_LOW', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK_DATA'
        unique_together = (('DT', 'TICKER'),)

class StockDetail(models.Model):
    #idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ma_200 = models.FloatField(db_column='MA_200', blank=True, null=True)  # Field name made lowercase.
    ma_50 = models.FloatField(db_column='MA_50', blank=True, null=True)  # Field name made lowercase.
    book_value = models.FloatField(db_column='BOOK_VALUE', blank=True, null=True)  # Field name made lowercase.
    volume_avg = models.FloatField(db_column='VOLUME_AVG', blank=True, null=True)  # Field name made lowercase.
    ebitda = models.FloatField(db_column='EBITDA', blank=True, null=True)  # Field name made lowercase.
    dividend_yield = models.FloatField(db_column='DIVIDEND_YIELD', blank=True, null=True)  # Field name made lowercase.
    market_cap = models.FloatField(db_column='MARKET_CAP', blank=True, null=True)  # Field name made lowercase.
    year_high = models.FloatField(db_column='YEAR_HIGH', blank=True, null=True)  # Field name made lowercase.
    year_low = models.FloatField(db_column='YEAR_LOW', blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK_DETAIL'
        unique_together = (('DT', 'TICKER'),)




class StockInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    exchange = models.CharField(db_column='EXCHANGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ccy_cd = models.CharField(db_column='CCY_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK_INFO'


class XpathData(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    xpath_code = models.CharField(db_column='XPATH_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    xpath = models.CharField(db_column='XPATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    xpath_index = models.IntegerField(db_column='XPATH_INDEX', blank=True, null=True)  # Field name made lowercase.
    use = models.CharField(db_column='USE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    insert_column = models.CharField(db_column='INSERT_COLUMN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #crtn_time = models.DateTimeField(db_column='CRTN_TIME', blank=True, null=True)  # Field name made lowercase.
    #update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XPATH_DATA'


class XpathInfo(models.Model):
    idx = models.AutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    sitecode = models.CharField(db_column='SITECODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'XPATH_INFO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
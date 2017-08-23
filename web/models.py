from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
    	return "{}-token".format(self.user)

class Expense(models.Model):
    text = models.CharField(_('text'),max_length=255)
    amount = models.BigIntegerField(_('amount'))
    date = models.DateTimeField(_('date'))
    user = models.ForeignKey(User,verbose_name=_('user'))
    def __unicode__(self):
    	return "{}-{}".format(self.text,self.amount)
    def __str__(self):
    	return "{}-{}".format(self.text,self.amount)

class Income(models.Model):
    text = models.CharField(_('text'),max_length=255)
    amount = models.BigIntegerField(_('amount'))
    date = models.DateTimeField(_('date'))
    user = models.ForeignKey(User,verbose_name=_('user'))
    def __unicode__(self):
    	return "{}-{}".format(self.text,self.amount)
    def __str__(self):
    	return "{}-{}".format(self.text,self.amount)
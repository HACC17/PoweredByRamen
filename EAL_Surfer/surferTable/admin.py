# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from surferTable.models import *
from django.apps import apps

for model in apps.get_app_config('surferTable').models.values():

    admin.site.register(model)

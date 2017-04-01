#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    :  Jason
# @Mail      :  jczhangmail@126.com
# @File      :  glance.py

from flask import Blueprint,render_template


glance = Blueprint('glance',__name__,url_prefix='/rally/glance')


@glance.route('/')
@glance.route('/index')
def index():
    return render_template('rally/glance/glance_index.html')

@glance.route('/detail')
def detail():
    return render_template("rally/glance/glance_detail.html")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    :  Jason
# @Mail      :  jczhangmail@126.com
# @File      :  neutron.py

from flask import Blueprint,render_template


neutron = Blueprint('neutron',__name__,url_prefix='/raly/neutron')


@neutron.route('/')
@neutron.route('/index')
def index():
    return render_template('rally/neutron/neutron_index.html')

@neutron.route('/detail')
def detail():
    return render_template("rally/neutron/neutron_detail.html")
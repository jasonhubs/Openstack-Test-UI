#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jason
# @Mail    : jczhangmail@126.com
# @File    : keystone.py

from flask import Blueprint,render_template,send_file


rally_keystone = Blueprint('rally_keystone',__name__,url_prefix='/rally/keystone')


@rally_keystone.route('/')
@rally_keystone.route('/index')
def index():
    return render_template('rally/keystone/keystone_index.html')

@rally_keystone.route('/detail')
def detail():
    return send_file("templates/rally/keystone/test2.html")